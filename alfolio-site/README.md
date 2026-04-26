# al-folio styled site for Saurabh Kaushik

A clean, static-HTML site styled after [al-folio](https://github.com/alshedivat/al-folio),
populated with your actual research content. **Designed to live alongside your existing
AcademicPages site without overwriting any of it.**

## What's inside

```
alfolio-site/
├── index.html          # about page (the al-folio "home")
├── news.html           # full news / highlights
├── publications.html   # publications grouped by year
├── projects.html       # projects grid
├── cv.html             # CV summary
├── assets/
│   ├── css/main.css    # all styling (light + dark themes)
│   └── js/main.js      # theme toggle + mobile menu
└── README.md           # this file
```

No build step. No Jekyll, no Ruby, no bundler. Just open `index.html` in a browser.

## Features that match al-folio

- Fixed top navbar with brand on the left, page links on the right
- Roboto Slab serif typography
- Profile section with circular photo + bio + contact icons
- Highlighted news table
- Publications styled with year headings, venue badges, and link buttons
- Projects grid with hover lift
- **Built-in light / dark mode** toggle (saved to localStorage)
- Fully responsive (mobile menu collapses)

## How to deploy WITHOUT destroying your original site

You have three good options. Pick whichever fits your workflow.

### Option A — Subfolder under your existing repo (simplest, recommended)

Your current site lives at `https://sk-2103.github.io/`. You can drop this entire
`alfolio-site/` folder into your repo and it will be served at
`https://sk-2103.github.io/alfolio-site/` without touching any existing file.

```bash
# from inside your local clone of Sk-2103.github.io
cp -r path/to/alfolio-site ./alfolio-site
git add alfolio-site
git commit -m "Add al-folio styled mirror site"
git push
```

Then visit: **https://sk-2103.github.io/alfolio-site/**

You can rename the folder (e.g. to `v2/` or `new/`) if you want a shorter URL.
Your current Jekyll site continues to build and serve normally — Jekyll just treats
this folder as static assets and copies them through.

If Jekyll ever ignores it, add this line to your `_config.yml`:

```yaml
include: ["alfolio-site"]
```

### Option B — Separate branch on the same repo

Keep your `master` branch as-is. Push the new site to a different branch and
serve it from a subdomain or a separate Pages site:

```bash
git checkout --orphan alfolio
git rm -rf .
cp -r path/to/alfolio-site/* .
git add .
git commit -m "al-folio styled site"
git push origin alfolio
```

Then in **GitHub → Settings → Pages**, you can choose to serve from this branch
(but only one branch can be the active Pages source for a given repo at a time —
if you want both live simultaneously, use Option A or C).

### Option C — Brand-new repository (totally isolated)

Create a new repo, e.g. `Sk-2103/alfolio-site`, push these files to its `main`
branch, and enable GitHub Pages. It will be served at
`https://sk-2103.github.io/alfolio-site/` (project pages URL).

```bash
cd path/to/alfolio-site
git init
git add .
git commit -m "Initial al-folio site"
git remote add origin git@github.com:Sk-2103/alfolio-site.git
git branch -M main
git push -u origin main
```

Your existing `Sk-2103.github.io` repo is **completely untouched**.

## Linking the two sites (optional)

If you'd like a small "switch theme" link on each site, add these snippets:

**On the original site** (e.g. in `_includes/masthead.html`):

```html
<a href="https://sk-2103.github.io/alfolio-site/">Try the al-folio version →</a>
```

**On the new site** (e.g. in the navbar of every `*.html`, just before the theme toggle):

```html
<li><a href="https://sk-2103.github.io/">classic site →</a></li>
```

## Customising

- **Profile photo** — currently pulled from your live AcademicPages site at
  `https://Sk-2103.github.io/images/profile.jpg`. To bundle your own, drop a
  file at `assets/img/prof_pic.jpg` and update the `<img src>` in `index.html`.
- **Theme color** — edit `--global-theme-color` in `assets/css/main.css`
  (currently `#b509ac`, al-folio's signature purple).
- **Fonts** — change the `@import` URL in each HTML `<head>` (currently
  Roboto Slab + JetBrains Mono).
- **Adding content** — every page is a single, hand-written HTML file with
  inline content. No templates or front matter. Just open and edit.

## Local preview

```bash
cd alfolio-site
python3 -m http.server 8000
# open http://localhost:8000
```

That's it. The original Jekyll site stays exactly as it is.
