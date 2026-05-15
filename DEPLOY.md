# Persona Lens — Website Deployment Guide

This is the marketing site for **persona-lens.com**. It is a fully static site (no backend, no build step) so it can be deployed in about 5 minutes on any modern static host. The recommendation below is **Cloudflare Pages** — it is free, fast, supports your custom domain with one click, and gives you HTTPS automatically.

---

## What's in this folder

```
Website/
├── index.html              Landing page (Hero, six lenses, How It Works, Sample, Testimonials, Privacy, Pricing, Footer)
├── lens-self.html          Self Lens — detail page
├── lens-romantic.html      Romantic Lens — detail page
├── lens-friendship.html    Friendship Lens — detail page
├── lens-professional.html  Professional Lens — detail page
├── lens-family.html        Family Lens — detail page
├── lens-group.html         Group Lens — detail page (with the full Awards Ceremony showcase)
├── testimonials.html       Six lens groups × 3-6 reactions each
├── pricing.html            Full pricing — credit table, Pro vs Credits comparison, FAQ
├── privacy.html            Privacy policy
├── terms.html              Terms of use
├── style.css               Brand stylesheet — all colours from iOS Theme.swift
├── assets/                 14 PNG brand assets (6 lens icons, 5 source-app icons, app logo, app icon, paper background)
├── fonts/                  TeX Gyre Bonum Bold .otf (self-hosted display font, LPPL licensed)
└── DEPLOY.md               This file
```

Everything in `Website/` is what you upload. The whole site is ~9 MB (icons are unoptimised PNGs — see "Optional next steps").

## Brand fidelity — sourced from iOS

Every visual token in this site is matched to the **iOS app's `Theme.swift`** — the single source of truth.

- Navy `#25375B` for headings and primary CTA
- Cream `#F8F6F3` page surface, `#F2EEE8` secondary
- Charcoal-brown text `#2B2622`
- Lens colours tuned to the revised iOS icons:
  - Self `#6BA7B3` · Romantic `#D78377` · Friendship `#FBB35F`
  - Professional `#A783D7` · Family `#83B3E3` · Group `#FB775F`
- **TeX Gyre Bonum Bold** for display type (the same custom font shipped inside the iOS app), self-hosted from `/fonts/`
- **Inter** for body, from Google Fonts
- Lens icons copied directly from `PersonaLens/Assets.xcassets/` — not from older marketing rendering

## Recommended host: Cloudflare Pages

Cloudflare Pages gives you €0/month, unlimited bandwidth, HTTPS auto-issued, custom domain support, and a global CDN. No build step needed.

### Step 1 — Create the project

1. Go to <https://dash.cloudflare.com> and sign up (free, no card required).
2. From the sidebar choose **Workers & Pages** → **Pages** → **Upload assets**.
3. Project name: `persona-lens`.
4. Drag the entire **contents** of the `Website/` folder onto the upload box. (Not the folder itself — its contents: `index.html`, all the `.html` files, `style.css`, and the `assets/` and `fonts/` subfolders.)
5. Click **Deploy site**. After ~30 seconds it goes live at `https://persona-lens.pages.dev`.

### Step 2 — Point persona-lens.com to it

1. In the Pages project, open **Custom domains** → **Set up a custom domain**.
2. Enter `persona-lens.com`. Cloudflare will display the DNS records to add.
3. Open a new tab and go to **Squarespace Domains** (where persona-lens.com is registered).
4. Find persona-lens.com → **DNS settings** → **Custom Records**.
5. Add the records Cloudflare gave you (typically one `CNAME` on `@` and one on `www`, both pointing to `persona-lens.pages.dev`).
6. Save. DNS usually propagates in 2–10 minutes.
7. Back in Cloudflare Pages, the custom domain status will flip to **Active** once DNS is live; an HTTPS certificate is auto-provisioned (another 5–10 minutes).

> **Heads up — keep email forwarding working.** persona-lens.com currently forwards `fabrice@persona-lens.com` → `chemreset@gmail.com` via Squarespace. **Do not delete the existing MX records** when adding the CNAME — they are independent. If Cloudflare suggests switching nameservers, you must re-create the MX records inside Cloudflare or the email forwarding will silently break.

### Step 3 — Updating the site later

1. Edit the file locally.
2. In Cloudflare Pages → your project → **Create new deployment** → **Upload assets**.
3. Drag the updated `Website/` contents again. New version live in ~30 seconds.

For a developer-style flow, you can connect the project to a GitHub repo (`personalens-website`, for example) and Cloudflare will redeploy on every `git push`. Not required for a static site.

---

## Alternative hosts (also free, custom domain on free tier)

| Host | Notes |
| --- | --- |
| **Cloudflare Pages** (recommended) | Best CDN, fastest, easiest custom domain |
| **Netlify** | Same drag-and-drop UX |
| **Vercel** | Same flow; geared for developers |
| **GitHub Pages** | Free; requires the site to live in a GitHub repo |

Pick one and stick with it.

---

## After deploy — quick QA

Open `https://persona-lens.com` and walk through:

1. The header app-icon loads (the navy "P" icon from the App Store).
2. Hero shows correctly side-by-side on desktop, stacks on mobile.
3. The six lens cards each have their colored top stripe and the correct iOS icon below the eyebrow.
4. Click each "Explore the X Lens →" — six per-lens pages load with the matching colour theme.
5. **Group Lens detail page** — scroll to the Awards Ceremony grid; eight tiles render with names and quotes.
6. Click **Testimonials** in the nav — six lens sections render with reactions per lens.
7. Click **Pricing** — credit table, comparison table, and FAQ all render.
8. Footer links resolve: Privacy, Terms, contact mailto, all six lens pages.

If anything looks off, the files to edit will almost always be `index.html` (content) or `style.css` (colours, spacing).

---

## Optional next steps (post-launch)

These are nice-to-haves; the site ships fine without them.

- **Optimise icons.** The lens PNGs are 1024×1024 originals from the iOS asset catalog. Running them through `pngquant` would cut the page weight from ~9 MB to under 1 MB. This is the single biggest performance win.
- **WebP variants.** Add `<picture>` blocks with WebP sources for older browsers if performance becomes a concern.
- **Open Graph image.** The current `og:image` points at the app icon. A dedicated 1200×630 OG card would render better on social shares.
- **Analytics.** Cloudflare Web Analytics is free and privacy-respecting — drop the snippet from your Pages project settings if you want pageview data.
- **Localised pages.** When the app's other-language launches mature, add `/fr/`, `/es/`, `/ru/` versions of `index.html` and the lens pages.
