# -*- coding: utf-8 -*-
"""Generates the SEO location pages in /locations from one template.

To add a city: add an entry to CITIES, run `python tools/gen_locations.py`,
then add the new page to sitemap.xml and the locations grid in index.html.
"""
import os

BASE_URL = "https://jconn5803.github.io/jconn5803-web"

CITIES = [
    {
        "slug": "newcastle",
        "name": "Newcastle upon Tyne",
        "short": "Newcastle",
        "region": "the North East",
        "in_person": True,
        "meta": "Done-for-you AI automation for Newcastle businesses. Based in the North East, I build automations that handle the quoting, chasing and admin eating your week. Book a free call.",
        "intro": "Newcastle is my home city, which makes this the one place on this site where 'local' actually means local. From agencies on the Quayside to trades in Gosforth and family firms across the Toon, I help Newcastle businesses hand their repetitive admin to software — and because I'm based here, we can map your time leaks face-to-face over a coffee.",
        "local": "Newcastle's business scene is a mix of creative agencies, professional services, construction and trades, recruitment firms and a fast-growing tech crowd around Ouseburn and the Helix. Almost all of them share the same problem: skilled people spending hours every week retyping data, chasing invoices and answering the same enquiries by hand. Those are exactly the jobs AI automation does best.",
        "industries": "agencies, trades and construction firms, recruiters, e-commerce sellers and professional services across Newcastle and Tyneside",
    },
    {
        "slug": "sunderland",
        "name": "Sunderland",
        "short": "Sunderland",
        "region": "the North East",
        "in_person": True,
        "meta": "AI automation for Sunderland businesses — done for you. From manufacturing supply chains to service firms, I automate the admin, quoting and reporting that drains your week. Book a free call.",
        "intro": "Sunderland calls itself a software city, but most of its businesses still run on copy-paste. I build done-for-you AI automations for Sunderland firms — and being based in the North East, I can sit down with you in person to find where your hours are going.",
        "local": "Between the manufacturing and automotive supply chain around Nissan, the logistics firms that serve it, contact-centre operations and a growing digital sector at places like Sunderland Software Centre, Wearside businesses handle enormous volumes of orders, paperwork and customer queries. Every one of those flows is a candidate for automation — and the savings compound with volume.",
        "industries": "manufacturing and automotive suppliers, logistics firms, contact centres, trades and service businesses across Sunderland and Wearside",
    },
    {
        "slug": "durham",
        "name": "Durham",
        "short": "Durham",
        "region": "the North East",
        "in_person": True,
        "meta": "AI automation for Durham businesses. I build done-for-you automations for County Durham firms — bookings, invoicing, enquiries and reporting handled by software. Book a free call.",
        "intro": "From professional services in the city to hospitality around the Cathedral and trades across County Durham, most Durham businesses are small teams where the owner does the admin at night. That's precisely where automation pays back fastest — and I'm close enough to come and map it with you in person.",
        "local": "County Durham runs on small and family businesses: solicitors and accountants, B&Bs and restaurants serving the tourist trade, builders and trades covering huge rural patches. Small teams feel time leaks hardest — there's no spare admin person to absorb them. Automating bookings, quotes, invoice chasing and supplier paperwork routinely gives a Durham business owner their evenings back.",
        "industries": "professional services, hospitality and tourism businesses, trades and rural firms across Durham and County Durham",
    },
    {
        "slug": "middlesbrough",
        "name": "Middlesbrough & Teesside",
        "short": "Middlesbrough",
        "region": "Teesside",
        "in_person": True,
        "meta": "AI automation for Middlesbrough and Teesside businesses. Done-for-you automations for engineering, logistics and service firms — quoting, compliance and admin handled. Book a free call.",
        "intro": "Teesside builds real things — and the paperwork that comes with real things is brutal. RAMS, quotes, PO chasing, compliance records, timesheets. I build done-for-you automations for Middlesbrough and Teesside businesses that take that load off your desk, and I'm near enough to do it face-to-face.",
        "local": "With the engineering and process-industry supply chain, the growth around Teesworks and the freeport, and the logistics and construction firms that serve them, Teesside businesses drown in documents: quotes against tight deadlines, purchase orders, certs and compliance paperwork. Automating document handling and quoting isn't a luxury here — it's the difference between bidding on five jobs a week and fifteen.",
        "industries": "engineering and fabrication firms, process-industry suppliers, hauliers and logistics companies, and construction businesses across Middlesbrough, Stockton and wider Teesside",
    },
    {
        "slug": "leeds",
        "name": "Leeds",
        "short": "Leeds",
        "region": "Yorkshire",
        "in_person": False,
        "meta": "AI automation for Leeds businesses — done for you. I automate client onboarding, document handling, reporting and admin for Leeds firms. Book a free 30-minute call, no obligation.",
        "intro": "Leeds is the biggest legal and financial centre in England outside London — which means a city full of businesses that run on documents, deadlines and billable hours. Every hour of admin is an hour you can't bill. I build done-for-you AI automations that hand that admin to software.",
        "local": "Leeds firms — law practices, accountancies, financial services, healthtech companies and the agencies that serve them — share one economic fact: their people's time is the product. Client onboarding packs, engagement letters, document summarising, time capture and monthly reporting are all automatable today. I worked for years with Yorkshire clients (including Yorkshire Water) building exactly these kinds of data and automation pipelines.",
        "industries": "law firms, accountancy practices, financial services, healthtech companies, recruiters and agencies across Leeds and West Yorkshire",
    },
    {
        "slug": "manchester",
        "name": "Manchester",
        "short": "Manchester",
        "region": "the North West",
        "in_person": False,
        "meta": "AI automation for Manchester businesses. Done-for-you automations for agencies, e-commerce and service firms — enquiries answered, admin eliminated, reporting automated. Book a free call.",
        "intro": "Manchester moves fast, and the businesses that win here are the ones that respond first. A lead that emails five Manchester agencies books the one that replies in minutes. I build done-for-you AI automations that make your business the fast one — without hiring anyone.",
        "local": "From agencies and SaaS companies around Ancoats and Spinningfields to e-commerce brands, property firms and professional services across Greater Manchester, the city's businesses compete on speed and volume. AI that answers enquiries instantly, drafts proposals from your past pricing and keeps your pipeline updated automatically is a structural advantage your competitors mostly don't have yet.",
        "industries": "agencies, SaaS and tech companies, e-commerce brands, property firms and professional services across Manchester and the North West",
    },
    {
        "slug": "birmingham",
        "name": "Birmingham",
        "short": "Birmingham",
        "region": "the West Midlands",
        "in_person": False,
        "meta": "AI automation for Birmingham businesses. I build done-for-you automations for manufacturers, trades and service firms in the West Midlands — quotes, orders and admin handled. Book a free call.",
        "intro": "Birmingham and the Black Country have been making things longer than almost anywhere on earth — and the admin around making things (quotes, orders, delivery notes, invoices, chasing) hasn't improved much since the fax machine. I build done-for-you automations that drag that paperwork into the modern era.",
        "local": "The West Midlands is dense with manufacturers, engineering suppliers, wholesalers, logistics operators and trades — businesses where every job generates a paper trail. Automating the trail (order acknowledgements, invoice runs, delivery confirmations, payment chasing) frees up office staff for the work that actually needs a human, and removes the retyping errors that cost real money.",
        "industries": "manufacturers, engineering suppliers, wholesalers, logistics firms and trades across Birmingham and the West Midlands",
    },
    {
        "slug": "london",
        "name": "London",
        "short": "London",
        "region": "London",
        "in_person": False,
        "meta": "AI automation for London businesses. Done-for-you AI automations — enquiries, onboarding, documents and reporting handled by software, at North East rates. Book a free call.",
        "intro": "Nowhere in the UK is an hour of staff time more expensive than London. Which means nowhere does automation pay back faster. I build done-for-you AI automations for London businesses — delivered remotely, at North East rates rather than Zone 1 ones.",
        "local": "London businesses — consultancies, agencies, property firms, financial services, e-commerce brands — pay the country's highest salaries and rents, then spend those expensive hours on data entry, enquiry handling and report assembly. Every process you automate at London staff costs returns multiples of what the same automation saves elsewhere. Everything is scoped, built and handed over remotely, with the same documentation and support as if I were down the corridor.",
        "industries": "consultancies, agencies, property and financial services firms, and e-commerce brands across Greater London",
    },
    {
        "slug": "glasgow",
        "name": "Glasgow",
        "short": "Glasgow",
        "region": "Scotland",
        "in_person": False,
        "meta": "AI automation for Glasgow businesses — done for you. Quoting, job sheets, invoicing and enquiries automated for engineering, trades and service firms. Book a free call.",
        "intro": "Glasgow's businesses are practical — they want to know what something does, what it saves and when it'll be working. Fair enough. I build done-for-you AI automations for Glasgow firms: software that does the retyping, chasing and answering your team currently does by hand.",
        "local": "Across Glasgow's engineering and manufacturing firms, construction and trades, hospitality venues and professional services, the pattern is the same: experienced staff spending hours on quotes, job sheets, supplier paperwork and the same dozen customer questions. Those hours are automatable now — and having studied in Scotland (St Andrews, mathematics), I'm always glad of a reason to work with Scottish businesses.",
        "industries": "engineering and manufacturing firms, construction and trades, hospitality venues and professional services across Glasgow and the West of Scotland",
    },
    {
        "slug": "edinburgh",
        "name": "Edinburgh",
        "short": "Edinburgh",
        "region": "Scotland",
        "in_person": False,
        "meta": "AI automation for Edinburgh businesses. Done-for-you automations for financial services, tourism and professional firms — bookings, documents and reporting handled. Book a free call.",
        "intro": "Edinburgh runs on two clocks: the steady rhythm of financial and professional services, and the August chaos of the world's biggest arts festival. Both produce mountains of repetitive admin. I build done-for-you AI automations for Edinburgh businesses that make those mountains disappear.",
        "local": "From financial services and fintech around the Exchange district to law firms on the Royal Mile and the hotels, venues and tour operators that ride the tourism wave, Edinburgh businesses juggle bookings, compliance documents, client onboarding and seasonal enquiry spikes. AI handles spikes brilliantly — it answers the thousandth enquiry as quickly as the first. I studied mathematics at St Andrews, so Scotland is familiar ground.",
        "industries": "financial services and fintech firms, law and professional practices, hotels, venues and tourism operators across Edinburgh and the Lothians",
    },
]

