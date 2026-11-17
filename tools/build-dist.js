/*
 * Copies the public website files into dist/ for hosts that ask for an
 * "output directory". The site is already built HTML, so nothing is compiled:
 * this only leaves out the editing files (_build, tools, package files).
 * No dependencies needed.  Run:  npm run build
 */
"use strict";
var fs = require("fs");
var path = require("path");

var ROOT = path.resolve(__dirname, "..");
var OUT = path.join(ROOT, "dist");
var SKIP = ["_build", "tools", "dist", "node_modules", "package.json", "package-lock.json",
            "server.js", "README.md", ".git", ".gitignore", ".claude"];

function rmrf(p) {
  if (!fs.existsSync(p)) return;
  if (fs.statSync(p).isDirectory()) {
    fs.readdirSync(p).forEach(function (f) { rmrf(path.join(p, f)); });
    fs.rmdirSync(p);
  } else {
    fs.unlinkSync(p);
  }
}

function copy(src, dst) {
  if (fs.statSync(src).isDirectory()) {
    if (!fs.existsSync(dst)) fs.mkdirSync(dst);
    fs.readdirSync(src).forEach(function (f) { copy(path.join(src, f), path.join(dst, f)); });
  } else {
    fs.writeFileSync(dst, fs.readFileSync(src));
  }
}

rmrf(OUT);
fs.mkdirSync(OUT);
var count = 0;
fs.readdirSync(ROOT).forEach(function (name) {
  if (SKIP.indexOf(name) !== -1) return;
  if (name.charAt(0) === "." && name !== ".nojekyll" && name !== ".htaccess") return;
  copy(path.join(ROOT, name), path.join(OUT, name));
  count++;
});
console.log("Copied " + count + " top-level items into dist/");
