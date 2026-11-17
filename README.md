# Komodo & Ko. website

Static website: English at the root, Indonesian in `id/`. No server code needed; upload the whole folder (except `_build/`) to any web host.

## Edit text
All text lives in two files:
- `_build/content_main.py`: contacts, menus, services, packages, home page, enquiry form, about, privacy, terms
- `_build/content_dest.py`: the 13 destination pages

Each text has an English and an Indonesian version: `L("English", "Indonesia")`.

After editing, regenerate every page:

```
python _build/build.py
```

## Add your own photos
Photos are picked up automatically by file name. Use landscape photos at least 2000px wide.

| Where | Put the file at |
|---|---|
| Destination card + page header | `assets/img/destinations/<slug>.jpg` (e.g. `padar-island.jpg`) |
| Package card + page header | `assets/img/packages/<slug>.jpg` (e.g. `sharing-trip.jpg`) |
| Service card + page header | `assets/img/services/<slug>.jpg` (e.g. `stays.jpg`) |
| Home page hero | replace `assets/img/padar-island.jpg` |
| Home page dragon | replace `assets/img/komodo-dragon.jpg` |

Slugs are listed in the content files (`"slug": ...`). Run `python _build/build.py` after adding photos.

## Preview locally
```
python -m http.server 8765
```
Then open http://localhost:8765

## Current photos
All photos are free Unsplash photos (Unsplash License: free for commercial use, no credit required).
The list of files, photographers and sources is in `assets/img/CREDITS.md`, generated from `_build/photos.tsv`.
To swap a photo for your own, replace the file with the same name and run `python _build/build.py`.
Your two original photos are kept in `assets/img/original/`.