PAGE = """<!DOCTYPE html>
<html lang="en-GB">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Automation {name} | Done-For-You Business Automation — James Conn</title>
    <meta name="description" content="{meta}">
    <link rel="canonical" href="{base}/locations/ai-automation-{slug}.html">
    <meta property="og:type" content="website">
    <meta property="og:title" content="AI Automation for {name} Businesses — James Conn">
    <meta property="og:description" content="{meta}">
    <meta property="og:url" content="{base}/locations/ai-automation-{slug}.html">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/style.css">
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "ProfessionalService",
      "name": "James Conn — AI & Business Automation, {name}",
      "description": "Done-for-you AI automation and business process automation for businesses in {name}.",
      "url": "{base}/locations/ai-automation-{slug}.html",
      "founder": {{ "@type": "Person", "name": "James Conn" }},
      "areaServed": "{name}",
      "serviceType": ["AI Automation", "Business Process Automation", "Automated Reporting"]
    }}
    </script>
</head>
<body>

<nav class="lp-nav">
    <div class="lp-nav-inner">
        <a href="../index.html" class="lp-logo">James Conn</a>
        <div class="lp-nav-links">
            <a href="../index.html#offers">What I Do</a>
            <a href="../index.html#how">How It Works</a>
            <a href="../blog/index.html">Blog</a>
            <a href="../portfolio.html">Portfolio</a>
            <a href="#contact" class="btn-cta">Book Your Free Call</a>
        </div>
    </div>
</nav>

<!-- ═══════ HERO ═══════ -->
<header class="lp-hero">
    <div class="lp-wrap">
        <p class="lp-eyebrow">AI &amp; Business Automation · {name}</p>
        <h1>AI Automation For {name} Businesses.<br><em>Done For You.</em></h1>
        <p class="lp-sub">{intro}</p>
        <a href="#contact" class="btn-cta">Book Your Free Call</a>
        <a href="#local" class="btn-cta-ghost">Why {short}? &darr;</a>
        <p class="lp-trust">Built software used by real paying customers &middot; AI engineer at Golf.AI &middot; Ex-AI &amp; data consultant at a 30,000-person global consultancy</p>
    </div>
</header>

<!-- ═══════ WHAT I AUTOMATE ═══════ -->
<section class="lp-section" id="offers">
    <div class="lp-wrap">
        <p class="lp-eyebrow">What I Automate</p>
        <h2 class="lp-h2">The Hours {short} Businesses Lose Every Week — Handled By Software.</h2>
        <div class="lp-offer-grid">
            <div class="lp-offer-card">
                <span class="lp-offer-icon">&#129302;</span>
                <h3>AI Automations</h3>
                <ul>
                    <li>Enquiries answered in minutes, 24/7 — not the next working day</li>
                    <li>Quotes and proposals drafted automatically from your past pricing</li>
                    <li>Documents and emails read, summarised and filed by AI</li>
                </ul>
                <p class="lp-offer-outcome">Every lead answered before your competitors open their inbox.</p>
            </div>
            <div class="lp-offer-card">
                <span class="lp-offer-icon">&#9881;&#65039;</span>
                <h3>Business Process Automation</h3>
                <ul>
                    <li>Your systems connected — no more retyping data between them</li>
                    <li>Invoices raised, sent and chased automatically</li>
                    <li>Bookings, reminders and follow-ups that run themselves</li>
                </ul>
                <p class="lp-offer-outcome">The boring 20% of every job, gone for good.</p>
            </div>
            <div class="lp-offer-card">
                <span class="lp-offer-icon">&#128202;</span>
                <h3>Automated Reporting</h3>
                <ul>
                    <li>One report every Monday — sales, cash, jobs, pipeline</li>
                    <li>Data pulled automatically from all your systems</li>
                    <li>Alerts when something actually needs your attention</li>
                </ul>
                <p class="lp-offer-outcome">Run the business off numbers, not gut feel.</p>
            </div>
        </div>
    </div>
</section>

<!-- ═══════ LOCAL ═══════ -->
<section class="lp-section" id="local">
    <div class="lp-wrap">
        <p class="lp-eyebrow">{name}</p>
        <h2 class="lp-h2">Why {short} Businesses Are Automating Now.</h2>
        <p class="lp-lead">{local}</p>
        <p class="lp-lead">If you run one of the {industries} — and your week still involves retyping, chasing or copy-pasting — you are leaving hours on the table that software can do for a fraction of a wage.</p>
    </div>
</section>

<!-- ═══════ THE OFFER ═══════ -->
<section class="lp-section" id="plan">
    <div class="lp-wrap">
        <div class="lp-stack">
            <p class="lp-eyebrow">The Offer</p>
            <h3>The Free 30-Minute Automation Call</h3>
            <p class="lp-stack-sub">One call. Before you spend a penny, you'll know exactly what's worth automating in your {short} business and what it's costing you not to.</p>
            <ul>
                <li><strong>A 30-minute call about your business</strong> — {meeting_mode}. No prep needed on your side.</li>
                <li><strong>Your Time-Leak Report</strong> — sent after the call: your repetitive tasks, ranked by hours lost and what those hours cost per year.</li>
                <li><strong>A plain-English automation roadmap</strong> — what to automate first, second and third.</li>
            </ul>
            <div class="lp-guarantee">
                <strong>My promise:</strong> if I can't find at least 5 hours a week worth of automatable work in your business, I'll tell you straight — and you've lost nothing but half an hour. Everything I send you after the call is yours to keep.
            </div>
            <a href="#contact" class="btn-cta">Book Your Free Call</a>
        </div>
    </div>
</section>

<!-- ═══════ FAQ ═══════ -->
<section class="lp-section" id="faq">
    <div class="lp-wrap">
        <p class="lp-eyebrow">Questions</p>
        <h2 class="lp-h2">Common Questions From {short} Businesses.</h2>
        <div class="lp-faq">
            <details>
                <summary>Do you work with {short} businesses in person?</summary>
                <p>{in_person_answer}</p>
            </details>
            <details>
                <summary>What kind of {short} businesses benefit most from automation?</summary>
                <p>Any business where people spend hours on email, spreadsheets, quotes, bookings or invoices. In {short} that's especially the {industries}. If your team retypes information between systems, you have a time leak worth plugging.</p>
            </details>
            <details>
                <summary>How much does it cost?</summary>
                <p>It depends on what we automate — which is exactly why the first call is free. You'll know what's worth doing, what it costs and what it saves before committing to anything.</p>
            </details>
        </div>
    </div>

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {{"@type": "Question", "name": "Do you work with {short} businesses in person?", "acceptedAnswer": {{"@type": "Answer", "text": "{in_person_answer}"}}}},
        {{"@type": "Question", "name": "What kind of {short} businesses benefit most from AI automation?", "acceptedAnswer": {{"@type": "Answer", "text": "Any business where people spend hours on email, spreadsheets, quotes, bookings or invoices — in {short}, especially the {industries}."}}}},
        {{"@type": "Question", "name": "How much does AI automation cost?", "acceptedAnswer": {{"@type": "Answer", "text": "It depends on what is being automated, which is why the first call is free: you'll know what's worth doing, what it costs and what it saves before you commit to anything."}}}}
      ]
    }}
    </script>
</section>

<!-- ═══════ CONTACT ═══════ -->
<section class="lp-section" id="contact">
    <div class="lp-wrap">
        <p class="lp-eyebrow">Get Started</p>
        <h2 class="lp-h2">Tell Me What's Eating Your Week.</h2>
        <p class="lp-lead">Fill this in (60 seconds) and I'll reply within one working day to book your free 30-minute call. No pitch, no pressure.</p>
        <div class="lp-form-wrap">
            <form class="lp-form" action="https://formspree.io/f/xdavwqzr" method="POST">
                <div>
                    <label for="name">Your name</label>
                    <input type="text" id="name" name="name" required placeholder="Jane Smith">
                </div>
                <div>
                    <label for="business">Business name</label>
                    <input type="text" id="business" name="business" required placeholder="Smith & Sons Ltd">
                </div>
                <div>
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" required placeholder="jane@smithandsons.co.uk">
                </div>
                <div>
                    <label for="phone">Phone (optional)</label>
                    <input type="tel" id="phone" name="phone" placeholder="07123 456789">
                </div>
                <div>
                    <label for="message">What's the most repetitive, time-draining task in your business right now?</label>
                    <textarea id="message" name="message" rows="4" required placeholder="e.g. We retype every order from email into our system..."></textarea>
                </div>
                <input type="hidden" name="_subject" value="New free call request — {name}">
                <input type="hidden" name="location" value="{name}">
                <button type="submit" class="btn-cta">Send &mdash; Book My Free Call</button>
                <p class="lp-form-note">Your details go straight to me, James — not a sales team, because there isn't one.</p>
            </form>
        </div>
    </div>
</section>

<!-- ═══════ OTHER LOCATIONS ═══════ -->
<section class="lp-section" id="locations">
    <div class="lp-wrap">
        <p class="lp-eyebrow">Elsewhere</p>
        <h2 class="lp-h2">AI Automation Across The UK.</h2>
        <div class="lp-loc-grid">
{other_links}
        </div>
    </div>
</section>

<footer class="lp-footer">
    <div class="lp-footer-inner">
        <p>&copy; 2026 James Conn &middot; AI &amp; Business Automation, UK</p>
        <div class="lp-footer-links">
            <a href="../index.html">Home</a>
            <a href="../blog/index.html">Blog</a>
            <a href="../portfolio.html">Portfolio &amp; CV</a>
            <a href="https://linkedin.com/in/conn" target="_blank">LinkedIn</a>
            <a href="https://github.com/jconn5803" target="_blank">GitHub</a>
        </div>
    </div>
</footer>

</body>
</html>
"""

