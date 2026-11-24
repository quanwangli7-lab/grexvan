# PR #1 review remediation — 2026-11-24

Status: review only. No main merge, production deployment, paid service or analytics activation authorized.

## Product consistency

Owner manually confirmed Amazon ASIN B0HGZ3ZXWM displays GREXVAN / GV-KIT-001 and Mazda CX-5 2.0L 2013–2019 / 2.5L 2014–2025 naturally aspirated fitment. Amazon page independently retrieved for cross-check: https://www.amazon.com/dp/B0HGZ3ZXWM . Website fitment scope was not expanded. Cabin OE reference KD45-61-J6X series; engine PE07-13-3A0 / PE07-13-3A0A. These are comparison references, not OEM affiliation or VIN-specific certification. Manufacturer engineering validation and complete VIN-level compatibility evidence are unavailable. Package/listing dimensions were not treated as verified filter dimensions. Listing warranty field does not establish an additional GREXVAN manufacturer warranty; website text no longer implies an extension.

## Implemented

Home and kit detail Amazon outbound links use target=_blank and rel=noopener noreferrer, with purchase disclosure. Existing installation/support and original JPG assets retained. Wholesale explains actual two-filter kit, limited applications, OE references, documentation and email inquiry workflow. It does not represent a server-submitted form. Reference PDF is one page, visually checked, and explicitly not an engineering specification or test certificate. All 21 content pages have descriptions and production canonical URLs; sitemap lists those 21 URLs. Root 404 disables Pages SPA fallback. Preview host-specific noindex headers, MIME sniffing protection, frame restrictions and CSP added. Hosting behavior still requires fresh deployed-preview verification.

## Unresolved acceptance blockers

Actual authorized support reply test failed: Gmail delivery subsystem reports support@grexvan.com sending identity authorization no longer valid. API accepted the send request but a later bounce proves delivery failed. Incoming forwarding is not independently established by same-account inbox labels. Owner must restore sending authorization and repeat an external inbound + support outbound test. No passwords or verification codes should be supplied in chat.

Native browser screenshots and Safari/Firefox execution are not certified: browser automation failed to start in this environment. DOM render exports must be labeled as such and cannot substitute for native screenshots. Prior PageSpeed API calls returned HTTP 429; no Lighthouse scores are claimed. Browser and network evidence must be regenerated against the latest preview before final approval.

## Free analytics research

Cloudflare Web Analytics is free for basic traffic, but does not support custom events; it cannot satisfy Amazon button event tracking by itself. Sources: https://developers.cloudflare.com/web-analytics/about/ and https://developers.cloudflare.com/web-analytics/faq/ . GA4 standard enhanced measurement can record outbound clicks with link URL/domain; both buttons have stable product/placement data attributes for a later controlled integration. Source: https://support.google.com/analytics/answer/13566436?hl=en . No analytics account, script, cookie or new subscription was activated. Privacy/consent requirements and actual event receipt must be checked before enabling.

## Search Console research

After owner approval, use the free Domain property and an owner-provided DNS TXT verification record, then submit the production sitemap. No DNS records or verification tokens changed. Source: https://support.google.com/webmasters/answer/9008080 . Preview must remain noindex; production canonical URLs do not authorize preview indexing. Crawlers must be able to fetch pages to read noindex: https://developers.google.com/search/docs/crawling-indexing/block-indexing .

## Hosting / security evidence sources

Cloudflare header syntax: https://developers.cloudflare.com/pages/configuration/headers/ . Root 404 behavior: https://developers.cloudflare.com/pages/configuration/serving-pages/ . Preview isolation: https://developers.cloudflare.com/pages/configuration/preview-deployments/ . CSP permits only local scripts and the exact home JSON-LD hash; existing YouTube frames remain allowed. Inline CSS remains allowed to preserve existing pages. This is a configuration review, not a penetration-test certification.

## Release and rollback plan

Keep PR #1 draft until all blockers are resolved, preview headers/404 verified, owner independently approves. Record approved commit and existing production deployment ID before release. Only then merge the reviewed commit and deploy via existing Cloudflare pipeline. Verify critical routes, Amazon, mail, SEO and support. Roll back via Cloudflare to the previously recorded production deployment; if necessary revert the approved merge through a separate reviewed commit. Never rewrite main history. No production action has been taken for this remediation.
