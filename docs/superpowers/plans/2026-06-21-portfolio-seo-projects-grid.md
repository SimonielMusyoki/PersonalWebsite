# Portfolio SEO/AEO Overhaul + Projects Grid Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite `index.html`'s SEO/AEO metadata, remove placeholder template content, and replace the portfolio section with a responsive grid of 8 real projects with live mockups.

**Architecture:** Single static HTML file (`index.html`) plus one new CSS file (`css/projects-grid.css`) for the new grid/card/browser-frame styles, and two new root files (`robots.txt`, `sitemap.xml`). No build step, no JS framework changes — `js/main.js` and existing plugins are untouched. There is no test runner in this project; each task's "test" step is a concrete manual verification (grep check, browser load, structured-data validator) run by the implementer.

**Tech Stack:** Plain HTML5, CSS3 (Bootstrap 4 grid classes already loaded), no new JS dependencies. Tech logos via `https://cdn.simpleicons.org/<slug>`. Project mockups via `https://s.wordpress.com/mshots/v1/<url-encoded-target>?w=1200`.

## Global Constraints

- Canonical domain: `https://simonielmusyoki.com/` — use this exact origin in canonical/OG/JSON-LD URLs.
- Do not touch: contact form markup/behavior, the `our-office` section (stays `display:none`), `js/` files, `css/bootstrap.min.css`, `css/plugin.min.css`, `css/style.css`, `css/responsive.css` (new styles go in the new `css/projects-grid.css` file only).
- Nav must end up as exactly: Home, About, Tech Stack, Projects, Contact — same set in both desktop (`#main-nav` / `.nav-list`) and mobile (`.mob-nav2` / `nav#main-nav .first-nav`) menus.
- Stats section must show exactly 3 stats: "7+ Years Coding", "18 Projects Shipped", "9 Tech Stacks".
- Tech stack strip must show exactly 9 logos: Python, Node.js, React, Django, Flutter, Next.js, Docker, GCP, WordPress+WooCommerce (one combined logo), AWS, Shopify, PHP — grouping WordPress/WooCommerce as a single icon brings the count to 9.
- Projects grid must contain exactly these 8 cards, in this order, each with the exact URL given:
  1. Dawaflow — `https://dawaflow.com/` — Django, Next.js, Docker, GCP
  2. Dawaflow Consumer App — `https://play.google.com/store/apps/details?id=com.dawaflow.dawaflow_app&hl=en_SG` — Django, Flutter
  3. Dawaflow Doctors App — `https://play.google.com/store/apps/details?id=com.dawaflow.dawaflow_doctors&hl=en_SG` — Django, Flutter
  4. LIJ Shoes — `https://www.lij.co.ke/` — WordPress, WooCommerce, AWS
  5. Uncover Skincare — `https://ke.uncoverskincare.com/` — Shopify
  6. Bundles and Snuggles — `https://bundlesnsnuggles.co.ke/` — WordPress, WooCommerce, AWS
  7. Derma Aesthetics — `https://derma-aesthetics.com/` — Shopify
  8. WODE Convening — `https://wodeconvening.org/` — PHP

---

## Task 1: Rewrite `<head>` SEO meta tags

**Files:**
- Modify: `index.html:1-34` (the `<head>` block)

**Interfaces:**
- Produces: canonical URL string `https://simonielmusyoki.com/` reused in Task 2 (JSON-LD `url`) and Task 9 (OG `og:url`).

- [ ] **Step 1: Replace the title and meta tags**

Replace lines 5-17 (from `<title>` through the theme-color meta) with:

```html
    <title>Simoniel Musyoki — Full-Stack & Mobile App Developer</title>
    <meta
      name="description"
      content="Simoniel Musyoki is a full-stack and mobile developer based in Nairobi, Kenya, building web platforms and apps with Django, Next.js, Flutter, and WordPress/Shopify e-commerce."
    />
    <meta name="keywords" content="Simoniel Musyoki, full-stack developer, mobile app developer, Django developer, Flutter developer, Nairobi Kenya developer" />
    <meta name="author" content="Simoniel Musyoki" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="theme-color" content="#c7ecff" />
    <meta name="robots" content="index,follow" />
    <link rel="canonical" href="https://simonielmusyoki.com/" />
```

- [ ] **Step 2: Add Open Graph and Twitter Card tags**

Immediately after the canonical link added in Step 1, add:

