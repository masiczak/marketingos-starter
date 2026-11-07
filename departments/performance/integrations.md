# performance · integrations

The skill works today with CSV exports. Connecting tools removes the export step.
Connect **read-only first**. Write access (pausing, budgets) only after read works, and always
with a human approving each change.

| Tool | What it adds | Status | How to connect |
|---|---|---|---|
| Google Ads | campaign + search terms data | `TODO: connect` | `/marketingos-setup` → Step 4 |
| Microsoft Ads | campaign data | `TODO: connect` | Step 4 |
| LinkedIn Campaign Manager | campaign data | `TODO: connect` | Step 4 |
| Meta Ads | campaign data | `TODO: connect` | Step 4 |
| GA4 | what happens after the click | `TODO: connect` | Step 4 |

Until connected: export CSVs (campaign level, two periods) and attach them.
