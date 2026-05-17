#!/usr/bin/env python3
"""
Generate SEO landing pages from a structured spec.
Outputs to /guides/<slug>.html with full schema markup + brand chrome.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
GUIDES_DIR = ROOT / "guides"
GUIDES_DIR.mkdir(exist_ok=True)

HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{description}" />
<meta name="keywords" content="{keywords}" />
<link rel="canonical" href="https://persona-lens.com/guides/{slug}.html" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{description}" />
<meta property="og:image" content="https://persona-lens.com/assets/appicon.png" />
<meta property="og:url" content="https://persona-lens.com/guides/{slug}.html" />
<meta property="og:type" content="article" />
<meta property="og:site_name" content="Persona Lens" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{description}" />
<meta name="twitter:image" content="https://persona-lens.com/assets/appicon.png" />
<meta name="theme-color" content="#25375B" />
<link rel="icon" type="image/x-icon" href="/assets/favicon.ico?v=20260515" />
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png?v=20260515" />
<link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png?v=20260515" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/style.css" />
<script src="/menu.js" defer></script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{title_clean}",
  "description": "{description}",
  "image": "https://persona-lens.com/assets/appicon.png",
  "author": {{ "@type": "Organization", "name": "Persona Lens", "url": "https://persona-lens.com/" }},
  "publisher": {{ "@type": "Organization", "name": "Persona Lens", "url": "https://persona-lens.com/", "logo": {{ "@type": "ImageObject", "url": "https://persona-lens.com/assets/appicon.png" }} }},
  "datePublished": "2026-05-17",
  "dateModified": "2026-05-17",
  "mainEntityOfPage": "https://persona-lens.com/guides/{slug}.html",
  "inLanguage": "en"
}}
</script>
{faq_schema}
</head>
<body>

<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="/"><img src="/assets/appicon.png" alt="Persona Lens" class="brand-mark"/><span class="brand-name">Persona Lens</span></a>
    <nav class="site-nav"><a href="/#lenses">The Lenses</a><a href="/#how">How It Works</a><a href="/science.html">Science</a><a href="/testimonials.html">Testimonials</a><a href="/pricing.html">Pricing</a></nav>
    <div class="lang-picker"><span class="lang-flag flag-en active" aria-label="English"></span><a class="lang-flag flag-fr" href="/fr/" aria-label="Français"></a><a class="lang-flag flag-es" href="/es/" aria-label="Español"></a><a class="lang-flag flag-ru" href="/ru/" aria-label="Русский"></a></div><a class="btn btn-primary header-cta" href="https://apps.apple.com/be/app/persona-lens/id6759287207" target="_blank" rel="noopener">Get the App</a>
  <button class="nav-toggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button></div>
</header>

<nav class="mobile-nav" aria-label="Mobile navigation">
  <a href="/#lenses">The Lenses</a>
  <a href="/#how">How It Works</a>
  <a href="/science.html">Science</a>
  <a href="/testimonials.html">Testimonials</a>
  <a href="/pricing.html">Pricing</a>
  <a class="mobile-cta" href="https://apps.apple.com/be/app/persona-lens/id6759287207" target="_blank" rel="noopener">Get the App</a>
</nav>

<main class="legal-page">
  <div class="container">
    <p class="legal-meta"><a href="/" style="color: var(--text-3);">← Persona Lens</a> &nbsp;·&nbsp; Guide &nbsp;·&nbsp; Updated May 2026</p>
    <h1>{h1}</h1>
    <p style="font-size: 19px; line-height: 1.6; color: var(--text-2); margin-bottom: 30px;">{intro}</p>
"""

CTA = """
    <div style="background: var(--cream-warm); border: 1px solid var(--border); border-radius: var(--radius); padding: 28px 26px; margin: 36px 0;">
      <p class="eyebrow" style="margin-bottom: 8px;">Read your own situation</p>
      <h3 style="font-family: 'TeX Gyre Bonum', Georgia, serif; font-weight: 700; font-size: 22px; color: var(--navy); margin: 0 0 10px;">{cta_title}</h3>
      <p style="margin: 0 0 18px; color: var(--text-2); line-height: 1.55;">{cta_body}</p>
      <a class="btn btn-primary" href="https://apps.apple.com/be/app/persona-lens/id6759287207" target="_blank" rel="noopener">Try Persona Lens free →</a>
    </div>
"""

FAQ_OPEN = """
    <h2>Frequently asked questions</h2>
"""

FAQ_ITEM = """
    <div style="margin-bottom: 22px;">
      <h3 style="font-family: 'TeX Gyre Bonum', Georgia, serif; font-weight: 700; font-size: 19px; color: var(--navy); margin: 0 0 8px;">{q}</h3>
      <p style="margin: 0; color: var(--text-2); line-height: 1.6;">{a}</p>
    </div>
"""