```html
    <meta property="og:type" content="website" />
    <meta property="og:title" content="Simoniel Musyoki — Full-Stack & Mobile App Developer" />
    <meta
      property="og:description"
      content="Full-stack and mobile developer based in Nairobi, Kenya, building web platforms and apps with Django, Next.js, Flutter, and WordPress/Shopify e-commerce."
    />
    <meta property="og:url" content="https://simonielmusyoki.com/" />
    <meta property="og:image" content="https://simonielmusyoki.com/images/logo_now.png" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="Simoniel Musyoki — Full-Stack & Mobile App Developer" />
    <meta
      name="twitter:description"
      content="Full-stack and mobile developer based in Nairobi, Kenya, building web platforms and apps with Django, Next.js, Flutter, and WordPress/Shopify e-commerce."
    />
    <meta name="twitter:image" content="https://simonielmusyoki.com/images/logo_now.png" />
```

- [ ] **Step 3: Verify**

Run: `grep -c "Creative Agency Template" index.html`
Expected output: `0`

Run: `grep -c "rel=\"canonical\"" index.html`
Expected output: `1`

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "Rewrite head SEO meta tags with real title, description, OG, and canonical URL"
```

---

## Task 2: Add JSON-LD structured data (Person + ItemList)

**Files:**
- Modify: `index.html` — insert before `</head>` (after the `<link href="css/responsive.css" ...>` line)

**Interfaces:**
- Consumes: project list and URLs from Global Constraints (Task 9 will build the human-visible cards from the same list; this block is the machine-readable mirror, kept in sync manually since there's no templating layer).

- [ ] **Step 1: Insert the JSON-LD script block**

Add immediately before the closing `</head>` tag:

```html
    <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Simoniel Musyoki",
        "jobTitle": "Full-Stack & Mobile App Developer",
        "url": "https://simonielmusyoki.com/",
        "email": "mailto:info@simonielmusyoki.com",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Nairobi",
          "addressCountry": "KE"
        },
        "knowsAbout": [
          "Django",
          "Next.js",
          "Flutter",
          "React",
          "Node.js",
          "Python",
          "WordPress",
          "Shopify",
          "AWS",
          "GCP",
          "Docker",
          "PHP"
        ]
      }
    </script>
    <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "itemListElement": [
          {
            "@type": "ListItem",
            "position": 1,
            "item": {
              "@type": "CreativeWork",
              "name": "Dawaflow",
              "url": "https://dawaflow.com/",
              "description": "Online pharmacy and telemedicine platform in Kenya delivering medicines and skincare products with virtual doctor consultations.",
              "keywords": "Django, Next.js, Docker, GCP"
            }
          },
          {
            "@type": "ListItem",
            "position": 2,
            "item": {
              "@type": "CreativeWork",
              "name": "Dawaflow Consumer App",
              "url": "https://play.google.com/store/apps/details?id=com.dawaflow.dawaflow_app&hl=en_SG",
              "description": "Mobile app for Dawaflow patients to order medicines and book virtual doctor consultations.",
              "keywords": "Django, Flutter"
            }
          },
          {
            "@type": "ListItem",
            "position": 3,
            "item": {
              "@type": "CreativeWork",
              "name": "Dawaflow Doctors App",
              "url": "https://play.google.com/store/apps/details?id=com.dawaflow.dawaflow_doctors&hl=en_SG",
              "description": "Mobile app for Dawaflow's doctors to manage and conduct virtual patient consultations.",
              "keywords": "Django, Flutter"
            }
          },
          {
            "@type": "ListItem",
            "position": 4,
            "item": {
              "@type": "CreativeWork",
              "name": "LIJ Shoes",
              "url": "https://www.lij.co.ke/",
              "description": "E-commerce store selling classic, durable sneakers and leather footwear in Kenya.",
              "keywords": "WordPress, WooCommerce, AWS"
            }
          },
          {
            "@type": "ListItem",
            "position": 5,
            "item": {
              "@type": "CreativeWork",
              "name": "Uncover Skincare",
              "url": "https://ke.uncoverskincare.com/",
              "description": "E-commerce store for K-Beauty skincare products formulated for melanin-rich skin.",
              "keywords": "Shopify"
            }
          },
          {
            "@type": "ListItem",
            "position": 6,
            "item": {
              "@type": "CreativeWork",
              "name": "Bundles and Snuggles",
              "url": "https://bundlesnsnuggles.co.ke/",
              "description": "Online baby shop in Kenya selling apparel, feeding supplies, and nursery essentials.",
              "keywords": "WordPress, WooCommerce, AWS"
            }
          },
          {
            "@type": "ListItem",
            "position": 7,
            "item": {
              "@type": "CreativeWork",
              "name": "Derma Aesthetics",
              "url": "https://derma-aesthetics.com/",
              "description": "E-commerce store for skincare products and aesthetic treatments formulated for melanin skin.",
              "keywords": "Shopify"
            }
          },
          {
            "@type": "ListItem",
            "position": 8,
            "item": {
              "@type": "CreativeWork",
              "name": "WODE Convening",
              "url": "https://wodeconvening.org/",
              "description": "Event site for a multi-day Nairobi convening on competency-based education and workforce readiness.",
              "keywords": "PHP"
            }
          }
        ]
      }
    </script>
