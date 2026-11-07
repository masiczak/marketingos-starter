# Integrations guide (used by marketingos-setup, Step 4)

> Written November 2026. Connectors, APIs and plans change every month.
> **Before following any line below, check the vendor's current documentation and tell the user
> the date you checked.** If reality differs from this file, follow reality and update this file.

For every tool: start read-only, keep credentials out of this folder (only paths or names in `.env`),
record the result in the department's `integrations.md`.

---

## Google Search Console → content-architect

- **What it gives:** real queries, impressions, clicks and positions for your site and pages.
- **You need:** access to the property (Owner or Full user to set up; Restricted is enough to read).
- **Ways in:**
  - *Ready connector:* at the time of writing, Google had no official Search Console MCP server.
    Check again. Community servers exist: rung 3, security check first, read-only.
  - *Script:* the Search Console API (Search Analytics query). Needs a Google Cloud project,
    the API enabled, and OAuth or a service account added as a user on the property.
  - *Export:* Performance report → filter by query or page → Export (CSV/Sheets).
    The UI export is capped (around 1,000 rows), which is fine for one topic.
- **Check it works:** pull last 28 days of queries for one page and compare one number with the UI.

## Google Analytics 4 → content-architect, performance

- **What it gives:** sessions, engagement, conversions per page and per channel.
- **You need:** Viewer access to the GA4 property; the property ID.
- **Ways in:**
  - *Ready connector:* Google publishes an official, read-only, open-source GA4 MCP server
    (labelled experimental at the time of writing). Setup needs a Google Cloud project with the
    Analytics Admin and Data APIs enabled, plus local Google credentials. Usually needs
    someone comfortable with a terminal for 30-60 minutes.
  - *Script:* Analytics Data API (runReport). Same Cloud project and credentials.
  - *Export:* any report → Share → Download file (CSV).
- **Check it works:** sessions for yesterday match the GA4 UI.

## Google Ads → performance

- **What it gives:** campaign, ad group, keyword and search-term performance.
- **You need:** access to the Ads account (or manager account); for API/MCP routes also a
  **developer token** (applied for in the manager account's API Center; approval levels limit
  usage) and OAuth credentials.
- **Ways in:**
  - *Ready connector:* Google publishes an official open-source Google Ads MCP server (read-only
    at the time of writing). Needs the developer token and a Cloud project.
  - *Script:* Google Ads API with GAQL queries. Same requirements.
  - *Export:* Campaigns view → set date range → Download (CSV). Search terms report the same way.
- **Write access** (pausing, budgets): only after read works for weeks, and every change still
  needs a human yes. Many teams never need it.

## Microsoft Ads / LinkedIn Campaign Manager / Meta Ads → performance

- Check each vendor's current docs for an official connector first. Availability changes often.
- APIs exist for all three; LinkedIn and Meta require an approved developer app for API access,
  which can take time. Organic social APIs (posting, page analytics) are usually harder to get than ads APIs.
- *Export always works:* campaign-level CSV for two periods → `weekly-performance-review`.

## CMS → content-architect

Ask which CMS. Then:
- **WordPress:** REST API with an Application Password (per user, revocable). An official MCP
  adapter from the WordPress project was reported at the time of writing; check its status.
  Start with reading posts/pages only.
- **Webflow, HubSpot CMS, Contentful, Sanity, Storyblok, other:** check for an official connector
  in the vendor's docs and in the Claude connector directory; otherwise use their content API
  with a read-only token.
- **Hard rule:** the AI may save drafts at most. A human publishes. Configure the token/role so
  publishing is impossible if the CMS allows that.
- *Without integration:* paste the page URL or text; the skill works the same.

## CRM → abm-outbound

- **HubSpot:** offers an official Claude connector (sign in, choose scopes). Start with read scopes.
- **Salesforce, Pipedrive, other:** check for an official connector; otherwise API with a
  read-only user, or a CSV export of the accounts list.
- Keep personal data minimal: the skills need company-level data and roles, not private contact details.

## Calendar and mail → executive-assistant

- Use the official connectors offered in the Claude app (e.g. Google Workspace, Microsoft 365)
  where available. Read-only scopes.
- The morning brief never sends, accepts or declines. Suggestions only.
- *Without integration:* paste today's calendar and the subject lines that matter.

## Website visitor / intent tools → abm-outbound

- Many tools keep API access for higher plans. Check the plan.
- *Export:* list of identified companies for the last 7 days (CSV) → paste into `account-brief`.
- Visiting companies are prospects: don't paste their names into public places; the shared repo is private.

---

## Template for a department's integrations.md row once connected

`| Google Ads | campaign + search terms | connected YYYY-MM-DD, read-only, official MCP | owner: {role} |`
