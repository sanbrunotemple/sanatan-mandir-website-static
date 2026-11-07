import json, shutil, os, html, datetime
from pathlib import Path
src = Path.home()/"workspace/sanatan-mandir/sanatan_mandir_2026_events.json"
events = json.loads(src.read_text())
root = Path.home()/"workspace/sanatan-mandir-website"
(root/"assets").mkdir(parents=True, exist_ok=True)
(root/"data").mkdir(parents=True, exist_ok=True)
shutil.copy(src, root/"data/events.json")
shutil.copy(Path.home()/"workspace/sanatan-mandir/sanatan_mandir_2026_events.csv", root/"data/events.csv")
shutil.copy(Path.home()/"workspace/sanatan-mandir/sanatan_mandir_2026.ics", root/"data/calendar.ics")

ADDRESS="205 W Angus Avenue, San Bruno, CA 94066"
PHONE="(650) 794-1294"
EMAIL="SanatanMandirSanBruno@gmail.com"

CSS = """
:root{--cream:#FBF3E2;--surface:#FFFDF6;--ink:#3A2011;--muted:#A46C4F;--saffron:#F07A15;--saffron-deep:#D65F00;--maroon:#9A3818;--maroon-deep:#7A2B12;--gold:#DCC083;--tan:#E3C79A;--radius:20px}
*{box-sizing:border-box}body{margin:0;font-family:Inter,system-ui,Arial,sans-serif;color:var(--ink);background:var(--cream);line-height:1.6}
h1,h2,h3{font-family:'Cormorant Garamond',Georgia,serif;line-height:1.15;margin:.2em 0 .4em}h1{font-size:clamp(40px,6vw,64px)}h2{font-size:clamp(28px,4vw,36px)}a{color:var(--maroon)}
.wrap{max-width:1200px;margin:0 auto;padding:0 20px}.section{padding:72px 0}
.eyebrow{font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--saffron-deep)}
.announce{background:linear-gradient(90deg,var(--saffron),var(--gold));color:#fff;text-align:center;padding:9px 40px;font-size:14px;position:relative}
.announce button{position:absolute;right:12px;top:4px;background:none;border:0;color:#fff;font-size:18px;cursor:pointer}
.utility{background:var(--ink);color:#F7E8CF;font-size:13px}.utility .wrap{display:flex;gap:18px;flex-wrap:wrap;padding-top:8px;padding-bottom:8px}
header.site{background:var(--surface);position:sticky;top:0;z-index:10;border-bottom:1px solid var(--tan)}
header.site .wrap{display:flex;align-items:center;gap:22px;padding-top:14px;padding-bottom:14px;flex-wrap:wrap}
.logo{display:flex;align-items:center;gap:12px;text-decoration:none;color:var(--ink)}
.om{width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,var(--saffron),var(--gold));display:grid;place-items:center;font-size:26px;color:#fff}
.logo b{font-family:'Cormorant Garamond',serif;font-size:22px;letter-spacing:.04em}.logo span{display:block;font-size:11px;letter-spacing:.18em;color:var(--muted)}
nav.main{display:flex;gap:16px;flex-wrap:wrap;margin-left:auto}nav.main a{text-decoration:none;color:var(--ink);font-size:15px}
.btn{display:inline-block;padding:11px 20px;border-radius:999px;text-decoration:none;font-weight:600;border:1px solid var(--maroon);color:var(--maroon);background:transparent}
.btn.primary{background:linear-gradient(90deg,var(--saffron),var(--saffron-deep));color:#fff;border:0}.btn.dark{background:var(--ink);color:#fff;border:0}
.hero{background:linear-gradient(120deg,var(--maroon-deep),var(--maroon) 40%,var(--saffron) 85%,var(--gold));color:#fff;border-radius:0 0 28px 28px}
.hero .wrap{display:grid;grid-template-columns:1.2fr .8fr;gap:32px;padding-top:64px;padding-bottom:64px;align-items:center}
.ph{border:2px dashed var(--tan);background:#FFF8E8;color:var(--muted);border-radius:var(--radius);min-height:220px;display:grid;place-items:center;text-align:center;padding:20px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:24px}
.card{background:var(--surface);border:1px solid var(--tan);border-radius:var(--radius);padding:22px}
.card.dark{background:var(--ink);color:#F7E8CF}.chip{display:inline-block;background:#EAF6EC;color:#256029;border-radius:999px;padding:2px 10px;font-size:12px;font-weight:700}
.datechip{display:inline-block;background:var(--saffron);color:#fff;border-radius:10px;padding:4px 10px;font-weight:700;font-size:13px}
.divider{text-align:center;color:var(--gold);font-size:22px;margin:10px 0}
.band{background:linear-gradient(90deg,var(--saffron),var(--gold));border-radius:var(--radius);padding:36px;color:#fff}
footer{background:var(--ink);color:#EEDFC2;padding:56px 0 28px;margin-top:0}footer a{color:#F3C98B}footer .grid{gap:32px}
input.search{width:100%;padding:13px 16px;border-radius:12px;border:1px solid var(--tan);font-size:16px;background:#fff}
.month{margin-top:36px}.event-row{display:flex;gap:16px;align-items:baseline;padding:12px 0;border-bottom:1px solid var(--tan)}
.event-row time{font-weight:700;min-width:170px}.small{font-size:14px;color:#6B4A2F}
@media(max-width:760px){.hero .wrap{grid-template-columns:1fr}.section{padding:48px 0}.event-row{flex-direction:column;gap:2px}}
"""
(root/"assets/style.css").write_text(CSS)
JS = """
document.querySelectorAll('[data-dismiss]').forEach(b=>b.onclick=()=>b.parentElement.remove());
const q=document.querySelector('#eventSearch'); if(q){q.addEventListener('input',()=>{const v=q.value.toLowerCase();document.querySelectorAll('.event-row').forEach(r=>r.style.display=r.textContent.toLowerCase().includes(v)?'':'none');document.querySelectorAll('.month').forEach(m=>{const any=[...m.querySelectorAll('.event-row')].some(r=>r.style.display!=='none');m.style.display=any?'':'none'})})}
"""
(root/"assets/site.js").write_text(JS)