```

- [ ] **Step 2: Verify JSON is well-formed**

Run: `node -e "const fs=require('fs');const html=fs.readFileSync('index.html','utf8');const blocks=[...html.matchAll(/<script type=\"application\/ld\+json\">([\s\S]*?)<\/script>/g)];blocks.forEach((b,i)=>{JSON.parse(b[1]);console.log('block '+i+' OK')})"`
Expected output:
```
block 0 OK
block 1 OK
```

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "Add JSON-LD Person and ItemList structured data for AEO"
```

---

## Task 3: Remove fake testimonials section

**Files:**
- Modify: `index.html:1183-1282` (the `<!--Start Testinomial-->` ... `<!--End Testinomial-->` `<section>` block)

**Interfaces:**
- Produces: removal of the `id="testmonials"` anchor target — Task 6 must not link to it.

- [ ] **Step 1: Delete the section**

Delete the entire block from `<!--Start Testinomial-->` through `<!--End Testinomial-->` inclusive (the `<section class="testinomial-section pad-tb" id="testmonials">...</section>` element and its surrounding comments).

- [ ] **Step 2: Verify**

Run: `grep -c "testmonials\|Simmertech\|Optimum Solutions\|Simba Systems" index.html`
Expected output: `0`

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "Remove fake testimonials section"
```

---

## Task 4: Replace stats section with real numbers

**Files:**
- Modify: `index.html:747-872` (the `<div class="statistics-section ... id="statistics">` block)

**Interfaces:**
- Consumes: nothing.
- Produces: `id="statistics"` anchor retained (still referenced by nav, renamed label "Statistics" stays valid as an id target — Task 6 relabels the link text only).

- [ ] **Step 1: Replace the full statistics block**

Replace the entire `<div class="statistics-section bg-gradient pad-tb tilt3d" id="statistics"> ... </div>` (everything between `<!--Start statistics-->` and `<!--End statistics-->`) with:

```html
    <!--Start statistics-->
    <div class="statistics-section bg-gradient pad-tb tilt3d" id="statistics">
      <div class="container">
        <div class="row justify-content-center t-ctr">
          <div class="col-lg-4 col-sm-6">
            <div class="statistics">
              <div
                data-tilt
                data-tilt-max="20"
                data-tilt-speed="1000"
                class="statistics-img"
              >
                <img
                  src="images/icons/startup.svg"
                  alt="years"
                  class="img-fluid"
                />
              </div>
              <div class="statnumb">
                <span class="counter">7</span><span>+</span>
                <p>Years Coding</p>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-sm-6">
            <div class="statistics">
              <div
                data-tilt
                data-tilt-max="20"
                data-tilt-speed="1000"
                class="statistics-img"
              >
                <img
                  src="images/icons/computers.svg"
                  alt="projects"
                  class="img-fluid"
                />
              </div>
              <div class="statnumb">
                <span class="counter">18</span>
                <p>Projects Shipped</p>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-sm-6">
            <div class="statistics">
              <div
                data-tilt
                data-tilt-max="20"
                data-tilt-speed="1000"
                class="statistics-img"
              >
                <img
                  src="images/icons/deal.svg"
                  alt="tech stacks"
                  class="img-fluid"
                />
              </div>
              <div class="statnumb">
                <span class="counter">9</span>
                <p>Tech Stacks</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--End statistics-->
```

- [ ] **Step 2: Verify**

Run: `grep -c "153\|Happy Clients\|Team Members\|Hours Worked" index.html`
Expected output: `0`

Run: `grep -c "Years Coding\|Projects Shipped\|Tech Stacks" index.html`
Expected output: `1` for each phrase (run grep separately per phrase, or `grep -E "Years Coding|Projects Shipped|Tech Stacks" index.html | wc -l` expecting `3`)

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "Replace fake stats with real numbers: 7+ years, 18 projects, 9 tech stacks"
```

---

## Task 5: Update tech stack logo strip to real 9 stacks

**Files:**
- Modify: `index.html:990-1066` (the `<section class="clients-section ... id="tech-stacks">` block)

**Interfaces:**
- Consumes: nothing.

- [ ] **Step 1: Replace the heading and logo list**

