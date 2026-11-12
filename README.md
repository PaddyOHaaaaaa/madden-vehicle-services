# Madden Vehicle Services website

Static website for https://maddenvehicleservices.co.uk, hosted on Cloudflare Pages.

## Folder layout

- `public/` – the live website (this is the only folder Cloudflare publishes)
  - `index.html`, `about.html`, `contact.html`, `cookie-policy.html`, `gdpr-policy.html`, `404.html`
  - `styles.css`, `script.js`, `images/`
  - `sitemap.xml`, `robots.txt`, `_headers` (Cloudflare security/caching headers)
- `.claude/` – local preview tools (not published)

## Cloudflare Pages settings

| Setting | Value |
| --- | --- |
| Production branch | `main` |
| Framework preset | None |
| Build command | *(leave empty)* |
| Build output directory | `public` |

## Making changes

1. Edit files in `public/`.
2. Commit and push to the `main` branch on GitHub.
3. Cloudflare rebuilds and publishes the site automatically within a minute or two.

Pushing to any other branch creates a private preview link in Cloudflare instead of changing the live site.

## Preview locally

```bash
python .claude/serve.py 8080
```

Then open http://localhost:8080.