IN_PERSON_YES = ("Yes. I'm based in the North East, so for businesses in {short} and around {region} "
                 "the free 30-minute session can happen in person, at your premises, over a coffee. "
                 "The build itself happens wherever is most convenient.")
IN_PERSON_NO = ("The free 30-minute session happens over a video call, and the build is delivered fully remotely — "
                "scoped, documented and handed over the same way as for a business down the road. I'm based in the "
                "North East of England and work with businesses across the UK, including {short}.")


def main():
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "locations")
    os.makedirs(out_dir, exist_ok=True)

    for city in CITIES:
        others = [c for c in CITIES if c["slug"] != city["slug"]]
        other_links = "\n".join(
            '            <a href="ai-automation-{slug}.html" class="lp-loc-link">{name}</a>'.format(**c)
            for c in others
        ) + '\n            <a href="../index.html#locations" class="lp-loc-link">All locations &rarr;</a>'

        in_person_answer = (IN_PERSON_YES if city["in_person"] else IN_PERSON_NO).format(
            short=city["short"], region=city["region"])
        meeting_mode = ("in person if you're in or around {short}, or over a quick video call".format(**city)
                        if city["in_person"] else "over a quick video call")

        html = PAGE.format(
            base=BASE_URL,
            other_links=other_links,
            in_person_answer=in_person_answer,
            meeting_mode=meeting_mode,
            **city
        )
        path = os.path.join(out_dir, "ai-automation-{slug}.html".format(**city))
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
        print("wrote", path)


if __name__ == "__main__":
    main()