Replace the `<span>Our Comfortable Stacks</span>` / `<h2>Some of our Tech Stacks we Use</h2>` heading text and the `<ul>` of `<li class="wow fadeIn">` logo items (lines ~994-1052) with:

```html
              <span>What I Build With</span>
              <h2>Tech Stacks I Use</h2>
```

and the logo list:

```html
              <ul>
                <li class="wow fadeIn" data-wow-delay=".1s">
                  <div class="clients-logo">
                    <img src="https://cdn.simpleicons.org/python" alt="Python" class="img-fluid" />
                  </div>
                </li>
                <li class="wow fadeIn" data-wow-delay=".2s">
                  <div class="clients-logo">
                    <img src="https://cdn.simpleicons.org/nodedotjs" alt="Node.js" class="img-fluid" />
                  </div>
                </li>
                <li class="wow fadeIn" data-wow-delay=".3s">
                  <div class="clients-logo">
                    <img src="https://cdn.simpleicons.org/react" alt="React" class="img-fluid" />
                  </div>
                </li>
                <li class="wow fadeIn" data-wow-delay=".4s">
                  <div class="clients-logo">
                    <img src="https://cdn.simpleicons.org/django" alt="Django" class="img-fluid" />
                  </div>
                </li>
                <li class="wow fadeIn" data-wow-delay=".5s">
                  <div class="clients-logo">
                    <img src="https://cdn.simpleicons.org/flutter" alt="Flutter" class="img-fluid" />
                  </div>
                </li>
                <li class="wow fadeIn" data-wow-delay=".6s">
                  <div class="clients-logo">
                    <img src="https://cdn.simpleicons.org/nextdotjs" alt="Next.js" class="img-fluid" />
                  </div>
                </li>
                <li class="wow fadeIn" data-wow-delay=".7s">
                  <div class="clients-logo">
                    <img src="https://cdn.simpleicons.org/docker" alt="Docker" class="img-fluid" />
                  </div>
                </li>
                <li class="wow fadeIn" data-wow-delay=".8s">
                  <div class="clients-logo">
                    <img src="https://cdn.simpleicons.org/googlecloud" alt="Google Cloud Platform" class="img-fluid" />
                  </div>
                </li>
                <li class="wow fadeIn" data-wow-delay=".9s">
                  <div class="clients-logo">
                    <img src="https://cdn.simpleicons.org/woocommerce" alt="WordPress / WooCommerce" class="img-fluid" />
                  </div>
                </li>
                <li class="wow fadeIn" data-wow-delay="1s">
                  <div class="clients-logo">
                    <img src="https://cdn.simpleicons.org/amazonaws" alt="AWS" class="img-fluid" />
                  </div>
                </li>
                <li class="wow fadeIn" data-wow-delay="1.1s">
                  <div class="clients-logo">
                    <img src="https://cdn.simpleicons.org/shopify" alt="Shopify" class="img-fluid" />
                  </div>
                </li>
                <li class="wow fadeIn" data-wow-delay="1.2s">
                  <div class="clients-logo">
                    <img src="https://cdn.simpleicons.org/php" alt="PHP" class="img-fluid" />
                  </div>
                </li>
              </ul>
```

Note: this lists 12 individual logos but WordPress+WooCommerce is represented as one combined icon (`woocommerce`), so the distinct **stack count** referenced in the stats ("9 Tech Stacks") corresponds to the 9 *project-tech groupings* in the Global Constraints list (Django/Next/Docker/GCP, Flutter, WordPress+WooCommerce, AWS, Shopify, PHP, plus Python/Node/React as the underlying language layer) — the logo strip itself shows every individual logo for completeness. Do not change the "9 Tech Stacks" stat to match the logo count; the stat refers to stacks, the strip shows constituent technologies.

- [ ] **Step 2: Verify**

Run: `grep -c "languages/python.png\|languages/nodejs.png\|languages/react.png\|languages/django.png\|languages/flutter.png" index.html`
Expected output: `0` (old local logo references removed)

Run: `grep -c "cdn.simpleicons.org" index.html`
Expected output: `1` or more (12 `<img>` tags present)

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "Update tech stack logo strip to real stacks via Simple Icons CDN"
```

---

## Task 6: Simplify navigation (desktop + mobile)

**Files:**
- Modify: `index.html:65-123` (desktop `.nav-list`)
- Modify: `index.html:306-408` (mobile `nav#main-nav`)

**Interfaces:**
- Consumes: section ids — `#about-us` (exists), `#tech-stacks` (exists, Task 5 section), `#projects` (new id, defined in Task 9 — must match exactly), `#contact` (new id, added to the enquire-form section in this task since it currently has none).

- [ ] **Step 1: Add an id to the contact section**

