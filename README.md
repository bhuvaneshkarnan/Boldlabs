# Boldlabs Studio — Pixel-Brutalist Dark Homepage

A premium, pixel-brutalist, and responsive single-page homepage for **Boldlabs Studio** (Bhuvanesh), a booking-first website design and automation service. Built using semantic, accessible HTML5, responsive vanilla CSS, and clean interaction scripts.

This visual design is derived directly from custom grid layouts, game-like stats cards, pixelated borders, and stark monochromatic contrasts.

---

## Visual Design System & Tokens

Our design tokens are declared as CSS custom variables in the `:root` element of `style.css`.

### 1. Typography
We use a clean, geometric developer font pairing:
- **Display Headings & Badges**: `Silkscreen` (Google Font) — An uppercase, geometric 8-bit pixel font that matches the retro-game header styling.
- **Body copy & UI**: `JetBrains Mono` (Google Font) — A clean, highly legible developer monospace font for code blocks, lists, and meta text.

### 2. Palette
A high-contrast monochromatic system with a dramatic section swap:
- **Main Theme (Dark)**:
  - Background: `#000000` (Pure pitch black)
  - Card Backgrounds: `#0C0C0C` (Off-black cards)
  - Text: `#FFFFFF` (Solid white)
  - Muted Text: `#8C8C8C` (Medium gray)
  - Borders & Lines: `#262626` (Thin gray grid outline)
- **Footer Swap Theme (Light)**:
  - Background: `#F5F5F3` (Light warm gray)
  - Text: `#000000`
  - Borders: `#D4D4D4`

### 3. Corners & Borders
- **Corners**: `0px` radius (perfectly sharp architectural borders).
- **Borders**: `1px solid var(--color-border)` outlines for elements, grids, and divider lines.
- **Testimonial Corners**: Testimonial quote cards feature custom corner decorations styled using inline repeating pixel patterns.

---

## Assets Reference

This site loads local assets situated in the root folder:
1. **[favicon.svg](file:///e:/Boldlabs%20Studio/favicon.svg)** — A custom pixel-brutalist favicon matching the studio branding.
2. **[shakanksh_portrait.png](file:///e:/Boldlabs%20Studio/shakanksh_portrait.png)** — High-contrast anime character portrait representing Bhuvanesh's stats card.
3. **[Works/](file:///e:/Boldlabs%20Studio/Works)** — A folder containing screenshots of real portfolio sites (180 Tattoo, Zyropets, Ze&Zow, RGHT Tax).

---

## Dynamic Interactivity

- **Interactive Card Stack**: In the **CLIENT REVIEWS** section, clicking any card updates the active layout. The active card (the Lead Architect stats profile card) scales up (`scale(1.05)`), shifts z-index, and updates to a dark color scheme while the inactive testimonial cards are styled with rotated perspectives, white backgrounds, and black text.
- **FAQ Accordion**: Got Questions accordion cards toggle open/close. Opening a row dynamically calculates and transition-scales the `max-height` for a smooth reveal, rotating the chevron arrow 90 degrees.
- **Floating Navigation Bar**: A floating light-mode pill-bar dynamically sticks to the top of the viewport.
- **Smooth Anchor Scrolling**: Supports smooth scroll target shifts with automatic keyboard focus management.

---

## Competitor-Aligned Integrations

Adapted from analyzing top B2B web agency competitors to maximize business trust and authority:
1. **Infinite Partner Marquee**: An auto-scrolling ticker below the hero section displaying partner brands (`ZYROPETS`, `HIIPOOH`, `FURORA`, `SWARNA IMPON`, `ZEZOW`, `AMIZHTHINI FOODS`, `180 TATTOO`, `DENTAL CARE`, `SMART PARKNGO`, `RGHT TAX`) rendered in high-contrast pixel typography, with a trust signal label above.
2. **Mission Timeline Section**: A dedicated 5-stage chronological grid layout representing the Boldlabs Studio project cycle.
3. **Value Delivered Checklist**: A dedicated objectives box inside the Case Studies detail panel outlining the solutions delivered (funnel tracking, simplified checkout, SMS reminders, CRM setups).
4. **The Solution Grid**: A 3-column pixel-brutalist grid outlining the core package: Booking-First Website, Reminders & Follow-Ups, and Monthly Subscription Care.
5. **Services Grid**: A separate 2x2 capabilities grid showcasing additional tailored offerings: Landing Pages, E-Commerce, AI Automations, and Whitelabel Partnerships.
6. **Sitemap & Legal Pages**: Full support for SEO crawlers via [sitemap.xml](file:///e:/Boldlabs%20Studio/sitemap.xml) and premium branded legal subpages ([terms.html](file:///e:/Boldlabs%20Studio/terms.html) and [privacy.html](file:///e:/Boldlabs%20Studio/privacy.html)).
