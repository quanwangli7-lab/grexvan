# Sales channel upgrade — review only

Based on production commit `0f3a2c4b80f98e19f7866850394805ed6c40a27b`.

## Behavior

- GV-KIT-001 has a **Buy on Amazon** link to `https://www.amazon.com/dp/B0HGZ3ZXWM`, opened in a new tab with `noopener noreferrer`.
- The adjacent disclosure reads **Complete your purchase on Amazon.**
- Vehicle fitment and **Installation & Support** remain available. Existing installation pages, video URLs, OE references and real photos are unchanged.
- **Wholesale Inquiry** is accessible from the home page and kit page. The new page serves U.S. parts distributors, repair shops and retailers, with an email template sent to the existing `support@grexvan.com` inbox. The visitor must review and send the email in their email app; there is no simulated form submission or new backend.
- No prices, stock information, ratings, Prime badges or delivery promises are added. No new package, service, subscription or paid plugin is needed by the website.

## Analytics audit

The source and current live product page contain no GA/gtag, GTM/dataLayer, Plausible, Clarity or Cloudflare Web Analytics integration. Cloudflare email protection is not a click analytics service. Consequently no click tracking service or new analytics script has been installed, and no Amazon click totals are claimed. If an existing analytics account is connected later, the button can be instrumented against that account after its requirements are confirmed.

## Verification

Run `python3 tests/check_sales_upgrade.py` from this repository. This checks local links, the Amazon destination and tab attributes, wholesale email fields, and byte-for-byte preservation of support and photo files.

The separate review preview runs browser layout assertions in actual 1280px and 390px iframes. These cover overflow, loaded assets, button dimensions, focus, support anchors and inquiry details. This is responsive browser testing, not physical phone testing. No purchase or email was submitted, and Amazon checkout was not tested. Amazon's tab-opening attributes were checked; a manual outbound navigation remains available in the review preview.

## Deployment

This revision is local-only. Do not push or merge into `main` without explicit approval: `main` triggers Cloudflare Pages production deployment. No hosting configuration is changed. The patch or local branch can be reviewed before deployment is approved.