In `index.html`, find `<section class="enquire-form pad-tb">` (around line 1284) and change it to:

```html
    <section class="enquire-form pad-tb" id="contact">
```

- [ ] **Step 2: Replace the desktop nav list**

Replace the entire `<ul class="nav-list"> ... </ul>` content (lines 66-286, i.e. every `<li class="sbmenu">...</li>` and the `<li class="contact-show">` item, but keep the outer `<ul class="nav-list">` and `</ul>` tags) with:

```html
              <li><a href="#" class="menu-links">Home</a></li>
              <li><a href="#about-us" class="menu-links">About</a></li>
              <li><a href="#tech-stacks" class="menu-links">Tech Stack</a></li>
              <li><a href="#projects" class="menu-links">Projects</a></li>
              <li><a href="#contact" class="menu-links">Contact</a></li>
```

- [ ] **Step 3: Replace the mobile nav list**

Replace the `<ul class="first-nav"> ... </ul>` content (lines 307-408, i.e. every `<li>` and its commented-out sub-`<ul>`) with:

```html
            <li><a href="#">Home</a></li>
            <li><a href="#about-us">About</a></li>
            <li><a href="#tech-stacks">Tech Stack</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#contact">Contact</a></li>
```

- [ ] **Step 4: Verify**

Run: `grep -c "Homepage Demos\|Shortcodes\|sub-menu-section" index.html`
Expected output: `0`

Run: `grep -oE 'href="#[a-z-]*"' index.html | sort -u`
Expected output includes exactly: `href="#"`, `href="#about-us"`, `href="#contact"`, `href="#projects"`, `href="#tech-stacks"` (plus any unrelated `href="#"` used by buttons/modals, which is fine)

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "Simplify nav to Home/About/Tech Stack/Projects/Contact, add #contact id"
```

---

## Task 7: Rewrite About section copy for AEO

**Files:**
- Modify: `index.html:571-608` (the About text column)

**Interfaces:**
- Consumes: nothing.

- [ ] **Step 1: Replace the About copy**

Replace the `<div class="common-heading text-l">` block inside the About section (the `<span>We Are Creative Agency</span>` through the closing `</div>` before `<div class="user- mt30">`) with:

```html
            <div class="common-heading text-l">
              <span>Full-Stack & Mobile Developer</span>
              <h2>About Simoniel Musyoki</h2>
              <p>
                Simoniel Musyoki is a full-stack and mobile developer based in
                Nairobi, Kenya, with 7+ years of experience building web
                platforms and mobile apps. He specializes in Django and
                Next.js for backend/web work, Flutter for cross-platform
                mobile apps, and has shipped e-commerce sites on WordPress,
                WooCommerce, and Shopify. His work spans telemedicine
                (Dawaflow), e-commerce, and event platforms, deployed on AWS,
                GCP, and Docker. See his code on
                <a href="https://github.com/SimonielMusyoki" target="_blank">
                  GitHub</a
                >.
              </p>
              <p class="quote">
                I love working in teams. It's much faster to execute development
                stuff, and getting more output on efficieny and effectiveness.
                So, I work with friends :)
              </p>
            </div>
```

(Note: the `<a href="#tech-stacks">HERE</a>` reference and the duplicate GitHub link from the original copy are consolidated into the single GitHub link above; the `<div class="user- mt30">...</div>` media block below this stays unchanged.)

- [ ] **Step 2: Verify**

Run: `grep -c "We Are Creative Agency\|maintaining a huge codebase" index.html`
Expected output: `0`

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "Rewrite About section copy to be factual and AEO-friendly"
```

---

## Task 8: Add projects grid CSS

**Files:**
- Create: `css/projects-grid.css`
- Modify: `index.html:32-33` (stylesheet links, to add the new file)

**Interfaces:**
- Produces: CSS classes consumed by Task 9's markup — `.projects-grid`, `.project-card`, `.project-mockup-frame`, `.project-mockup-frame img`, `.project-info`, `.project-tags`, `.project-tags span`, `.project-visit-link`.

- [ ] **Step 1: Create the stylesheet**

