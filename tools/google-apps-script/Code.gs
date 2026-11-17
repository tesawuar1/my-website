/**
 * Komodo & Ko. — enquiry database
 *
 * Receives every enquiry sent from the website's enquiry form (both the
 * "Send via WhatsApp" and "Send via Email" buttons), adds it as a row in a
 * Google Sheet, and emails a notification to the addresses below.
 *
 * Set-up (once, signed in as YOUR-MAIN-ADDRESS@gmail.com):
 *   1. Run setup() once and allow the permissions it asks for.
 *   2. Deploy > New deployment > Web app: Execute as "Me", access "Anyone".
 *   3. Copy the Web app URL into _build/content_main.py ("enquiry_endpoint")
 *      and rebuild the site.
 * Full steps: tools/google-apps-script/SETUP.md
 */

var OWNER_EMAIL = "YOUR-MAIN-ADDRESS@gmail.com";     // owns the sheet, gets notifications
var BACKUP_EMAIL = "YOUR-BACKUP-ADDRESS@gmail.com";    // shared as editor, gets notifications
var SHEET_NAME = "Enquiries";
var HEADERS = ["Received", "Sent via", "Name", "Phone / WhatsApp", "Email", "Travel dates",
               "Guests", "Service / experience", "Estimated budget", "Language", "Page", "Status"];

/** Run once: creates the spreadsheet, adds headers and shares it with the backup address. */
function setup() {
  var props = PropertiesService.getScriptProperties();
  var id = props.getProperty("SHEET_ID");
  var ss = id ? SpreadsheetApp.openById(id) : SpreadsheetApp.create("Komodo & Ko. Enquiries");
  var sh = ss.getSheetByName(SHEET_NAME) || ss.getSheets()[0].setName(SHEET_NAME);
  if (sh.getLastRow() === 0) {
    sh.appendRow(HEADERS);
    sh.getRange(1, 1, 1, HEADERS.length).setFontWeight("bold").setBackground("#283926").setFontColor("#f4f0e3");
    sh.setFrozenRows(1);
    sh.setColumnWidths(1, HEADERS.length, 170);
  }
  if (BACKUP_EMAIL) ss.addEditor(BACKUP_EMAIL);
  props.setProperty("SHEET_ID", ss.getId());
  Logger.log("Sheet ready: " + ss.getUrl());
  return ss.getUrl();
}

/** Website posts here. Body is JSON sent as text/plain (avoids browser pre-flight checks). */
function doPost(e) {
  try {
    var d = JSON.parse((e && e.postData && e.postData.contents) || "{}");
    if (d.website) return reply({ ok: true });                 // hidden spam trap was filled in
    var required = ["name", "phone", "email", "dates", "guests", "service", "budget"];
    for (var i = 0; i < required.length; i++) {
      if (!clean(d[required[i]])) return reply({ ok: false, error: "missing " + required[i] });
    }
    var lock = LockService.getScriptLock();
    lock.waitLock(20000);
    try {
      var ss = SpreadsheetApp.openById(PropertiesService.getScriptProperties().getProperty("SHEET_ID"));
      var sh = ss.getSheetByName(SHEET_NAME);
      var row = [new Date(), d.channel === "wa" ? "WhatsApp" : "Email", clean(d.name), clean(d.phone),
                 clean(d.email), clean(d.dates), clean(d.guests), clean(d.service), clean(d.budget),
                 d.lang === "id" ? "Indonesian" : "English", clean(d.page), "New"];
      sh.appendRow(row);
    } finally {
      lock.releaseLock();
    }
    notify(d, ss.getUrl());
    return reply({ ok: true });
  } catch (err) {
    return reply({ ok: false, error: String(err) });
  }
}

/** Lets you open the Web app URL in a browser to check it is running. */
function doGet() {
  return ContentService.createTextOutput("Komodo & Ko. enquiry endpoint is running.");
}

function notify(d, sheetUrl) {
  var via = d.channel === "wa" ? "WhatsApp" : "Email";
  var subject = "New enquiry: " + clean(d.name) + " (" + clean(d.dates) + ", " + clean(d.guests) + " guests)";
  var lines = [
    "A new enquiry was submitted on the website (sent via " + via + ").", "",
    "Name: " + clean(d.name),
    "Phone / WhatsApp: " + clean(d.phone),
    "Email: " + clean(d.email),
    "Travel dates: " + clean(d.dates),
    "Guests: " + clean(d.guests),
    "Service / experience: " + clean(d.service),
    "Estimated budget: " + clean(d.budget),
    "Language: " + (d.lang === "id" ? "Indonesian" : "English"), "",
    "All enquiries: " + sheetUrl
  ];
  var options = { name: "Komodo & Ko. Website" };
  if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(clean(d.email))) options.replyTo = clean(d.email);
  var to = [OWNER_EMAIL, BACKUP_EMAIL].filter(String).join(",");
  MailApp.sendEmail(to, subject, lines.join("\n"), options);
}

/** Trim, cap length, and stop spreadsheet formulas being injected through the form. */
function clean(v) {
  var s = String(v === undefined || v === null ? "" : v).trim().slice(0, 2000);
  return /^[=+\-@]/.test(s) ? "'" + s : s;
}

function reply(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}
