# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Members of the general public, mostly on phones, arriving from social networks (WhatsApp, Instagram, X, Facebook, LinkedIn). People on BOTH sides of the Israel–Gaza debate, curious about AI, non-technical. They have a chat AI they already use (ChatGPT, Gemini, Claude, Copilot, Grok, Meta AI, DeepSeek, Le Chat, Perplexity). Their job: copy one exact question into their own chat, bring back the answer (share link or pasted text), say what it concluded and whether it leans to one side, optionally test another chat, then see how chats compare.

## Product Purpose

ChatRadar (TheChatRadar.com) is a citizen experiment that measures, chat by chat, whether AI chatbots answer a contested question with a systematic lean. One conversation proves nothing; thousands of real answers collected by participants can. Success: many participants from both sides complete the test (about 3 minutes), test more than one chat, share it, and the aggregated, verifiable data can be published per chat and taken to the companies whose chats show the most uneven answers.

## Positioning

Instead of experts testing models in a lab, ordinary users test the chats they actually use, with the exact same words, in their own language and country, and bring back verifiable share links. Each chat is measured on its own and never averaged with the others.

## Operating Context

- Test #1 is a single question about the Gaza war, loaded on purpose (the founder's real question to ChatGPT); the site measures whether each AI follows, corrects or balances that point of view. A Test #2 loaded from the opposite angle is announced; visitors can suggest new topics.
- Flow: landing → copy the question / open a chat → bring back link or text → 2 required ratings (conclusion; lean: Israeli / balanced / Palestinian / not sure) + optional argument boxes (4 per side + 1 neutral) + optional own stance → invite to test another chat → "Your chats" (own rating vs everyone's average per chat, all chats compared, 2-axis map) → detailed results.
- Results and the landing needle are hidden until the visitor has taken part (to avoid anchoring); counts are visible.
- Languages: English (main landing), Spanish, French, Hebrew (RTL). Country is derived from the connection; IP is never stored.
- Runs as a Flask app on PythonAnywhere; domain thechatradar.com.

## Capabilities and Constraints

- Neutrality is the core constraint: nothing in the design, colors, wording or order may signal a side. No flag colors (blue/white; red/green/black), no alarm red, purple avoided (perceived political meaning), both ends of any scale identical in color, size and weight. Sides follow alphabetical order in each language (Israeli left in LTR, right in Hebrew) with the rule stated visibly; the order of answer options in the form is randomized per visitor.
- The word "genocide" appears only inside the verbatim question and the conclusion question label, never in headlines, buttons or share texts.
- Share texts never include the participant's own verdict.
- Must work at 390px wide and in RTL; four languages for every visible string.
- Fake answers are filtered (share links, keyword checks, duplicates); admin moderation exists.
- Undecided: who signs the project publicly (unsigned for now; do not invent a founder name, team or organization). Test #2 question not chosen yet.

## Brand Commitments

- Name: ChatRadar; address written as TheChatRadar.com; contact hello@thechatradar.com.
- Voice: curious, calm, fair. Citizen observatory, not activism. No "exposed", "truth", "propaganda", exclamation marks in headlines.
- Founder's origin story: asked ChatGPT the question, felt the answer leaned to one side; after pushback ChatGPT said "Your criticism of my previous answer is valid: I presented the issue in a way that was too one-sided." The quote lives on the method page, not on the landing.

## Evidence on Hand

- No real participant data yet (only test data). No testimonials, press, partners or endorsements: do not fabricate any.
- Real sample answers exist from Gemini and Claude to the test question (founder's own tests).
- Manifesto draft (unpublished): ai-bias-lab/borradores/manifiesto.md.

## Product Principles

1. Both sides must feel the site is fair and want to take part; credibility with skeptics outranks virality.
2. Measure, don't accuse: compare answers chat by chat with observable evidence (share links, argument boxes), never a verdict on people.
3. Fast and frictionless on a phone: one question, about 3 minutes, no sign-up.
4. Curiosity and reciprocity drive participation: see results after taking part, then test another chat.
5. Built to expand to other topics; Gaza is Test #1, not the brand.

## Accessibility & Inclusion

Mobile-first, readable at 390px, RTL Hebrew, WCAG AA contrast, reduced-motion respected.