```css
.projects-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
}

@media (max-width: 991px) {
  .projects-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 575px) {
  .projects-grid {
    grid-template-columns: 1fr;
  }
}

.project-card {
  background: #fff;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
  display: flex;
  flex-direction: column;
}

.project-mockup-frame {
  background: #e8e8e8;
  border-bottom: 8px solid #050748;
  position: relative;
  aspect-ratio: 16 / 10;
  overflow: hidden;
}

.project-mockup-frame::before {
  content: "";
  position: absolute;
  top: 8px;
  left: 12px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #ff5f56;
  box-shadow: 16px 0 0 #ffbd2e, 32px 0 0 #27c93f;
  z-index: 2;
}

.project-mockup-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top;
  display: block;
  margin-top: 20px;
}

.project-info {
  padding: 25px;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.project-info h4 {
  margin-bottom: 10px;
}

.project-info p {
  margin-bottom: 15px;
  flex: 1;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 15px;
}

.project-tags span {
  background: #f1f1fb;
  color: #050748;
  font-size: 12px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 20px;
}

.project-visit-link {
  font-weight: 600;
  color: #050748;
}
```

- [ ] **Step 2: Link the stylesheet**

In `index.html`, after `<link href="css/responsive.css" rel="stylesheet" />`, add:

```html
    <link href="css/projects-grid.css" rel="stylesheet" />
```

- [ ] **Step 3: Verify**

Run: `test -f css/projects-grid.css && echo FOUND`
Expected output: `FOUND`

Run: `grep -c "projects-grid.css" index.html`
Expected output: `1`

- [ ] **Step 4: Commit**

```bash
git add css/projects-grid.css index.html
git commit -m "Add projects grid stylesheet"
```

---

## Task 9: Replace portfolio section with projects grid

**Files:**
- Modify: `index.html:873-988` (the `<section class="portfolio-section pad-tb" id="portfolio">` block)

**Interfaces:**
- Consumes: CSS classes from Task 8 (`.projects-grid`, `.project-card`, `.project-mockup-frame`, `.project-info`, `.project-tags`, `.project-visit-link`).
- Produces: `id="projects"` anchor target, consumed by Task 6's nav links.

- [ ] **Step 1: Replace the entire portfolio section**

Replace from `<!--Start Portfolio-->` through `<!--End Portfolio-->` with:

