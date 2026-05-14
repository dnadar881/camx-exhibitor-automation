
# CAMX Exhibitor Automation

## Overview
This project scrapes exhibitors from CAMX 2026 and generates personalized first lines for cold outreach.

## Features
- Scrapes exhibitor data using Selenium
- Extracts company descriptions and links
- Generates personalized first lines using signal-based logic
- Exports data to CSV / Google Sheets

## Tech Stack
- Python
- Selenium
- Pandas

## Workflow
1. Scrape exhibitor list (dynamic scrolling)
2. Visit each profile page
3. Extract and clean description
4. Generate first line using prompt/fallback logic
5. Export to CSV

## Prompt Used
You are writing the first sentence of a cold email to a company exhibiting at CAMX.

INPUT:
Company Name: {company_name}
Description: {description}

- Identify ONE clear signal
- Use only that signal
- Keep it natural and specific
- One sentence only

## Note
All first lines were generated programmatically. Minor edits were applied for readability.