def header(active=""):
    nav=[("Home","index.html"),("Events","events.html"),("Services","services.html"),("Balvihar","balvihar.html"),("About","about.html"),("Resources","resources.html"),("Gallery","gallery.html"),("Visit","visit.html")]
    links="".join(f'<a href="{u}">{n}</a>' for n,u in nav)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sanatan Mandir — San Bruno, California</title><link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="assets/style.css"></head><body>
<div class="announce">NOTICE — Diwali / Amavasya Laxmi Pooja — Sun, Nov 8, 5:19–7:09 PM. All are welcome.<button data-dismiss aria-label="Dismiss">×</button></div>
<div class="utility"><div class="wrap"><span>Open today · 8:00 AM–12:00 PM &amp; 4:00 PM–8:00 PM</span><span>{PHONE}</span><span>{ADDRESS}</span></div></div>
<header class="site"><div class="wrap"><a class="logo" href="index.html"><span class="om">ॐ</span><span><b>Sanatan Mandir</b><span>SAN BRUNO, CALIFORNIA</span></span></a><nav class="main">{links}</nav><a class="btn" href="visit.html">Directions</a><a class="btn primary" href="donate.html">Donate</a></div></header>"""

FOOTER=f"""<footer><div class="wrap"><div class="grid"><div><h3>ॐ Sanatan Mandir</h3><p>A Hindu temple and community learning center in San Bruno, serving Bay Area families.</p></div>
<div><h3>Visit</h3><p>{ADDRESS}<br>{PHONE}<br>{EMAIL}</p><p><a href="https://www.google.com/maps/search/?api=1&query=Sanatan+Mandir+205+W+Angus+Ave+San+Bruno+CA+94066">Get directions</a></p></div>
<div><h3>Temple hours</h3><p>Mon, Wed–Sun: 8 AM–12 PM &amp; 4–8 PM<br>Tuesday: 8 AM–12 PM &amp; 4–9 PM<br>Daily aarti: 8 AM &amp; 4 PM</p></div>
<div><h3>Quick links</h3><p><a href="events.html">Events</a><br><a href="balvihar.html">Balvihar</a><br><a href="services.html">Services &amp; Health Clinic</a><br><a href="resources.html">Hinduism Resources</a><br><a href="data/calendar.ics">Annual Calendar (.ics)</a></p></div></div>
<p class="small" style="color:#C9A87A">© 2000–2026 Sanatan Mandir of San Bruno. All rights reserved. · <a href="contact.html">Contact</a> · Nonprofit / tax-exempt statement — pending confirmation.</p></div></footer><script src="assets/site.js"></script></body></html>"""

def fmt(d):
    dt=datetime.date.fromisoformat(d); return dt.strftime("%a, %b %-d, %Y")
upcoming=[e for e in events if e["date"]>="2026-11-08"]
def event_card(e):
    note=f' — {html.escape(e["time_or_note"])}' if e.get("time_or_note") else ""
    return f'<article class="card"><span class="datechip">{fmt(e["date"])}</span><h3>{html.escape(e["event"])}</h3><p class="small">{html.escape(e["weekday"])}{note}</p><p class="small">{ADDRESS}</p></article>'

home_cards="".join(event_card(e) for e in upcoming[:6])
index = header()+f"""<section class="hero"><div class="wrap"><div><p class="eyebrow" style="color:var(--gold)">Welcome to</p><h1>Where devotion feels like coming home.</h1><p>A welcoming mandir in San Bruno — for darshan, satsang, language and culture, and seva.</p><p><a class="btn primary" href="events.html">See upcoming events</a> <a class="btn dark" href="visit.html">Plan your visit</a></p></div><div class="ph">Mandir courtyard or murti photo<br><span class="small">Placeholder — replace with a temple photo</span></div></div></section>
<section class="section"><div class="wrap"><div class="grid">
<div class="card"><h3>Darshan hours</h3><p><span class="chip">Open today</span></p><p>Morning 8:00 AM–12:00 PM<br>Evening 4:00 PM–8:00 PM</p><p class="small">Tuesday evening aarti extends to 9:00 PM.</p></div>
<div class="card"><h3>This week</h3><p><strong>Diwali / Amavasya Laxmi Pooja</strong><br>Sun, Nov 8 · 5:19–7:09 PM</p><p><a href="events.html">View the full calendar →</a></p></div>
<div class="card"><h3>Festival spotlight</h3><p><strong>Anakutt Govardhan Pooja</strong><br>Mon, Nov 9</p><p><a href="events.html">Details →</a></p></div></div>
<div class="divider">✦</div><p class="eyebrow">Festivals &amp; gatherings</p><h2>Upcoming events</h2><p>From the Mandir's 2026 calendar — all are welcome.</p><div class="grid">{home_cards}</div><p style="margin-top:22px"><a class="btn" href="events.html">Full calendar</a> <a class="btn" href="data/calendar.ics">Download calendar (.ics)</a></p></div></section>
<section class="section" style="padding-top:0"><div class="wrap"><h2>A rhythm for every week</h2><div class="grid"><div class="card dark"><h3>Daily aarti</h3><p>Every day · 8 AM &amp; 4 PM</p></div><div class="card dark"><h3>Saturday satsang</h3><p>Every Saturday · 6:00 PM</p></div><div class="card"><h3>Sunday Balvihar</h3><p>Language, stories and values for children.</p></div><div class="card"><h3>Monthly havan</h3><p>See the events calendar for dates.</p></div></div></div></section>
<section class="section" style="padding-top:0"><div class="wrap"><h2>Services</h2><div class="grid"><div class="card"><h3>✦ Puja &amp; homam</h3><p class="small">Book a puja with the temple — see Services.</p></div><div class="card"><h3>✦ Prasad &amp; hall booking</h3><p class="small">Community hall and prasad arrangements.</p></div><div class="card"><h3>✦ Health Clinic (Free)</h3><p class="small">Free clinic — schedule to be confirmed.</p></div><div class="card"><h3>✦ Hinduism Resources</h3><p class="small">Learning resources for all ages.</p></div></div>
<div class="band" style="margin-top:28px"><h2>Balvihar: language, stories, and values</h2><p>Classes for children aged 5–14.</p><a class="btn dark" href="balvihar.html">Explore Balvihar</a></div></div></section>
<section class="section" style="padding-top:0"><div class="wrap"><h2>A temple built by its community</h2><p>Serving Bay Area families for 25 years, founded in San Bruno by families who wanted authentic worship, language and culture close to home.</p><div class="grid"><div class="card"><h3>25</h3><p class="small">Years of service</p></div><div class="card"><h3>2,000+</h3><p class="small">Families served</p></div><div class="card"><h3>700+</h3><p class="small">Volunteers</p></div><div class="card"><h3>108</h3><p class="small">Calendar events in 2026</p></div></div></div></section>
"""+FOOTER
(root/"index.html").write_text(index)

# Events page grouped by month
from collections import OrderedDict
months=OrderedDict()
for e in events: months.setdefault(e["date"][:7],[]).append(e)
parts=[header(),'<main class="section"><div class="wrap"><p class="small"><a href="index.html">Home</a> / Events</p><h1>Events</h1><p>Festivals, satsangs and community programs from the Mandir Calendar 2026. To update an event, edit <code>data/events.json</code> and re-run <code>build_events.py</code> — see the README.</p><input id="eventSearch" class="search" placeholder="Search events — try Diwali, Ekadashi, Purnima…"><p><a class="btn" href="data/calendar.ics">Download all as .ics</a></p>']
for ym, evs in months.items():
    dt=datetime.date.fromisoformat(ym+"-01"); parts.append(f'<section class="month"><h2>{dt.strftime("%B %Y")}</h2>')
    for e in evs:
        note=f' · {html.escape(e["time_or_note"])}' if e.get("time_or_note") else ""
        parts.append(f'<div class="event-row"><time>{fmt(e["date"])}</time><span><strong>{html.escape(e["event"])}</strong><span class="small">{note}</span></span></div>')
    parts.append('</section>')
parts.append('</div></main>'+FOOTER)
(root/"events.html").write_text("".join(parts))

def simple(name,title,body):
    (root/name).write_text(header()+f'<main class="section"><div class="wrap"><h1>{title}</h1>{body}</div></main>'+FOOTER)

simple("services.html","Services",'<div class="grid"><div class="card"><h3>Puja &amp; homam</h3><p>Arrange a puja or homam at the mandir or at home. Contact the temple to book and confirm priest availability and fees.</p></div><div class="card"><h3>Prasad &amp; hall booking</h3><p>Hall rental and prasad arrangements for community events — contact the temple for rates and availability.</p></div><div class="card"><h3>Health Clinic (Free)</h3><p>Free community health clinic. Schedule in the design mock is to be confirmed — please call before visiting.</p></div><div class="card"><h3>Become a member</h3><p>Membership supports daily worship and programs. Ask at the mandir for details.</p></div></div>')
simple("balvihar.html","Balvihar",'<p>Classes for children aged 5–14: stories, language, shloka, bhajans, and service projects.</p><div class="ph">Classroom or Balvihar photo — placeholder</div><p class="small">Class times, curriculum and fees were marked “to confirm” in the design mock — contact the temple to enroll.</p><p><a class="btn primary" href="contact.html">Enroll your child →</a></p>')
simple("about.html","About",'<p>Sanatan Mandir in San Bruno, California — a Hindu temple and community learning center serving Bay Area families since 2000, founded by families who wished for authentic worship, language and culture close to home.</p><div class="grid"><div class="card"><h3>25 years</h3><p class="small">of service</p></div><div class="card"><h3>2,000+</h3><p class="small">families served</p></div><div class="card"><h3>700+</h3><p class="small">volunteers</p></div></div>')
simple("resources.html","Resources",'<p>Hinduism learning resources, the annual calendar, and downloads.</p><div class="grid"><div class="card"><h3>Annual Calendar 2026</h3><p><a href="data/calendar.ics">Download .ics</a> · <a href="data/events.json">Events data (JSON)</a> · <a href="data/events.csv">CSV</a></p></div><div class="card"><h3>WhatsApp event bot</h3><p>Ask the Mandir bot for any festival date — demo live on the test number.</p></div></div>')
simple("gallery.html","Gallery",'<p>Recent celebrations and community moments.</p><div class="grid">' + '<div class="ph">Temple photo — placeholder</div>'*6 + '</div>')
simple("visit.html","Plan your visit",f'<div class="grid"><div class="card"><h3>Address</h3><p>{ADDRESS}<br>{PHONE}</p><p><a class="btn" href="https://www.google.com/maps/search/?api=1&query=Sanatan+Mandir+205+W+Angus+Ave+San+Bruno+CA+94066">Get directions</a></p></div><div class="card"><h3>Temple hours</h3><p>Mon, Wed–Sun: 8 AM–12 PM &amp; 4–8 PM<br>Tuesday: 8 AM–12 PM &amp; 4–9 PM<br>Daily aarti: 8 AM &amp; 4 PM</p></div><div class="card"><h3>Getting there</h3><p>Street parking is limited; please be neighbourly. Accessible parking near the entrance — details to be confirmed.</p></div></div>')
simple("contact.html","Contact",f'<div class="card"><p><strong>Sanatan Mandir</strong><br>{ADDRESS}<br>Phone: {PHONE}<br>Email: {EMAIL}</p><p class="small">For puja bookings, Balvihar enrollment and hall rental, please call or visit during temple hours.</p></div>')
simple("donate.html","Support the mandir",'<p>Your seva sustains daily worship, Balvihar and community service.</p><div class="grid"><div class="card"><h3>Where your offering goes</h3><p>✦ Daily worship — puja materials, flowers, prasad<br>✦ Balvihar &amp; education<br>✦ Festivals &amp; mahaprasad<br>✦ Building &amp; upkeep</p><p class="small">Tax-exempt status, EIN and legal name will appear here once confirmed by the temple.</p></div><div class="card"><h3>Make an offering</h3><p>Donations are accepted through the temple’s approved method, and in person at the mandir. Payment method to be confirmed — the mandir does not store card details on this site.</p><a class="btn primary" href="contact.html">Continue to donate</a></div></div>')

(root/".nojekyll").write_text("")
(root/"README.md").write_text("""# Sanatan Mandir — San Bruno website

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
""")
print("built", root)
