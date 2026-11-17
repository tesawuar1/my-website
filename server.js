/*
 * Tiny static web server for hosts that run the site as a Node.js app.
 * No dependencies needed.  Run:  npm start   (listens on $PORT, default 3000)
 * Serves dist/ if it exists (after "npm run build"), otherwise the project folder.
 */
"use strict";
var http = require("http");
var fs = require("fs");
var path = require("path");

var BASE = fs.existsSync(path.join(__dirname, "dist", "index.html")) ? path.join(__dirname, "dist") : __dirname;
var PORT = process.env.PORT || 3000;
var PRIVATE = /^\/(_build|tools|node_modules|\.git|\.claude)(\/|$)|^\/(server\.js|package(-lock)?\.json|README\.md)$/;
var TYPES = {
  ".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8", ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8", ".md": "text/plain; charset=utf-8", ".txt": "text/plain; charset=utf-8",
  ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp", ".svg": "image/svg+xml",
  ".ico": "image/x-icon", ".woff2": "font/woff2", ".mp4": "video/mp4"
};

function send(res, code, file) {
  var ext = path.extname(file).toLowerCase();
  var long = /\.(jpe?g|png|webp|svg|woff2|mp4)$/.test(ext);
  res.writeHead(code, {
    "Content-Type": TYPES[ext] || "application/octet-stream",
    "Cache-Control": long ? "public, max-age=604800" : "public, max-age=300",
    "X-Content-Type-Options": "nosniff"
  });
  fs.createReadStream(file).pipe(res);
}

function notFound(res) {
  res.writeHead(404, { "Content-Type": "text/html; charset=utf-8" });
  res.end('<!doctype html><meta charset="utf-8"><title>Page not found</title>' +
    '<p style="font-family:sans-serif;padding:40px">This page could not be found. <a href="/">Go to the home page</a></p>');
}

http.createServer(function (req, res) {
  var url;
  try { url = decodeURIComponent(req.url.split("?")[0].split("#")[0]); } catch (e) { res.writeHead(400); return res.end(); }
  if (req.method !== "GET" && req.method !== "HEAD") { res.writeHead(405); return res.end(); }
  if (PRIVATE.test(url) || /(^|\/)\./.test(url)) return notFound(res);
  var file = path.normalize(path.join(BASE, url));
  if (file.indexOf(BASE) !== 0) return notFound(res);          // no escaping the site folder
  fs.stat(file, function (err, st) {
    if (!err && st.isDirectory()) {
      if (url.slice(-1) !== "/") { res.writeHead(301, { Location: url + "/" }); return res.end(); }
      file = path.join(file, "index.html");
      return fs.stat(file, function (e2, s2) { return !e2 && s2.isFile() ? send(res, 200, file) : notFound(res); });
    }
    if (!err && st.isFile()) return send(res, 200, file);
    notFound(res);
  });
}).listen(PORT, function () {
  console.log("Komodo & Ko. website running on port " + PORT + " (serving " + BASE + ")");
});
