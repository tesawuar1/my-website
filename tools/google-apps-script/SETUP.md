# Enquiry database: Google Sheet + email alerts

> The real email addresses are kept only in the live script in your Google account
> (script.google.com, project "Komodo & Ko. Enquiries"). Replace the placeholders below
> with your own addresses if you ever set this up again from scratch.

Every enquiry sent from the website form ("Send via WhatsApp" or "Send via Email")
is saved as a new row in a Google Sheet, and an email alert goes to:

- **YOUR-MAIN-ADDRESS@gmail.com** (owns the sheet)
- **YOUR-BACKUP-ADDRESS@gmail.com** (backup: has edit access to the same sheet)

It is free and runs in your own Google account. Setup takes about 5 minutes and is done once.

## 1. Create the script
1. Sign in to Google as **YOUR-MAIN-ADDRESS@gmail.com**.
2. Go to <https://script.google.com> and click **New project**.
3. Name it `Komodo & Ko. Enquiries` (top left).
4. Delete the sample code, then paste in everything from `tools/google-apps-script/Code.gs`.
5. Click **Save** (disk icon).

## 2. Create the sheet
1. In the toolbar, choose the function **setup** and click **Run**.
2. Google asks for permission. Click **Review permissions**, choose YOUR-MAIN-ADDRESS@gmail.com,
   then **Advanced > Go to Komodo & Ko. Enquiries (unsafe) > Allow**.
   ("Unsafe" only means the script is your own and not reviewed by Google.)
3. When it finishes, a sheet called **Komodo & Ko. Enquiries** is in your Google Drive,
   and YOUR-BACKUP-ADDRESS@gmail.com receives an email that it was shared with them.

## 3. Turn on the web link
1. Click **Deploy > New deployment**.
2. Click the gear next to "Select type" and choose **Web app**.
3. Set **Execute as: Me (YOUR-MAIN-ADDRESS@gmail.com)** and **Who has access: Anyone**.
4. Click **Deploy** and copy the **Web app URL** (it ends in `/exec`).
5. Open the URL in a browser. You should see: *Komodo & Ko. enquiry endpoint is running.*

## 4. Connect the website
1. Open `_build/content_main.py` and paste the URL between the quotes of `"enquiry_endpoint": ""`.
2. Rebuild and upload:
   ```
   python _build/build.py
   git add -u
   git commit -m "Connect enquiry form to Google Sheet"
   git push
   ```
3. Redeploy on Hostinger.

## 5. Test it
Fill in the enquiry form on the live site and press either button. Within a few seconds
a new row appears in the sheet and both addresses get an email.

## Good to know
- **What is captured:** enquiries submitted through the website form. Messages people
  send to your WhatsApp or email directly (without using the form) are not captured;
  that would need the paid WhatsApp Business API or a Gmail filter.
- **Status column:** the last column starts as "New"; change it to "Replied", "Booked", etc.
- **Changing the alert addresses:** edit `OWNER_EMAIL` / `BACKUP_EMAIL` at the top of the
  script, save, then **Deploy > Manage deployments > Edit > Version: New version > Deploy**.
  The URL stays the same.
- **Limits:** a free Gmail account can send about 100 alert emails per day.
- **Spam:** the form has a hidden trap field; submissions from bots that fill it are ignored.