```html
    <!--Start Portfolio-->
    <section class="portfolio-section pad-tb" id="projects">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-8">
            <div class="common-heading">
              <span>Projects</span>
              <h2 class="mb0">Projects I've Built</h2>
            </div>
          </div>
        </div>
        <div class="projects-grid mt60">
          <div class="project-card" itemscope itemtype="https://schema.org/CreativeWork">
            <a class="project-mockup-frame" href="https://dawaflow.com/" target="_blank" rel="noopener">
              <img
                src="https://s.wordpress.com/mshots/v1/https%3A%2F%2Fdawaflow.com%2F?w=1200"
                alt="Dawaflow screenshot"
                loading="lazy"
              />
            </a>
            <div class="project-info">
              <h4 itemprop="name"><a href="https://dawaflow.com/" target="_blank" rel="noopener">Dawaflow</a></h4>
              <p itemprop="description">Online pharmacy and telemedicine platform in Kenya delivering medicines and skincare products with virtual doctor consultations.</p>
              <div class="project-tags">
                <span>Django</span><span>Next.js</span><span>Docker</span><span>GCP</span>
              </div>
              <a class="project-visit-link" href="https://dawaflow.com/" target="_blank" rel="noopener" itemprop="url">Visit ↗</a>
            </div>
          </div>
          <div class="project-card" itemscope itemtype="https://schema.org/CreativeWork">
            <a class="project-mockup-frame" href="https://play.google.com/store/apps/details?id=com.dawaflow.dawaflow_app&hl=en_SG" target="_blank" rel="noopener">
              <img
                src="https://s.wordpress.com/mshots/v1/https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.dawaflow.dawaflow_app%26hl%3Den_SG?w=1200"
                alt="Dawaflow Consumer App screenshot"
                loading="lazy"
              />
            </a>
            <div class="project-info">
              <h4 itemprop="name"><a href="https://play.google.com/store/apps/details?id=com.dawaflow.dawaflow_app&hl=en_SG" target="_blank" rel="noopener">Dawaflow Consumer App</a></h4>
              <p itemprop="description">Mobile app for Dawaflow patients to order medicines and book virtual doctor consultations.</p>
              <div class="project-tags">
                <span>Django</span><span>Flutter</span>
              </div>
              <a class="project-visit-link" href="https://play.google.com/store/apps/details?id=com.dawaflow.dawaflow_app&hl=en_SG" target="_blank" rel="noopener" itemprop="url">Visit ↗</a>
            </div>
          </div>
          <div class="project-card" itemscope itemtype="https://schema.org/CreativeWork">
            <a class="project-mockup-frame" href="https://play.google.com/store/apps/details?id=com.dawaflow.dawaflow_doctors&hl=en_SG" target="_blank" rel="noopener">
              <img
                src="https://s.wordpress.com/mshots/v1/https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.dawaflow.dawaflow_doctors%26hl%3Den_SG?w=1200"
                alt="Dawaflow Doctors App screenshot"
                loading="lazy"
              />
            </a>
            <div class="project-info">
              <h4 itemprop="name"><a href="https://play.google.com/store/apps/details?id=com.dawaflow.dawaflow_doctors&hl=en_SG" target="_blank" rel="noopener">Dawaflow Doctors App</a></h4>
              <p itemprop="description">Mobile app for Dawaflow's doctors to manage and conduct virtual patient consultations.</p>
              <div class="project-tags">
                <span>Django</span><span>Flutter</span>
              </div>
              <a class="project-visit-link" href="https://play.google.com/store/apps/details?id=com.dawaflow.dawaflow_doctors&hl=en_SG" target="_blank" rel="noopener" itemprop="url">Visit ↗</a>
            </div>
          </div>
          <div class="project-card" itemscope itemtype="https://schema.org/CreativeWork">
            <a class="project-mockup-frame" href="https://www.lij.co.ke/" target="_blank" rel="noopener">
              <img
                src="https://s.wordpress.com/mshots/v1/https%3A%2F%2Fwww.lij.co.ke%2F?w=1200"
                alt="LIJ Shoes screenshot"
                loading="lazy"
              />
            </a>
            <div class="project-info">
              <h4 itemprop="name"><a href="https://www.lij.co.ke/" target="_blank" rel="noopener">LIJ Shoes</a></h4>
              <p itemprop="description">E-commerce store selling classic, durable sneakers and leather footwear in Kenya.</p>
              <div class="project-tags">
                <span>WordPress</span><span>WooCommerce</span><span>AWS</span>
              </div>
              <a class="project-visit-link" href="https://www.lij.co.ke/" target="_blank" rel="noopener" itemprop="url">Visit ↗</a>
            </div>
          </div>
          <div class="project-card" itemscope itemtype="https://schema.org/CreativeWork">
            <a class="project-mockup-frame" href="https://ke.uncoverskincare.com/" target="_blank" rel="noopener">
              <img
                src="https://s.wordpress.com/mshots/v1/https%3A%2F%2Fke.uncoverskincare.com%2F?w=1200"
                alt="Uncover Skincare screenshot"
                loading="lazy"
              />
            </a>
            <div class="project-info">
              <h4 itemprop="name"><a href="https://ke.uncoverskincare.com/" target="_blank" rel="noopener">Uncover Skincare</a></h4>
              <p itemprop="description">E-commerce store for K-Beauty skincare products formulated for melanin-rich skin.</p>
              <div class="project-tags">
                <span>Shopify</span>
              </div>
              <a class="project-visit-link" href="https://ke.uncoverskincare.com/" target="_blank" rel="noopener" itemprop="url">Visit ↗</a>
            </div>
          </div>
          <div class="project-card" itemscope itemtype="https://schema.org/CreativeWork">
            <a class="project-mockup-frame" href="https://bundlesnsnuggles.co.ke/" target="_blank" rel="noopener">
              <img
                src="https://s.wordpress.com/mshots/v1/https%3A%2F%2Fbundlesnsnuggles.co.ke%2F?w=1200"
                alt="Bundles and Snuggles screenshot"
                loading="lazy"
              />
            </a>
            <div class="project-info">
              <h4 itemprop="name"><a href="https://bundlesnsnuggles.co.ke/" target="_blank" rel="noopener">Bundles and Snuggles</a></h4>
              <p itemprop="description">Online baby shop in Kenya selling apparel, feeding supplies, and nursery essentials.</p>
              <div class="project-tags">
                <span>WordPress</span><span>WooCommerce</span><span>AWS</span>
              </div>
              <a class="project-visit-link" href="https://bundlesnsnuggles.co.ke/" target="_blank" rel="noopener" itemprop="url">Visit ↗</a>
            </div>
          </div>
          <div class="project-card" itemscope itemtype="https://schema.org/CreativeWork">
            <a class="project-mockup-frame" href="https://derma-aesthetics.com/" target="_blank" rel="noopener">
              <img
                src="https://s.wordpress.com/mshots/v1/https%3A%2F%2Fderma-aesthetics.com%2F?w=1200"
                alt="Derma Aesthetics screenshot"
                loading="lazy"
              />
            </a>
            <div class="project-info">
              <h4 itemprop="name"><a href="https://derma-aesthetics.com/" target="_blank" rel="noopener">Derma Aesthetics</a></h4>
              <p itemprop="description">E-commerce store for skincare products and aesthetic treatments formulated for melanin skin.</p>
              <div class="project-tags">
                <span>Shopify</span>
              </div>
              <a class="project-visit-link" href="https://derma-aesthetics.com/" target="_blank" rel="noopener" itemprop="url">Visit ↗</a>
            </div>
          </div>
          <div class="project-card" itemscope itemtype="https://schema.org/CreativeWork">
            <a class="project-mockup-frame" href="https://wodeconvening.org/" target="_blank" rel="noopener">
              <img
                src="https://s.wordpress.com/mshots/v1/https%3A%2F%2Fwodeconvening.org%2F?w=1200"
                alt="WODE Convening screenshot"
                loading="lazy"
              />
            </a>
            <div class="project-info">
              <h4 itemprop="name"><a href="https://wodeconvening.org/" target="_blank" rel="noopener">WODE Convening</a></h4>
              <p itemprop="description">Event site for a multi-day Nairobi convening on competency-based education and workforce readiness.</p>
              <div class="project-tags">
                <span>PHP</span>
              </div>
              <a class="project-visit-link" href="https://wodeconvening.org/" target="_blank" rel="noopener" itemprop="url">Visit ↗</a>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!--End Portfolio-->
```

