# Personal site redesign — "Ice & Ink"

Date: 2026-08-31
Site: https://Sk-2103.github.io (repo `Sk-2103/Sk-2103.github.io`)

## Goal

Modernize the existing Academic Pages (Minimal Mistakes fork) Jekyll site in
place — new visual system, fixed placeholder content, and a few content
corrections — while keeping the data-driven collection structure
(`_publications`, `_talks`, `_teaching`, `_portfolio`, `_datasets`, `_tools`)
so future updates stay a matter of dropping in a markdown file.

## Background

The repo also contains `alfolio-site/`, a static (non-Jekyll) HTML prototype
styled after the [al-folio](https://github.com/alshedivat/al-folio) academic
theme, built in an earlier session but never linked from the live site. It is
not the basis for the live site going forward (its content duplicates and
will drift from the real Jekyll collections), but its bio copy is more
current than the live `about.md` and its type pairing (Roboto Slab +
JetBrains Mono) is being reused for continuity. It will be removed from the
repo once its useful content has been folded in — it remains recoverable via
git history.

The theme already has full light/dark theming via CSS custom properties
(`_sass/theme/_default.scss`, `_sass/theme/_dark.scss`) toggled at runtime
through a `data-theme="dark"` attribute set by existing JS in
`assets/js/_main.js`, with a toggle button already wired in
`_includes/masthead.html`. No new dark-mode infrastructure is needed — only
new color values.

## Visual system

### Color — light (`_sass/theme/_default.scss`, `:root`)

| Variable | Value | Purpose |
|---|---|---|
| `--global-bg-color` | `#FAFAF8` | page background (warm paper) |
| `--global-text-color` | `#1A1D23` | body/ink text |
| `--global-text-color-light` | `#5B6470` | secondary/muted text |
| `--global-base-color` | `#5B6470` | base/muted UI text |
| `--global-border-color` | `#E4E1D9` | hairlines, card borders |
| `--global-link-color` | `#1477A6` | glacier-blue accent, links |
| `--global-link-color-hover` | `#0F5C82` | link hover |
| `--global-link-color-visited` | `#3D93BE` | visited links |
| `--global-masthead-link-color` | `#1A1D23` | nav link default |
| `--global-masthead-link-color-hover` | `#1477A6` | nav link hover |
| `--global-code-background-color` | `#F3F6F8` | code/inline chip background |
| `--global-code-text-color` | `#33414A` | code text |
| `--global-fig-caption-color` | `#6B7280` | figure captions |
| `--global-thead-color` | `#EDEBE3` | table header background |

### Color — dark (`_sass/theme/_dark.scss`, `html[data-theme="dark"]`)

| Variable | Value | Purpose |
|---|---|---|
| `--global-bg-color` | `#12161B` | page background (deep ink) |
| `--global-text-color` | `#EDEFF2` | body text |
| `--global-text-color-light` | `#9BA4AF` | secondary/muted text |
| `--global-base-color` | `#9BA4AF` | base/muted UI text |
| `--global-border-color` | `#2A313B` | hairlines, card borders |
| `--global-link-color` | `#4FB8E0` | glacier-blue accent (brightened for contrast) |
| `--global-link-color-hover` | `#7ACBE8` | link hover |
| `--global-link-color-visited` | `#3A9CC0` | visited links |
| `--global-masthead-link-color` | `#EDEFF2` | nav link default |
| `--global-masthead-link-color-hover` | `#4FB8E0` | nav link hover |
| `--global-code-background-color` | `#1B2129` | code/inline chip background |
| `--global-code-text-color` | `#C7CDD4` | code text |
| `--global-fig-caption-color` | `#8891A0` | figure captions |
| `--global-thead-color` | `#1B2129` | table header background |

### Typography (`_sass/_themes.scss`)

- Headings (`$header-font-family`): "Roboto Slab", Georgia, serif
- Body (`$global-font-family`): "Inter", -apple-system, "Segoe UI", sans-serif
- Accent/mono (dates, venue badges — new class, not a global override):
  "JetBrains Mono", Monaco, monospace
- Fonts loaded via Google Fonts `<link>` in `_includes/head/custom.html`

### Components

- **Masthead/nav**: sticky top bar, background `--global-bg-color` with a
  1px bottom border in `--global-border-color`; nav links get an
  accent-color underline/hover; theme-toggle icon unchanged in behavior.
- **Author profile card** (`_includes/author-profile.html` + its SCSS):
  avatar gets a subtle ring/shadow; social/contact links restyled as a
  compact icon row using the accent color on hover; card background uses
  `--global-code-background-color` with `$border-radius` and a soft
  `$box-shadow`.
- **Archive/collection list items** (`_includes/archive-single*.html` and
  related SCSS) — used for publications, talks, teaching, portfolio: styled
  as cards with a small monospace year/venue badge tinted with the accent
  color at low opacity.
- **Buttons** (`_sass/layout/_buttons.scss`): rounded corners, accent-color
  primary style.
- **Footer**: unchanged structurally, muted text color.

No layout template restructuring (sidebar + content stays) — this is a
visual/CSS pass over the existing Minimal Mistakes structure, not a rebuild.

## Content changes

1. **`_config.yml`**
   - `description`: replace placeholder `"personal description"` with a real
     one-line description (e.g. "Postdoctoral researcher in geospatial data
     science — Earth observation, foundation models, and deep learning for
     glaciers, floods, and water resources.")
   - `author.pubmed`: clear the template's leftover example URL
     (`...term=john+snow`) — no real PubMed profile exists, so the field
     (and its sidebar entry) is simply removed rather than replaced.

2. **`_pages/about.md`**
   - Fold in bio content currently only in `alfolio-site/index.html`: the
     Tellman Lab / Schneider Lab affiliation detail, Hugging Face profile
     link, and teaching course mentions ("AI for Sustainability", "AI for
     Earth Observation").
   - Keep the existing Academic Achievements and News sections as-is —
     confirmed nothing newer than the Feb 2026 entry needs adding.

3. **`_publications/2025-07-01-publication.md`** ("Beyond Clouds")
   - Change status from `Under-Review` to `Published`.
   - Add the ESSD link: `https://doi.org/10.5194/essd-2026-474`.
   - Update the citation string to reflect ESSD publication (journal name,
     year, DOI), keeping all four co-authors (Kaushik, Tellman, Howat, and
     confirming Haritashya per the ESSD listing).
   - Keep the existing title ("Beyond Clouds: ...") and all four existing
     figures (`DOFA.png`, `GLB.png`, `GLB_random.png`, `challenge1.png`)
     unchanged.

4. **Repo cleanup**
   - Remove `alfolio-site/` (git `rm -r`) once (2) has absorbed its useful
     content — it stays recoverable via git history, just no longer shipped
     or discoverable as a stale duplicate.

## Testing

- Confirm Ruby/Jekyll/Bundler availability in the working environment before
  relying on `jekyll serve` for local verification; note if unavailable and
  fall back to careful manual review of generated SCSS/HTML.
- `bundle exec jekyll serve -l -H localhost`, then visually check:
  - Homepage/about (profile card, achievements, news) in both light and dark
  - A publication page (including the updated "Beyond Clouds" entry)
  - A talks/teaching archive listing (card styling)
  - Mobile-width nav collapse
  - Dark-mode toggle round-trips correctly (persists via localStorage)
- Confirm no Jekyll build errors/warnings introduced by the SCSS/content
  changes.

## Out of scope

- No layout/template restructuring beyond component-level restyling.
- No changes to `_datasets`/`_tools` collection content beyond inherited
  visual restyling.
- No new pages, no CMS/build-tooling changes, no hosting/workflow changes.
- Nothing is pushed to GitHub as part of this work without separate,
  explicit confirmation.
