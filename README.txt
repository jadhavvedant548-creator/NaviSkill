NAVISKILL V15 — FINAL RELEASE
Public brand: NaviSkill. Start with docs/Deployment_Guide.md and docs/Testing_Report.md. The six reports in docs/ describe the current release; prior version notes below are historical. Existing V14 storage keys retained for same-origin compatibility.

NAVISKILL V13 — PHASE 3 | Intelligent learning refinement
Problem Statement 2: Community-Based Digital Literacy and Skill Development

1. QUICK START (NO API KEY)
Extract the ZIP. Double-click NaviSkill_Offline.html in Chrome or Edge. All original V12 activities, seven tabs, English/Marathi/Hindi, quiz, city and guided missions are retained. New features:
- Floating NaviAI: type a question and choose Offline guide (eight predefined topic guides; not a generative AI response).
- Learn > Scam Detective card > Smart Scam Shield: analyse fictional text locally, or load the sample. Warning signs are heuristic, not proof of fraud or safety.
- Learn > personal roadmap: choose learner profile and starting skill level. Recommendations use these choices, completed activities and best quiz score; this is deterministic, not an AI diagnosis. Click a recommendation to launch the existing guided activity. Profile/level choices are session-only.
- Voice: Speak question (microphone permission, compatible browser and possibly network required); Read answer aloud (installed language voices vary). Typing remains available. Browser speech recognition may send audio to its provider.
V13 starts with fresh local progress, so V12 remains a separate backup. Do not replace the current live website until testing is complete.

2. OPTIONAL ONLINE GEMINI SETUP
A. Create a separate GitHub test repository and upload the CONTENTS of this folder, including api/guide.js, index.html, sw.js, manifest.webmanifest and icon.svg. Do not upload a real .env file. Do not use a static-only deployment that discards the api folder.
B. Import that repository in Vercel. Set Framework Preset to Other, root directory to the folder containing index.html and api/, no custom build command. Deploy.
C. Go to https://aistudio.google.com/apikey and create a Gemini Developer API key. Check the model available to your project at https://ai.google.dev/gemini-api/docs/models ; choose a supported text model that accepts generateContent. Use its exact model ID without the models/ prefix. Billing, quotas and availability vary; review them before enabling.
D. Vercel project Settings > Environment Variables: add GEMINI_API_KEY (your real key), GEMINI_MODEL (exact model ID), NAVISKILL_ACCESS_CODE (a new random private code of 16–128 characters, not the API key). Set the variables for the environment you are testing, then redeploy. To create a code in Node: node -e "console.log(require('crypto').randomBytes(24).toString('hex'))". Share the access code only with trusted exhibition testers; rotate after the event.
E. Open the HTTPS deployed site, click NaviAI, enter a fictional question, enter the exhibition access code, tick consent and click Ask online AI. The code is not saved to browser storage. Only the backend sees the Gemini API key. The question is transmitted to Google only after selecting the online option. No user accounts or chat database. The offline button never makes an AI request.
F. If the server, internet, API key, access code or model is unavailable, the frontend shows local guidance instead. Offline-file mode always falls back. Check your deployment function logs if a configured online request fails; do not print or share secrets.

3. SECURITY LIMITATIONS
Server validates method, content type, origin (if supplied), request body, language/mode, access code and likely personal identifiers. API key is sent only in a server-side header. Backend returns generic errors, uses no-store and limits request length, output and time. In-memory limits (5/min per apparent IP, 30/min per instance) are best-effort, NOT distributed limits; IP headers are not a reliable identity control. Access code is a shared exhibition gate, not a full user authentication system. For wider public use, add platform-level distributed rate limits, account authentication, monitoring, spend caps/quotas and privacy/security review. No guarantee of free usage or accuracy. Never paste real SMS with private information; even heuristic identifier filtering can miss private data. No real payments or official submissions. AI output can be wrong; independently verify important advice.

4. TEST CHECKLIST
- Regression: seven tabs, all 8 activities and guided completion, six city locations, all 10 quiz questions, progress/XP/badges/certificate/reset, mobile controls, three languages, offline file with Wi-Fi disconnected.
- NaviAI offline: type train ticket, spreadsheet or UPI; test Marathi and Hindi; unknown topic should show available topics, not invent an answer.
- Scam Shield: load sample; check warning signs; try benign text and verify it does not label it safe. No actual SMS needed.
- Roadmap: compare different profiles/skill levels; complete a task and check ordering; take quiz and check score. All recommendation buttons should launch existing activities.
- Voice: allow microphone only if comfortable; verify transcription and read-aloud in available languages. Unsupported browser should provide fallback.
- Online: test on Vercel with no config, wrong access code and then valid config; verify fallback, actual AI answer, no key in page source or browser request, and no cached AI response. Test hosted offline reload after service worker activation. Do not assume the standalone offline test proves hosted offline caching.
- Automated checks: run node tests/check.cjs from the project directory (Node 22 recommended). Uses fake credentials and mocked Gemini; no real network call.

5. LOGBOOK CONSISTENCY
Keep Weeks 1–13 unchanged. These are later refinements of multilingual learning, cyber safety, accessibility and individual skill development. Attach actual screenshots and results in additional refinement evidence; do not backdate tests or claim community outcomes not measured.

6. VERIFIED TEST STATUS
Both HTML files passed JS syntax checks, static seven-tab/ID checks, ten-question structure for each language, and offline-guide/scam rule tests. Backend mock passed method, origin, access-code, input, identifier, rate-limit, successful response, upstream error and missing-config checks. Service worker syntax passed. Chromium local file navigation returned ERR_BLOCKED_BY_ADMINISTRATOR, so interactive UI, speech, actual Gemini requests, hosted offline caching and deployment remain unverified. No security audit performed.

7. V14 PHASE 4 ADDITIONS
Community tab: create an anonymous learner with consent, select the learner, take initial assessment, practise original modules, record only observed skills and actual sessions, take final assessment, record rating and difficulty, or delete the learner. Dashboard starts empty and averages only paired assessments; repeated questions may introduce practice effects. Feedback stores the latest rating/difficulty per learner, not free text. Progress tab: select personal or anonymous learner passport, then Print / Save PDF. Records are browser-local, not synced or encrypted; delete learners on shared devices. V14 uses new progress storage keys, so V13 progress is not migrated. Personal reset does not delete community records; delete those individually. No community records are sent to Gemini. Existing API configuration is unchanged. Keep V13 backup. No new tabs. These are post-logbook refinements, not evidence of past testing.
Run node tests/check.cjs and node tests/community.cjs. Community logic tests verify zero-state metrics, paired score changes, feedback averages, scoring and translation counts. Browser execution attempt timed out; manually verify creating/deleting learners, persistence, both assessments, language switching, feedback, print and existing features. No live API or real community testing performed for V14.
