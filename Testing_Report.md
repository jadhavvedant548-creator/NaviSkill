# Test report — V15
Base: V14 source, previously user-tested. Current tests executed with Node and Chromium/Playwright.

PASS: both HTML files parse JavaScript; seven navigation links; 30 quiz entries across three languages; unique tested feature IDs; no Gemini key reference in HTML; offline guide and scam logic; community translations, scoring, empty dashboard, paired scores and feedback averages. Mock API: method, authentication, origin, identifier, input, success, rate limit, upstream failure and missing key.

PASS in Chromium using set_content and simulated localStorage: render, seven tabs, language switches and branding, offline AI and online prerequisite fallback, scam sample, learner creation, both assessments, session, feedback, passport and deletion, six city destinations open, ten-question quiz completion, 390px mobile document width, no uncaught errors in exercised flows.

Pending: actual origin persistence across refresh, every individual simulation end-to-end, keyboard/screen-reader audit, voice and print output, hosted service worker offline reload, live Gemini, actual deployment headers and low-end device performance. No benchmark speed improvement claimed. Run node tests/check.cjs and node tests/community.cjs; optional Python Playwright browser test requires Chromium at /usr/bin/chromium. The browser test uses mocked storage, not real origin navigation.