FOOTER = """

    <div style="margin-top: 50px; padding-top: 24px; border-top: 1px solid var(--border); color: var(--text-3); font-size: 14px;">
      <p><strong>About this guide.</strong> Written by the Persona Lens team. We build software that does the same kind of reading at scale — Persona Lens is an iOS app that takes a real conversation and returns a structured psychological reading across six relationship lenses. Every reading takes about three minutes. The first one is free.</p>
      <p>This guide is informational, not clinical. If you are in distress or your relationship feels unsafe, please reach out to a qualified professional.</p>
    </div>

    <div style="margin-top: 40px;">
      <h3 style="font-family: 'TeX Gyre Bonum', Georgia, serif; font-weight: 700; font-size: 18px; color: var(--navy); margin: 0 0 14px;">More guides</h3>
      <ul style="list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: 1fr; gap: 8px;">
        <li><a href="/guides/emotionally-unavailable-partner.html">How to tell if your partner is emotionally unavailable →</a></li>
        <li><a href="/guides/emotionally-immature-parent.html">7 signs your parent is emotionally immature →</a></li>
        <li><a href="/guides/one-sided-friendship.html">Is this friendship one-sided? A diagnostic guide →</a></li>
        <li><a href="/guides/read-your-boss.html">How to read your boss from their messages →</a></li>
        <li><a href="/guides/group-chat-dynamics.html">What your group chat reveals about you →</a></li>
        <li><a href="/guides/big-five-from-real-behavior.html">The Big Five test that uses real behaviour →</a></li>
        <li><a href="/guides/attachment-style-from-texts.html">Attachment style from your texts →</a></li>
        <li><a href="/guides/should-you-break-up.html">Should you break up? The 5 patterns →</a></li>
      </ul>
    </div>

  </div>
</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-inner">
      <div class="footer-col footer-brand-col"><div class="footer-brand"><img src="/assets/appicon.png" alt="" class="footer-mark"/><p class="footer-name">Persona Lens</p></div><p class="footer-tag">Understand any relationship in three minutes.</p></div>
      <div class="footer-col"><h4>The Lenses</h4><ul><li><a href="/lens-self.html">Self</a></li><li><a href="/lens-romantic.html">Romantic</a></li><li><a href="/lens-friendship.html">Friendship</a></li><li><a href="/lens-professional.html">Professional</a></li><li><a href="/lens-family.html">Family</a></li><li><a href="/lens-group.html">Group</a></li></ul></div>
      <div class="footer-col"><h4>Product</h4><ul><li><a href="/#how">How it works</a></li><li><a href="/pricing.html">Pricing</a></li><li><a href="/science.html">The science</a></li><li><a href="/testimonials.html">Testimonials</a></li><li><a href="/press.html">Press &amp; About</a></li></ul></div>
      <div class="footer-col"><h4>Legal</h4><ul><li><a href="/privacy.html">Privacy policy</a></li><li><a href="/terms.html">Terms of use</a></li></ul></div>
    </div>
    <div class="container footer-bottom"><span>© 2026 Persona Lens. Made with care, made to help.</span><span>AI insights, not diagnosis.</span></div>
  </div>
</footer>

</body>
</html>
"""


def render_section(section):
    """A section is {h2, paragraphs (list), optional list (bullets)}."""
    out = [f'\n    <h2>{section["h2"]}</h2>\n']
    for p in section.get("paragraphs", []):
        out.append(f'    <p>{p}</p>\n')
    if section.get("list"):
        out.append('    <ul>\n')
        for item in section["list"]:
            out.append(f'      <li>{item}</li>\n')
        out.append('    </ul>\n')
    if section.get("subsections"):
        for sub in section["subsections"]:
            out.append(f'\n    <h3>{sub["h3"]}</h3>\n')
            for p in sub.get("paragraphs", []):
                out.append(f'    <p>{p}</p>\n')
            if sub.get("list"):
                out.append('    <ul>\n')
                for item in sub["list"]:
                    out.append(f'      <li>{item}</li>\n')
                out.append('    </ul>\n')
    return "".join(out)


def build_faq_schema(faqs):
    """Generate FAQPage JSON-LD schema."""
    if not faqs:
        return ""
    items = []
    for f in faqs:
        items.append({
            "@type": "Question",
            "name": f["q"],
            "acceptedAnswer": {"@type": "Answer", "text": f["a"]}
        })
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": items
    }
    return f'<script type="application/ld+json">\n{json.dumps(schema, ensure_ascii=False, indent=2)}\n</script>'


def build_page(spec):
    title_clean = spec["title"].replace('"', '\\"')
    faq_schema = build_faq_schema(spec.get("faqs", []))
    html = HEADER.format(
        title=spec["title"],
        title_clean=title_clean,
        description=spec["description"],
        keywords=spec["keywords"],
        slug=spec["slug"],
        h1=spec["h1"],
        intro=spec["intro"],
        faq_schema=faq_schema,
    )
    # Sections (split CTA after section 3)
    sections = spec["sections"]
    for i, sec in enumerate(sections):
        html += render_section(sec)
        if i == 2 and spec.get("cta"):
            html += CTA.format(**spec["cta"])
    # Final CTA before FAQ
    if spec.get("cta"):
        html += CTA.format(**spec["cta"])
    # FAQ
    if spec.get("faqs"):
        html += FAQ_OPEN
        for f in spec["faqs"]:
            html += FAQ_ITEM.format(**f)
    html += FOOTER
    out_path = GUIDES_DIR / f"{spec['slug']}.html"
    out_path.write_text(html, encoding="utf-8")
    return out_path


if __name__ == "__main__":
    import sys
    spec_file = sys.argv[1] if len(sys.argv) > 1 else "guide_specs.json"
    specs = json.load(open(spec_file, encoding="utf-8"))
    for spec in specs:
        p = build_page(spec)
        print(f"  ✓ {p.name}  ({p.stat().st_size:,} bytes)")
    print(f"\nGenerated {len(specs)} guide pages.")
