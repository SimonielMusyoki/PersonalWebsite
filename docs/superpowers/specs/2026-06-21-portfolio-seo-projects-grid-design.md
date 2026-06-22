# Portfolio SEO/AEO Overhaul + Projects Grid

## Context

`index.html` is a single-page static site built from a generic Bootstrap agency
template ("Niwax"). It still carries template placeholder content: fake
testimonials, fake stats, a "Creative Agency Template" meta description, dead
nav links, and a portfolio section of stock template images instead of real
projects. Domain: `https://simonielmusyoki.com/`.

## Goals

1. Make the page accurate and strong for traditional SEO and AEO (answer
   engines / LLM citation).
2. Replace the portfolio section with a real, responsive projects grid
   showing the 8 projects actually built, each with a live mockup.
3. Remove placeholder/fake content that undermines credibility (E-E-A-T).

## Out of scope

- No backend/CMS changes — site stays static HTML.
- Contact form (`action="#"`) is not wired up — flagged separately, not fixed
  here.
- "Our Office" / locations section stays `display:none`, untouched.

## 1. SEO foundation (`<head>`)

- Real `<title>`: reflects Simoniel Musyoki as a full-stack/mobile developer.
- Real `<meta name="description">`.
- `<link rel="canonical" href="https://simonielmusyoki.com/">`
- Open Graph + Twitter Card meta tags (title, description, image, url).
- `<meta name="robots" content="index,follow">`
- `robots.txt` and `sitemap.xml` added at the site root.

## 2. AEO (Answer Engine Optimization)

- JSON-LD `Person` schema: name, jobTitle, url, sameAs (GitHub, and any other
  profile links available).
- JSON-LD `ItemList` of the 8 projects (each as `CreativeWork`), so answer
  engines can directly enumerate "projects by Simoniel Musyoki".
- About section copy rewritten in clear, factual, third-person-citable
  sentences (who he is, where based, what he specializes in) rather than
  template marketing language.
- Each project description is a concrete, answerable statement: what it is,
  who it's for, what tech built it.

## 3. Content cleanup

- Remove the fake testimonials section (`#testmonials`) entirely.
- Replace the stats section with 3 real stats:
  - **7+** Years Coding
  - **18** Projects Shipped
  - **9** Tech Stacks
  (Drop "team members" / "hours worked" — solo portfolio, not an agency.)
- Tech stack logo strip updated to the real 9 stacks used across projects:
  Python, Node.js, React, Django, Flutter, Next.js, Docker, GCP,
  WordPress/WooCommerce (combined), AWS, Shopify, PHP — grouped so the strip
  shows exactly 9 logos. Logos sourced via `https://cdn.simpleicons.org/<slug>`
  (no local asset work required).
- Remove dead `#` anchor links and commented-out template nav markup
  (homepage-demo dropdowns, Pages/Shortcodes/Blog mobile menu remnants).

## 4. Navigation simplification

New nav, both desktop and mobile menus: **Home · About · Tech Stack ·
Projects · Contact**, each linking to a real section id that exists after
cleanup.

## 5. Projects grid

Replaces the current "Our Latest Creative Work" isotope section.

- CSS grid, responsive: 3 columns desktop → 2 tablet → 1 mobile.
- Section heading: "Projects I've Built" (first-person, factual).
- Each card:
  - Live mockup screenshot via WordPress mShots:
    `https://s.wordpress.com/mshots/v1/<url-encoded-project-url>?w=1200`,
    wrapped in a CSS-only browser-frame.
  - Project name.
  - 1-2 sentence description (drafted from reviewing each live site/listing).
  - Tech-stack tag pills.
  - "Visit ↗" link to the live URL / store listing, opens in a new tab.
  - `itemscope itemtype="https://schema.org/CreativeWork"` microdata as a
    fallback alongside the JSON-LD `ItemList`.
- The 8 projects, in order:
  1. Dawaflow — Django, Next.js, Docker, GCP — https://dawaflow.com/
  2. Dawaflow Consumer App — Django, Flutter — Google Play listing
  3. Dawaflow Doctors App — Django, Flutter — Google Play listing
  4. LIJ Shoes — WordPress, WooCommerce, AWS — https://www.lij.co.ke/
  5. Uncover Skincare — Shopify — https://ke.uncoverskincare.com/
  6. Bundles and Snuggles — WordPress, WooCommerce, AWS — https://bundlesnsnuggles.co.ke/
  7. Derma Aesthetics — Shopify — https://derma-aesthetics.com/
  8. WODE Convening — PHP — https://wodeconvening.org/

## Testing / QA approach

Since this is a static HTML/CSS site with no build step or test suite:

- Visual check in a browser at desktop, tablet, and mobile widths after
  changes (grid responsiveness, nav, stats, tech logos).
- Validate JSON-LD with a structured-data checker (e.g. paste into Google's
  Rich Results Test) for syntax correctness.
- Click through every nav link and project card link to confirm no dead
  anchors / 404s.
- Confirm mShots URLs render images for all 8 project links (Play Store
  listing pages included).
