# FreeSliders (Placeholder Static Site)

A minimal, owner‑agnostic static placeholder intended for:

- GitHub Pages hosting
- Anonymous double‑blind review via https://anonymous.4open.science
- Being an easily replaceable landing page while the real site/app is in development

Current live entry point: `index.html` at the repository root.

---

## Contents

```
.
├── .nojekyll        # Disables Jekyll so files are served as-is
├── index.html       # Minimal “Hello World” placeholder page
└── README.md        # This file
```

No build step. No dependencies. No external assets. 100% static.

---

## Quick Start

1. Clone or fork this repository.
2. Edit `index.html` with your real content (keep relative links for portability).
3. Commit & push.

---

## Deploy on GitHub Pages

1. Open the repository in GitHub.
2. Go to: Settings → Pages.
3. Build and deployment:
   - Source: Deploy from a branch
   - Branch: `main` (or `master`) / root
4. Save and wait ~30–90 seconds.
5. Visit: `https://<username>.github.io/<repository-name>/`

Tip: If this is a user/organization site (named `<username>.github.io`), the URL will be just `https://<username>.github.io/`.

---

## Anonymous 4open Mirror (Double‑Blind Review)

1. Ensure no identifying text exists in:
   - `index.html` (author names, affiliations)
   - Commit messages (avoid personal signatures)
2. Go to: https://anonymous.4open.science/
3. Provide the repository URL (public).
4. Use the generated anonymized link in submissions.

Why it works:
- Relative paths only
- No analytics / external fonts / CDNs
- `.nojekyll` prevents accidental Liquid/Jekyll metadata injection

---

## Customizing

| Task | What to Do |
|------|------------|
| Add a second page | Create `about.html`; link via `<a href="about.html">About</a>` |
| Add basic styling | Add an inline `<style>` block or create `style.css` and reference it |
| Add images | Create `assets/` (e.g. `assets/logo.png`) and reference with `<img src="assets/logo.png" alt="Logo">` |
| Favicon | Put `favicon.ico` in root; add `<link rel="icon" href="favicon.ico">` in `<head>` |
| JavaScript | Add `main.js`; include `<script src="main.js" defer></script>` |
| Prevent indexing (temporary) | Keep `<meta name="robots" content="noindex,nofollow">` |
| Allow indexing later | Remove that `<meta>` line |

---

## Minimal Example Extension

Add a navigation block:

```html
<nav>
  <a href="index.html">Home</a> |
  <a href="about.html">About</a>
</nav>
```

---

## Recommended Commit Hygiene (for anonymity)

- Use neutral commit messages: `Update content`, `Add about page`, `Refactor layout`
- Avoid names/emails in page text during review
- Remove `noindex` meta after publication

---

## Common Pitfalls

| Pitfall | Avoid |
|---------|-------|
| Absolute URLs | `https://username.github.io/repo/style.css` (breaks anonymization) |
| External fonts | e.g. Google Fonts (can add tracking or leak review identity) |
| Analytics scripts | Google Analytics, Plausible, etc. |
| Large frameworks | Overkill for a single placeholder page |
| Missing `.nojekyll` | Can cause underscore-prefixed assets to be skipped |

---

## Roadmap (Optional Ideas)

- Add a minimal CSS theme
- Include a changelog section
- Add automated deployment badge
- Provide a zip export script

If you want any of these added, just describe what you need.

---

## License

Choose a license appropriate for your intended use (MIT, Apache-2.0, CC0, etc.).  
Placeholder suggestion (edit as needed):

```
MIT License (proposed)
Copyright (c) YEAR AUTHOR
Permission is hereby granted...
```

(Add the full license text in a `LICENSE` file.)

---

## FAQ

**Q: Why is there a `.nojekyll` file?**  
A: To disable Jekyll so that GitHub Pages serves files verbatim (important for underscored paths and pure static intent).

**Q: Can I add Markdown pages?**  
A: Yes, but without a generator they’ll just render raw text in browsers. Convert them to HTML manually or with a static site generator if needed later.

**Q: How do I make relative links work everywhere?**  
A: Always omit domain and repo: use `about.html`, `./about.html`, or `assets/image.png`.

---

## Contributing

Since this is a placeholder scaffold, contributions usually mean:
- Tightening minimal HTML
- Improving deployment notes
- Adding optional templates behind separate files

Open an issue or PR with a clear description.

---

Happy deploying.