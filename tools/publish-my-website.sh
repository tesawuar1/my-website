#!/usr/bin/env bash
# Publish the current website to github.com/tesawuar1/my-website (the repository
# Hostinger deploys from) as ONE new commit containing only the current files.
# The full development history stays in komodo-and-ko; my-website never receives
# older versions, so nothing removed from the files reappears there.
#
# Usage (from the project folder, after committing your changes):
#   bash tools/publish-my-website.sh "Short description of the update"
set -euo pipefail
cd "$(dirname "$0")/.."
URL="https://github.com/tesawuar1/my-website.git"
MSG="${1:-Update website}"

if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "You have uncommitted changes. Commit them first." >&2
  exit 1
fi
git fetch -q "$URL" main:refs/remotes/mysite/main
if git cat-file -e "refs/remotes/mysite/main:index.html" 2>/dev/null &&
   [ "$(git rev-parse 'refs/remotes/mysite/main^{tree}')" = "$(git rev-parse 'HEAD^{tree}')" ]; then
  echo "my-website already has these exact files. Nothing to publish."
  exit 0
fi
NEW=$(git commit-tree 'HEAD^{tree}' -p refs/remotes/mysite/main -m "$MSG")
git push "$URL" "$NEW:refs/heads/main"
git update-ref refs/remotes/mysite/main "$NEW"
echo "Published to my-website: $(git rev-parse --short "$NEW")"
echo "Now press Deploy in Hostinger (Websites > Manage > Advanced > GIT), unless Auto Deployment is on."
