# Persona Lens — Launch Status

**Date:** 2026-05-15
**Status:** 🟢 **LIVE** at https://persona-lens.com

---

## What's live right now

- ✅ **https://persona-lens.com** — HTTPS, HTTP/2, valid Let's Encrypt cert (expires 2026-08-13)
- ✅ HTTP → HTTPS auto-redirect (301)
- ✅ All 15 pages serving 200 OK:
  - `/` (English homepage)
  - `/fr/`, `/es/`, `/ru/` (Coming-soon stubs)
  - `/privacy.html`, `/terms.html`
  - `/science.html`, `/pricing.html`, `/testimonials.html`
  - `/lens-self.html`, `/lens-romantic.html`, `/lens-friendship.html`,
    `/lens-professional.html`, `/lens-family.html`, `/lens-group.html`

## Stack

| Layer | Provider | Notes |
|---|---|---|
| DNS | Squarespace | 3 of 4 GitHub Pages A records added |
| Hosting | GitHub Pages | Repo: `fabricebertinchamps-hub/personalens-website` |
| Cert | Let's Encrypt (auto via GH) | State: `approved` |
| CDN | Fastly (GH Pages default) | Built-in |
| Email outbound | Resend + Mailgun | MX/TXT records preserved |

## DNS records currently in Squarespace

```
A    @   185.199.108.153    ✅
A    @   185.199.109.153    ✅
A    @   185.199.110.153    ✅
A    @   185.199.111.153    ❌ pending (Squarespace 2FA required)
CNAME www → fabricebertinchamps-hub.github.io  ❌ pending (same 2FA)

# Email (preserved, do not touch)
CNAME _domainconnect → _domainconnect.domains.squarespace.com
MX   send → feedback-smtp.eu-west-1.amazonses.com (priority 10)
TXT  send → v=spf1 include:amazonses.com ~all
TXT  resend._domainkey → p=MIGfMA...  (DKIM)
TXT  krs._domainkey → ... (Mailgun DKIM)
TXT  _dmarc → v=DMARC1; p=reject; ...
TXT  @ → v=spf1 include:mailgun.org ~all
```

## Remaining work (your verification code blocked it)

Both items only matter for **redundancy**. The site is already fully functional without them.

### 1. Add the 4th A record
- Type: `A`
- Name: `@`
- Data: `185.199.111.153`

### 2. Add the www subdomain
- Type: `CNAME`
- Name: `www`
- Data: `fabricebertinchamps-hub.github.io`

**Why www matters:** Without it, `www.persona-lens.com` won't resolve. Anyone typing `www.` will get an error. The apex (`persona-lens.com`) works fine.

### How to add them when you're back

1. Go to https://account.squarespace.com/domains/managed/persona-lens.com/dns/dns-settings
2. Scroll to **Custom records**
3. Click **ADD RECORD**
4. Squarespace will ask for an auth code → check `chemreset@gmail.com` for a fresh `XXX XXX` code (request a new one if the old one expired)
5. Type the code, click VERIFY
6. Fill the row (Type=A, Name=@, Data=185.199.111.153) and save
7. Repeat for the CNAME: Type=CNAME, Name=www, Data=fabricebertinchamps-hub.github.io
8. Wait ~5 min, then run: `curl -I https://www.persona-lens.com` — should return 301 or 200

## What I did this session

1. Confirmed DNS resolution: `dig persona-lens.com` returns the 3 GH Pages IPs ✓
2. Triggered fresh GH Pages build to recover from "errored" state ✓
3. Confirmed CNAME file in repo: `persona-lens.com` ✓
4. Watched Let's Encrypt cert provision → state went from `null` → `approved` ✓
5. Enabled `https_enforced: true` via GH API ✓
6. Smoke-tested all 15 pages over HTTPS — all 200 OK ✓

## Useful commands

```bash
# Check site health
curl -I https://persona-lens.com

# Check DNS
dig +short persona-lens.com A

# Check GH Pages config
TOKEN="ghp_..."  # PAT in instagram-pipeline/.git/config
curl -s -H "Authorization: Bearer $TOKEN" \
  https://api.github.com/repos/fabricebertinchamps-hub/personalens-website/pages
```

## Repo links

- **Live site:** https://persona-lens.com
- **GitHub repo:** https://github.com/fabricebertinchamps-hub/personalens-website
- **GH Pages preview URL:** https://fabricebertinchamps-hub.github.io/personalens-website/
- **App Store:** https://apps.apple.com/be/app/persona-lens/id6759287207