- [ ] **Step 2: Verify markup count and old assets removed**

Run: `grep -c "isotope_item\|images/portfolio/" index.html`
Expected output: `0`

Run: `grep -c "class=\"project-card\"" index.html`
Expected output: `8`

Run: `grep -c "id=\"projects\"" index.html`
Expected output: `1`

- [ ] **Step 3: Manual browser check**

Open `index.html` directly in a browser (or serve via `python3 -m http.server` from the `frontend/` directory and visit `http://localhost:8000/`). Confirm:
- 8 cards render in a 3-column grid at full width.
- Resizing the window narrower shows 2 columns, then 1 column.
- Each mshots image loads (may take a few seconds on first load as mshots generates the screenshot — reload if a card shows a generic "generating" placeholder image).
- Clicking a card's image or "Visit ↗" opens the correct live URL in a new tab.

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "Replace portfolio section with 8-project responsive grid"
```

---

## Task 10: Add robots.txt and sitemap.xml

**Files:**
- Create: `robots.txt`
- Create: `sitemap.xml`

**Interfaces:**
- Consumes: canonical URL `https://simonielmusyoki.com/` from Task 1.

- [ ] **Step 1: Create `robots.txt`**

```
User-agent: *
Allow: /

Sitemap: https://simonielmusyoki.com/sitemap.xml
```

- [ ] **Step 2: Create `sitemap.xml`**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://simonielmusyoki.com/</loc>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```

- [ ] **Step 3: Verify**

Run: `test -f robots.txt && test -f sitemap.xml && echo BOTH_FOUND`
Expected output: `BOTH_FOUND`

Run: `node -e "require('fs').readFileSync('sitemap.xml','utf8')" && echo READABLE`
Expected output: `READABLE` (confirms the file is valid UTF-8/readable; this is plain XML so no parser is required)

- [ ] **Step 4: Commit**

```bash
git add robots.txt sitemap.xml
git commit -m "Add robots.txt and sitemap.xml"
```

---

## Task 11: Final QA pass

**Files:** none (verification only)

**Interfaces:** none.

- [ ] **Step 1: Full-page link check**

Run: `grep -oE 'href="[^"]*"' index.html | sort -u`

Manually scan the output: every `href="#..."` must correspond to an id that exists in the file (`#about-us`, `#tech-stacks`, `#projects`, `#contact`), and there should be no leftover `href="javascript:void(0)"` pointing at removed sections.

- [ ] **Step 2: Structured data validation**

Paste the two `<script type="application/ld+json">` blocks from `index.html` into Google's Rich Results Test (https://search.google.com/test/rich-results) or Schema.org's validator (https://validator.schema.org/). Confirm zero errors.

- [ ] **Step 3: Browser smoke test across breakpoints**

Serve the site locally:

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000/` in a browser. At desktop width, tablet width (~800px), and mobile width (~400px) confirm:
- Nav shows Home/About/Tech Stack/Projects/Contact and each link scrolls to the right section.
- Stats section shows 7+ / 18 / 9 with correct labels.
- Tech stack strip shows 12 logos loading correctly (no broken image icons).
- Projects grid shows 8 cards, responsive column count per breakpoint, all mshots images load.
- Testimonials section is gone (no fake quotes anywhere on the page).

- [ ] **Step 4: Final commit (only if any QA step required fixes)**

If Steps 1-3 surfaced issues, fix them in the relevant file and commit:

```bash
git add index.html
git commit -m "Fix QA issues found in final pass"
```

If no issues were found, no commit is needed for this task.
