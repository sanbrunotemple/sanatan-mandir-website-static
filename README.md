# Sanatan Mandir — San Bruno website

Static site matching the 'Sanatan Mandir website design' mock (Claude artifact JAV7Jvx3EJLJFDgH7sLqiC).
Hosted on GitHub Pages; every push to `main` updates the live site.

## Updating events (the common case)
1. Edit `data/events.json` (one object per event: event, date YYYY-MM-DD, weekday, time_or_note).
2. Run `python3 build_events.py` — regenerates `events.html` and the home-page upcoming list.
3. Commit and push. GitHub Pages redeploys automatically.

Or just tell MukunthRobo what changed — e.g. 'move Diwali to …' — and it will edit, rebuild, verify and push.

## Notes / to confirm with the temple
- Phone shown is the printed calendar number (650) 794-1294; the design mock had a placeholder number.
- Mock placeholder items marked '[confirm]' (donation payment method, EIN/tax-exempt statement, Balvihar fees/times, clinic schedule, parking details) are shown as 'to be confirmed' on the site.
- All photos are placeholders until temple photos are added to the repo.
