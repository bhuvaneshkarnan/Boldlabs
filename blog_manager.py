import os
import json
from datetime import datetime, timedelta

workspace_root = os.path.dirname(os.path.abspath(__file__))
current_date = datetime.now()
start_date = datetime(2026, 6, 1)

def build_extended_answer(post, index):
    clean_title = post["title"]
    core_answer = post["answer"]
    category = post.get("category", "WEB DEVELOPMENT")
    
    if category == "WEB PERFORMANCE":
        intro_paragraph = f"When it comes to web performance, nothing frustrates potential clients more than a slow mobile page load. Let's examine the mechanics of <strong>{clean_title}</strong> and map out a lightweight solution to speed up your website."
    elif category == "LOCAL SEO":
        intro_paragraph = f"For local service businesses, visibility on Google Maps and search results directly determines how many new leads discover your brand. Let's break down the details of <strong>{clean_title}</strong> and outline a step-by-step optimization plan."
    elif category == "BOOKING CONVERSIONS":
        intro_paragraph = f"A high-converting website is all about removing scheduling friction and letting hot prospects book discovery calls instantly. Let's explore the mechanics of <strong>{clean_title}</strong> and look at how to optimize your conversion pipeline."
    elif category == "CUSTOM VS BUILDERS":
        intro_paragraph = f"Choosing the right web architecture—clean custom code versus bulky visual templates—makes a massive difference in your site's speed and security. Let's unpack the details of <strong>{clean_title}</strong> and build a better alternative."
    else: # AI DISCOVERY
        intro_paragraph = f"AI search engines and generative crawlers are changing how service agencies get discovered and cited online. Let's examine the guidelines for <strong>{clean_title}</strong> and look at how to configure your website for LLM discovery."

    # Dynamic Steps Generation from core_answer
    sentences = [s.strip() for s in core_answer.split(".") if len(s.strip()) > 10]
    steps_html = "<ul>"
    for s in sentences:
        words = s.split()
        if len(words) >= 2:
            key_phrase = " ".join(words[:2]).capitalize()
            rest = " ".join(words[2:])
            steps_html += f"<li><strong>{key_phrase}:</strong> {rest}.</li>"
        else:
            steps_html += f"<li>{s}.</li>"
    steps_html += "</ul>"
    
    b2b_text = f"For service providers targeting clients globally, resolving issues related to <strong>{clean_title.lower()}</strong> is a major competitive advantage. It directly increases user retention, builds immediate brand trust, and improves organic search acquisition rates."

    import random
    
    # Internal Linking Engine: Find 2 other posts in the same category
    related_html = ""
    same_category_posts = [p for p in ALL_POSTS_GLOBAL if p["category"] == category and p["slug"] != post["slug"]]
    if same_category_posts:
        selected = random.sample(same_category_posts, min(2, len(same_category_posts)))
        related_html = '<div class="related-posts" style="margin-top: var(--space-xl); padding-top: var(--space-md); border-top: 1px solid rgba(0,0,0,0.1);">'
        related_html += '<h3 style="font-size: 1.1rem; text-transform: uppercase; margin-bottom: var(--space-sm);">Continue Reading</h3>'
        related_html += '<ul style="list-style-type: none; padding: 0;">'
        for rel in selected:
            related_html += f'<li style="margin-bottom: 8px;">→ <a href="{rel["slug"]}.html" style="color: var(--color-text-dark); text-decoration: underline; font-weight: 600;">{rel["title"]}</a></li>'
        related_html += '</ul></div>'

    return f"""
    <p>{intro_paragraph}</p>

    <h2>The Core Issue: Expert Solution</h2>
    <p>{core_answer}</p>
    
    <h3>Actionable Steps to Resolve:</h3>
    {steps_html}

    <h2>The B2B Business Value</h2>
    <p>{b2b_text}</p>
    
    <p>
      If you need help auditing your website, setting up automated reminders, or configuring your AI indexes, Bhuvanesh Karnan and the Boldlabs Studio engineering team can build a custom, booking-first solution tailored to your service business goals.
    </p>
    
    {related_html}
    """

import json
json_path = os.path.join(workspace_root, "all_200_blogs.json")
with open(json_path, "r", encoding="utf-8") as jf:
    topics = json.load(jf)

posts = []
for i, topic in enumerate(topics):
    slug, title, category, question, answer = topic
    # Schedule frequency: 1 post every 3 days starting June 1, 2026
    pub_date = start_date + timedelta(days=i * 3)
    posts.append({
        "slug": slug,
        "title": title,
        "category": category,
        "date": pub_date.strftime("%Y-%m-%d"),
        "date_display": pub_date.strftime("%d %b %Y").upper(),
        "question": question,
        "answer": answer
    })

global ALL_POSTS_GLOBAL
ALL_POSTS_GLOBAL = posts

# Recreate the blog directory output
blog_dir = os.path.join(workspace_root, "blog")
os.makedirs(blog_dir, exist_ok=True)

# Master Blog Post Template
post_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-R792DJ9GDG"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-R792DJ9GDG');
  </script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{TITLE}} — Boldlabs Studio Blog</title>
  <meta name="description" content="{{DESCRIPTION}}">
  <link rel="canonical" href="https://goboldlabs.com/blog/{{SLUG}}.html">
  <link rel="icon" type="image/svg+xml" href="../favicon.svg">
  
  <!-- Google Fonts Preconnect and Load -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Silkscreen:wght@400;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../style.css">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://goboldlabs.com/blog/{{SLUG}}.html">
  <meta property="og:title" content="{{TITLE}} — Boldlabs Studio Blog">
  <meta property="og:description" content="{{DESCRIPTION}}">
  <meta property="og:image" content="https://goboldlabs.com/shakanksh_portrait.png">

  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="https://goboldlabs.com/blog/{{SLUG}}.html">
  <meta property="twitter:title" content="{{TITLE}} — Boldlabs Studio Blog">
  <meta property="twitter:description" content="{{DESCRIPTION}}">
  <meta property="twitter:image" content="https://goboldlabs.com/shakanksh_portrait.png">

  <!-- Blog Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "{{TITLE}}",
    "description": "{{DESCRIPTION}}",
    "image": "https://goboldlabs.com/shakanksh_portrait.png",
    "datePublished": "{{DATE}}T00:00:00Z",
    "dateModified": "{{DATE}}T00:00:00Z",
    "author": {
      "@type": "Person",
      "name": "Bhuvanesh Karnan",
      "url": "https://www.linkedin.com/in/bhuvaneshkarnan/"
    },
    "publisher": {
      "@type": "Organization",
      "name": "Boldlabs Studio",
      "logo": {
        "@type": "ImageObject",
        "url": "https://goboldlabs.com/favicon.svg"
      }
    },
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://goboldlabs.com/blog/{{SLUG}}.html"
    }
  }
  </script>

  <style>
    .subpage-hero {
      padding: var(--space-4xl) 0 var(--space-2xl);
      text-align: center;
      position: relative;
    }
    .back-home {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--color-text-muted);
      text-transform: uppercase;
      margin-bottom: var(--space-md);
      transition: color var(--transition-normal);
    }
    .back-home:hover {
      color: var(--color-text);
    }
    .blog-content {
      max-width: 720px;
      margin: 0 auto;
      font-family: var(--font-mono);
      font-size: 0.9rem;
      line-height: 1.8;
      color: var(--color-text-muted);
    }
    .blog-content h2, .blog-content h3 {
      color: var(--color-text);
      font-family: var(--font-display);
      text-transform: uppercase;
      margin: var(--space-xl) 0 var(--space-sm);
      line-height: 1.3;
    }
    .blog-content h2 {
      font-size: 1.4rem;
    }
    .blog-content h3 {
      font-size: 1.1rem;
    }
    .blog-content p {
      margin-bottom: var(--space-md);
    }
    .blog-content ul {
      margin-bottom: var(--space-md);
      padding-left: var(--space-lg);
    }
    .blog-content li {
      margin-bottom: var(--space-xs);
    }
    .q-box {
      border: 1.5px solid var(--color-text-dark);
      background: var(--color-bg-card);
      padding: var(--space-md);
      margin-bottom: var(--space-lg);
      font-family: var(--font-mono);
    }
  </style>
</head>
<body>

  <!-- Floating Navigation Bar -->
  <nav class="navbar" aria-label="Main Navigation">
    <a href="../index.html#home" class="navbar-brand">Boldlabs Studio</a>
    
    <button class="nav-toggle" aria-label="Toggle Menu" aria-expanded="false" id="menu-toggle-btn">
      <span>MENU</span>
      <span class="menu-icon">☰</span>
    </button>
    
    <div class="nav-links" id="navbar-links-container">
      <span class="navbar-divider" aria-hidden="true">|</span>
      <a href="../index.html#services">Services</a>
      <span class="navbar-divider" aria-hidden="true">|</span>
      <a href="../index.html#latest-drop">Missions</a>
      <span class="navbar-divider" aria-hidden="true">|</span>
      <a href="../index.html#timeline">Timeline</a>
      <span class="navbar-divider" aria-hidden="true">|</span>
      <a href="../index.html#player">Reviews</a>
      <span class="navbar-divider" aria-hidden="true">|</span>
      <a href="../index.html#plans">Package</a>
      <span class="navbar-divider" aria-hidden="true">|</span>
      <a href="../blog.html">Blog</a>
      <span class="navbar-divider" aria-hidden="true">|</span>
      <a href="../index.html#build-together">Book Call</a>
    </div>
  </nav>

  <main id="main-content">
    
    <!-- Subpage Hero -->
    <section class="subpage-hero">
      <div class="container">
        <a href="../blog.html" class="back-home">← Back to Blog</a>
        <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--color-text-muted); display: block; margin-bottom: 8px; text-transform: uppercase;">{{DATE_DISPLAY}} · {{CATEGORY}}</span>
        <h1 style="font-size: clamp(2rem, 5vw, 3rem); line-height: 1.2; margin-bottom: var(--space-sm); text-transform: uppercase; color: var(--color-text);">{{TITLE}}</h1>
        <p style="color: var(--color-text-muted); max-width: 600px; margin: 0 auto; font-size: 0.9rem; font-family: var(--font-mono);">
          Written by Bhuvanesh Karnan · Founder & Developer
        </p>
      </div>
    </section>

    <!-- Post Body -->
    <section class="section">
      <div class="container">
        <article class="blog-content">
          <div class="q-box">
            <strong style="color: var(--color-text); text-transform: uppercase; display: block; margin-bottom: var(--space-xs);">User Question:</strong>
            <p style="margin: 0; font-style: italic;">"{{QUESTION}}"</p>
          </div>
          
          <h2>Expert Solution</h2>
          {{ANSWER}}
        </article>
      </div>
    </section>

    <!-- Lead Capture Section -->
    <section id="build-together" class="section section-light" style="background-color: var(--color-bg-light); color: var(--color-text-dark); border-top: 1px dashed rgba(0,0,0,0.15);">
      <div class="container" style="max-width: 600px;">
        <span class="section-subtitle" style="color: var(--color-muted-light); font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase; display: block; margin-bottom: var(--space-xs); font-family: var(--font-mono); text-align: center;">Ready to scale your bookings?</span>
        <h2 class="build-title" style="text-align: center; margin-bottom: var(--space-xs); font-size: 2.2rem;">START A PROJECT.</h2>
        <p class="build-desc" style="text-align: center; color: var(--color-muted-light); margin-bottom: var(--space-lg); font-size: 0.9rem;">
          Tell Bhuvanesh about your business and goals. We'll outline a plan for your custom build and booking automation flow.
        </p>

        <!-- Capture Form -->
        <form id="lead-capture-form" style="display: flex; flex-direction: column; gap: var(--space-md);">
          <div style="display: flex; flex-direction: column; gap: var(--space-xs);">
            <label for="lead-name" style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">Your Name</label>
            <input type="text" id="lead-name" required placeholder="e.g. John Doe" style="width: 100%; padding: 12px; border: 1.5px solid var(--color-text-dark); font-family: var(--font-mono); font-size: 0.85rem; background: #ffffff; color: #000000; outline: none; border-radius: 0; box-sizing: border-box;">
          </div>
          
          <div style="display: flex; flex-direction: column; gap: var(--space-xs);">
            <label for="lead-email" style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">Email Address</label>
            <input type="email" id="lead-email" required placeholder="e.g. john@example.com" style="width: 100%; padding: 12px; border: 1.5px solid var(--color-text-dark); font-family: var(--font-mono); font-size: 0.85rem; background: #ffffff; color: #000000; outline: none; border-radius: 0; box-sizing: border-box;">
          </div>

          <div style="display: flex; flex-direction: column; gap: var(--space-xs);">
            <label for="lead-whatsapp" style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">WhatsApp Number</label>
            <div style="display: flex; gap: var(--space-xs);">
              <select id="lead-country-code" aria-label="Country Code" required style="width: 110px; padding: 12px; border: 1.5px solid var(--color-text-dark); font-family: var(--font-mono); font-size: 0.85rem; background: #ffffff; color: #000000; outline: none; border-radius: 0; cursor: pointer; -webkit-appearance: none; -moz-appearance: none; appearance: none; background-image: url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22currentColor%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22><polyline points=%226 9 12 15 18 9%22></polyline></svg>'); background-repeat: no-repeat; background-position: right 8px center; background-size: 14px; box-sizing: border-box;">
                <!-- Initialized in JS -->
              </select>
              <input type="tel" id="lead-whatsapp" required placeholder="99999 99999" pattern="[0-9\s-]{7,15}" style="flex: 1; padding: 12px; border: 1.5px solid var(--color-text-dark); font-family: var(--font-mono); font-size: 0.85rem; background: #ffffff; color: #000000; outline: none; border-radius: 0; box-sizing: border-box;">
            </div>
          </div>
          
          <div style="display: flex; flex-direction: column; gap: var(--space-xs);">
            <label for="lead-contact-method" style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">How should we contact you?</label>
            <select id="lead-contact-method" aria-label="Contact Method" required style="width: 100%; padding: 12px; border: 1.5px solid var(--color-text-dark); font-family: var(--font-mono); font-size: 0.85rem; background: #ffffff; color: #000000; outline: none; border-radius: 0; cursor: pointer; -webkit-appearance: none; -moz-appearance: none; appearance: none; background-image: url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22currentColor%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22><polyline points=%226 9 12 15 18 9%22></polyline></svg>'); background-repeat: no-repeat; background-position: right 12px center; background-size: 16px;">
              <option value="WhatsApp">Contact me via WhatsApp</option>
              <option value="Email">Contact me via Email</option>
            </select>
          </div>
          
          <div style="display: flex; flex-direction: column; gap: var(--space-xs);">
            <label for="lead-question" style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">What do you need help with?</label>
            <textarea id="lead-question" required rows="3" placeholder="e.g. Interested in booking automation and custom web design." style="width: 100%; padding: 12px; border: 1.5px solid var(--color-text-dark); font-family: var(--font-mono); font-size: 0.85rem; background: #ffffff; color: #000000; outline: none; border-radius: 0; resize: vertical;"></textarea>
          </div>
          
          <button type="submit" class="pill-btn pill-btn-primary" style="margin-top: 8px; width: 100%; text-align: center; border-radius: 0; border: 2px solid var(--color-text-dark); cursor: pointer; display: block;">
            SUBMIT REQUEST
          </button>
        </form>
        <div id="lead-form-status" style="display: none; text-align: center; padding: var(--space-lg); font-family: var(--font-mono);">
          <span style="font-family: var(--font-display); font-size: 1.1rem; color: #008000; display: block; margin-bottom: 8px;">REQUEST SUBMITTED.</span>
          <p id="lead-status-msg" style="font-size: 0.8rem; line-height: 1.5; color: var(--color-text-dark); max-width: 500px; margin: 0 auto;">
            Thank you! Your request has been sent. Bhuvanesh will get back to you shortly.
          </p>
        </div>
      </div>
    </section>

  </main>

  <!-- Footer -->
  <footer class="main-footer">
    <div class="container">
      <div class="footer-grid">
        <!-- Column 1: Brand -->
        <div class="footer-brand-col">
          <div class="footer-logo">Boldlabs Studio</div>
          <p class="footer-tagline">Booking-first websites for service businesses.</p>
          <div class="footer-socials">
            <a href="https://www.linkedin.com/in/bhuvaneshkarnan/" target="_blank" rel="noopener" title="Bhuvanesh Karnan on LinkedIn">LinkedIn</a>
          </div>
        </div>

        <!-- Column 2: Navigation -->
        <div>
          <h3 class="footer-col-title">Navigation</h3>
          <ul class="footer-links">
            <li><a href="../index.html#services">Services</a></li>
            <li><a href="../index.html#latest-drop">Case Studies</a></li>
            <li><a href="../index.html#timeline">Process</a></li>
            <li><a href="../index.html#player">About</a></li>
          </ul>
        </div>

        <!-- Column 3: Trust -->
        <div>
          <h3 class="footer-col-title">Trust</h3>
          <ul class="footer-links">
            <li><a href="../index.html#player">Wall of Love</a></li>
            <li><a href="../blog.html">Blog</a></li>
            <li><a href="../index.html#build-together">Contact</a></li>
            <li><a href="../index.html#build-together">Book a Call</a></li>
          </ul>
        </div>

        <!-- Column 4: Legal -->
        <div>
          <h3 class="footer-col-title">Legal</h3>
          <ul class="footer-links">
            <li><a href="../terms.html">Terms</a></li>
            <li><a href="../privacy.html">Privacy</a></li>
            <li><span style="font-size: 0.75rem; color: rgba(0, 0, 0, 0.85); display: block; margin-top: 4px;">hello@boldlabs.studio</span></li>
          </ul>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="footer-bottom">
        <div class="container" style="padding: 0; width: 100%; display: flex; justify-content: space-between; align-items: center;">
          <span>© 2026 Boldlabs Studio — Bhuvanesh. All rights reserved.</span>
          <span style="font-family: var(--font-display); font-size: 0.7rem;">PROTAGONIST LOADED</span>
        </div>
      </div>
    </div>
  </footer>

  <!-- Global Configurations -->
  <script src="../firebase-config.js" defer></script>
  <!-- EmailJS SDK -->
  <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js" defer></script>

  <!-- Interactive Logic -->
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      // Mobile navigation menu toggle
      const toggleBtn = document.getElementById('menu-toggle-btn');
      const linksContainer = document.getElementById('navbar-links-container');
      
      if (toggleBtn && linksContainer) {
        toggleBtn.addEventListener('click', () => {
          const expanded = toggleBtn.getAttribute('aria-expanded') === 'true';
          toggleBtn.setAttribute('aria-expanded', !expanded);
          linksContainer.classList.toggle('active');
        });
      }

      // Initialize country codes in select element
      const countryCodeSelect = document.getElementById('lead-country-code');
      if (countryCodeSelect) {
        const countries = [
          { code: '91', name: 'IN' },
          { code: '1', name: 'US' },
          { code: '1', name: 'CA' },
          { code: '44', name: 'GB' },
          { code: '61', name: 'AU' },
          { code: '971', name: 'AE' },
          { code: '65', name: 'SG' }
        ];
        countryCodeSelect.innerHTML = '';
        countries.forEach(country => {
          const opt = document.createElement('option');
          opt.value = country.code;
          opt.textContent = `${country.name} (+${country.code})`;
          countryCodeSelect.appendChild(opt);
        });
      }

      // Contact form submit logic
      const leadForm = document.getElementById('lead-capture-form');
      const leadFormStatus = document.getElementById('lead-form-status');
      
      const isGoogleSheetConfigured = typeof firebaseConfig !== 'undefined' && firebaseConfig.googleSheetUrl;
      const isEmailjsConfigured = typeof emailjsConfig !== 'undefined' && emailjsConfig.publicKey !== "YOUR_PUBLIC_KEY";

      if (leadForm && leadFormStatus) {
        if (typeof emailjs !== 'undefined' && isEmailjsConfigured) {
          emailjs.init(emailjsConfig.publicKey);
        }

        leadForm.addEventListener('submit', async (e) => {
          e.preventDefault();
          const name = document.getElementById('lead-name').value.trim();
          const email = document.getElementById('lead-email').value.trim();
          const countryCode = document.getElementById('lead-country-code').value;
          const rawWhatsapp = document.getElementById('lead-whatsapp').value.trim();
          const question = document.getElementById('lead-question').value.trim();
          const contactMethod = document.getElementById('lead-contact-method').value;
          const timestamp = new Date().toISOString();
          
          const cleanPhone = rawWhatsapp.replace(/[^0-9]/g, '');
          const cleanWhatsappNumber = `${countryCode}${cleanPhone}`;
          const leadWhatsappLink = `https://wa.me/${cleanWhatsappNumber}`;
          const formattedWhatsapp = `+${countryCode} ${rawWhatsapp}`;

          const leadData = {
            name,
            email,
            whatsapp: formattedWhatsapp,
            contactMethod,
            question,
            sourcePage: 'Blog Post - {{SLUG}}',
            timestamp
          };

          try {
            // Save lead locally to localStorage
            const mockLeads = JSON.parse(localStorage.getItem('boldlabs_mock_leads') || '[]');
            mockLeads.push(leadData);
            localStorage.setItem('boldlabs_mock_leads', JSON.stringify(mockLeads));

            // Save to Google Sheets
            if (isGoogleSheetConfigured) {
              const formData = new URLSearchParams();
              formData.append('name', name);
              formData.append('email', email);
              formData.append('whatsapp', formattedWhatsapp);
              formData.append('contactMethod', contactMethod);
              formData.append('question', question);
              formData.append('sourcePage', 'Blog Post - {{SLUG}}');
              
              try {
                await fetch(firebaseConfig.googleSheetUrl, {
                  method: 'POST',
                  mode: 'no-cors',
                  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                  body: formData.toString()
                });
                console.log("Lead successfully dispatched to Google Sheets Apps Script.");
              } catch (err) {
                console.error("Error dispatching to Google Sheets:", err);
              }
            }

            // EmailJS trigger
            if (typeof emailjs !== 'undefined' && isEmailjsConfigured) {
              emailjs.send(emailjsConfig.serviceId, emailjsConfig.templateId, {
                lead_name: name,
                lead_email: email,
                lead_whatsapp: formattedWhatsapp,
                lead_contact_method: contactMethod,
                lead_question: question,
                lead_whatsapp_link: leadWhatsappLink
              });
            }

            const statusMsg = document.getElementById('lead-status-msg');
            if (contactMethod === 'WhatsApp') {
              const whatsappText = `Hi Boldlabs Studio, I would like to request a discovery call from your Blog post page.\n\n*Name*: ${name}\n*Email*: ${email}\n*WhatsApp*: ${formattedWhatsapp}\n*Details*: ${question}`;
              const whatsappUrl = `https://wa.me/${emailjsConfig.yourWhatsappNumber || '918870341570'}?text=${encodeURIComponent(whatsappText)}`;
              window.open(whatsappUrl, '_blank');
              if (statusMsg) {
                statusMsg.textContent = "Thank you! We've opened a new window to chat on WhatsApp. Please send the pre-filled message to connect with us instantly.";
              }
            } else {
              if (statusMsg) {
                statusMsg.textContent = `Thank you! Your request has been sent, and a confirmation email has been dispatched to ${email}. Bhuvanesh will review your request and get back to you shortly.`;
              }
            }

            leadForm.style.display = 'none';
            leadFormStatus.style.display = 'block';
          } catch (error) {
            console.error("Error capturing lead:", error);
            alert("Error sending request. Please email directly to hello@boldlabs.studio");
          }
        });
      }
    });
  </script>
</body>
</html>
"""

# Re-write the 100 posts files
published_posts = []
future_posts = []

for i, post in enumerate(posts):
    # Render post file content
    rendered = post_template
    rendered = rendered.replace("{{TITLE}}", post["title"])
    rendered = rendered.replace("{{DESCRIPTION}}", post["question"][:150] + "...")
    rendered = rendered.replace("{{SLUG}}", post["slug"])
    rendered = rendered.replace("{{CATEGORY}}", post["category"])
    rendered = rendered.replace("{{DATE}}", post["date"])
    rendered = rendered.replace("{{DATE_DISPLAY}}", post["date_display"])
    rendered = rendered.replace("{{QUESTION}}", post["question"])
    rendered = rendered.replace("{{ANSWER}}", build_extended_answer(post, i))
    
    file_path = os.path.join(blog_dir, f"{post['slug']}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(rendered)
        
    post_date_parsed = datetime.strptime(post["date"], "%Y-%m-%d")
    if post_date_parsed <= current_date:
        published_posts.append(post)
    else:
        future_posts.append(post)

# Export blog/posts.json for client-side dynamic loading
posts_json_path = os.path.join(blog_dir, "posts.json")
with open(posts_json_path, "w", encoding="utf-8") as pf:
    json.dump(posts, pf, indent=2)

# Print stats
print(f"Generated {len(posts)} blog post HTML files.")
print(f"Generated blog/posts.json index.")
print(f"Active (Published) Posts: {len(published_posts)}")
print(f"Scheduled (Future) Posts: {len(future_posts)}")

# 1. Regenerate blog.html listing page
blog_home_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-R792DJ9GDG"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-R792DJ9GDG');
  </script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Boldlabs Studio Blog — Web Design, SEO & Operations Automation Insights</title>
  <meta name="description" content="Read our latest engineering logs and strategic guides on booking-first web design, speed-optimized tech stacks (React & WordPress), local SEO, and AI automations.">
  <link rel="canonical" href="https://goboldlabs.com/blog.html">
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  
  <!-- Google Fonts Preconnect and Load -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Silkscreen:wght@400;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://goboldlabs.com/blog.html">
  <meta property="og:title" content="Boldlabs Studio Blog — Web Design, SEO & Automation Insights">
  <meta property="og:description" content="Read our latest engineering logs and strategic guides on booking-first web design, speed-optimized tech stacks, local SEO, and AI automations.">
  <meta property="og:image" content="https://goboldlabs.com/shakanksh_portrait.png">

  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="https://goboldlabs.com/blog.html">
  <meta property="twitter:title" content="Boldlabs Studio Blog — Web Design, SEO & Automation Insights">
  <meta property="twitter:description" content="Read our latest engineering logs and strategic guides on booking-first web design, speed-optimized tech stacks, local SEO, and AI automations.">
  <meta property="twitter:image" content="https://goboldlabs.com/shakanksh_portrait.png">

  <style>
    .subpage-hero {
      padding: var(--space-4xl) 0 var(--space-2xl);
      text-align: center;
      position: relative;
    }
    .back-home {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--color-text-muted);
      text-transform: uppercase;
      margin-bottom: var(--space-md);
      transition: color var(--transition-normal);
    }
    .back-home:hover {
      color: var(--color-text);
    }
    .features-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: var(--space-lg);
      margin-top: var(--space-xl);
    }
    @media (max-width: 992px) {
      .features-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }
    @media (max-width: 768px) {
      .features-grid {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>

  <!-- Floating Navigation Bar -->
  <nav class="navbar" aria-label="Main Navigation">
    <a href="index.html#home" class="navbar-brand">Boldlabs Studio</a>
    
    <button class="nav-toggle" aria-label="Toggle Menu" aria-expanded="false" id="menu-toggle-btn">
      <span>MENU</span>
      <span class="menu-icon">☰</span>
    </button>
    
    <div class="nav-links" id="navbar-links-container">
      <span class="navbar-divider" aria-hidden="true">|</span>
      <a href="index.html#services">Services</a>
      <span class="navbar-divider" aria-hidden="true">|</span>
      <a href="index.html#latest-drop">Missions</a>
      <span class="navbar-divider" aria-hidden="true">|</span>
      <a href="index.html#timeline">Timeline</a>
      <span class="navbar-divider" aria-hidden="true">|</span>
      <a href="index.html#player">Reviews</a>
      <span class="navbar-divider" aria-hidden="true">|</span>
      <a href="index.html#plans">Package</a>
      <span class="navbar-divider" aria-hidden="true">|</span>
      <a href="blog.html">Blog</a>
      <span class="navbar-divider" aria-hidden="true">|</span>
      <a href="index.html#build-together">Book Call</a>
    </div>
  </nav>

  <main id="main-content">
    
    <!-- Subpage Hero -->
    <section class="subpage-hero">
      <div class="container">
        <a href="index.html" class="back-home">← Back to Home</a>
        <h1 style="font-size: clamp(2.5rem, 6vw, 4rem); line-height: 1.1; margin-bottom: var(--space-sm);">THE BLOG</h1>
        <p style="color: var(--color-text-muted); max-width: 650px; margin: 0 auto; font-size: 0.95rem; line-height: 1.6;">
          Strategic guides, engineering logs, and insights on web design, local SEO, and operational scheduling automation.
        </p>
      </div>
    </section>

    <!-- Blog Posts Grid Section -->
    <section class="section">
      <div class="container">
        <h2 style="font-size: 1.5rem; margin-bottom: var(--space-md); text-transform: uppercase;">LATEST MISSIONS ({{PUBLISHED_COUNT}})</h2>
        <div class="features-grid">
          {{BLOG_CARDS}}
        </div>
      </div>
    </section>

    <!-- Lead Capture Section -->
    <section id="build-together" class="section section-light" style="background-color: var(--color-bg-light); color: var(--color-text-dark); border-top: 1px dashed rgba(0,0,0,0.15);">
      <div class="container" style="max-width: 600px;">
        <span class="section-subtitle" style="color: var(--color-muted-light); font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase; display: block; margin-bottom: var(--space-xs); font-family: var(--font-mono); text-align: center;">Ready to scale your bookings?</span>
        <h2 class="build-title" style="text-align: center; margin-bottom: var(--space-xs); font-size: 2.2rem;">START A PROJECT.</h2>
        <p class="build-desc" style="text-align: center; color: var(--color-muted-light); margin-bottom: var(--space-lg); font-size: 0.9rem;">
          Tell Bhuvanesh about your business and goals. We'll outline a plan for your custom build and booking automation flow.
        </p>

        <!-- Capture Form -->
        <form id="lead-capture-form" style="display: flex; flex-direction: column; gap: var(--space-md);">
          <div style="display: flex; flex-direction: column; gap: var(--space-xs);">
            <label for="lead-name" style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">Your Name</label>
            <input type="text" id="lead-name" required placeholder="e.g. John Doe" style="width: 100%; padding: 12px; border: 1.5px solid var(--color-text-dark); font-family: var(--font-mono); font-size: 0.85rem; background: #ffffff; color: #000000; outline: none; border-radius: 0; box-sizing: border-box;">
          </div>
          
          <div style="display: flex; flex-direction: column; gap: var(--space-xs);">
            <label for="lead-email" style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">Email Address</label>
            <input type="email" id="lead-email" required placeholder="e.g. john@example.com" style="width: 100%; padding: 12px; border: 1.5px solid var(--color-text-dark); font-family: var(--font-mono); font-size: 0.85rem; background: #ffffff; color: #000000; outline: none; border-radius: 0; box-sizing: border-box;">
          </div>

          <div style="display: flex; flex-direction: column; gap: var(--space-xs);">
            <label for="lead-whatsapp" style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">WhatsApp Number</label>
            <div style="display: flex; gap: var(--space-xs);">
              <select id="lead-country-code" aria-label="Country Code" required style="width: 110px; padding: 12px; border: 1.5px solid var(--color-text-dark); font-family: var(--font-mono); font-size: 0.85rem; background: #ffffff; color: #000000; outline: none; border-radius: 0; cursor: pointer; -webkit-appearance: none; -moz-appearance: none; appearance: none; background-image: url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22currentColor%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22><polyline points=%226 9 12 15 18 9%22></polyline></svg>'); background-repeat: no-repeat; background-position: right 8px center; background-size: 14px; box-sizing: border-box;">
                <!-- Initialized in JS -->
              </select>
              <input type="tel" id="lead-whatsapp" required placeholder="99999 99999" pattern="[0-9\s-]{7,15}" style="flex: 1; padding: 12px; border: 1.5px solid var(--color-text-dark); font-family: var(--font-mono); font-size: 0.85rem; background: #ffffff; color: #000000; outline: none; border-radius: 0; box-sizing: border-box;">
            </div>
          </div>
          
          <div style="display: flex; flex-direction: column; gap: var(--space-xs);">
            <label for="lead-contact-method" style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">How should we contact you?</label>
            <select id="lead-contact-method" aria-label="Contact Method" required style="width: 100%; padding: 12px; border: 1.5px solid var(--color-text-dark); font-family: var(--font-mono); font-size: 0.85rem; background: #ffffff; color: #000000; outline: none; border-radius: 0; cursor: pointer; -webkit-appearance: none; -moz-appearance: none; appearance: none; background-image: url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22currentColor%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22><polyline points=%226 9 12 15 18 9%22></polyline></svg>'); background-repeat: no-repeat; background-position: right 12px center; background-size: 16px;">
              <option value="WhatsApp">Contact me via WhatsApp</option>
              <option value="Email">Contact me via Email</option>
            </select>
          </div>
          
          <div style="display: flex; flex-direction: column; gap: var(--space-xs);">
            <label for="lead-question" style="font-family: var(--font-mono); font-size: 0.75rem; font-weight: 700; text-transform: uppercase;">What do you need help with?</label>
            <textarea id="lead-question" required rows="3" placeholder="e.g. Interested in booking automation and custom web design." style="width: 100%; padding: 12px; border: 1.5px solid var(--color-text-dark); font-family: var(--font-mono); font-size: 0.85rem; background: #ffffff; color: #000000; outline: none; border-radius: 0; resize: vertical;"></textarea>
          </div>
          
          <button type="submit" class="pill-btn pill-btn-primary" style="margin-top: 8px; width: 100%; text-align: center; border-radius: 0; border: 2px solid var(--color-text-dark); cursor: pointer; display: block;">
            SUBMIT REQUEST
          </button>
        </form>
        <div id="lead-form-status" style="display: none; text-align: center; padding: var(--space-lg); font-family: var(--font-mono);">
          <span style="font-family: var(--font-display); font-size: 1.1rem; color: #008000; display: block; margin-bottom: 8px;">REQUEST SUBMITTED.</span>
          <p id="lead-status-msg" style="font-size: 0.8rem; line-height: 1.5; color: var(--color-text-dark); max-width: 500px; margin: 0 auto;">
            Thank you! Your request has been sent. Bhuvanesh will get back to you shortly.
          </p>
        </div>
      </div>
    </section>

  </main>

  <!-- Footer -->
  <footer class="main-footer">
    <div class="container">
      <div class="footer-grid">
        <!-- Column 1: Brand -->
        <div class="footer-brand-col">
          <div class="footer-logo">Boldlabs Studio</div>
          <p class="footer-tagline">Booking-first websites for service businesses.</p>
          <div class="footer-socials">
            <a href="https://www.linkedin.com/in/bhuvaneshkarnan/" target="_blank" rel="noopener" title="Bhuvanesh Karnan on LinkedIn">LinkedIn</a>
          </div>
        </div>

        <!-- Column 2: Navigation -->
        <div>
          <h3 class="footer-col-title">Navigation</h3>
          <ul class="footer-links">
            <li><a href="index.html#services">Services</a></li>
            <li><a href="index.html#latest-drop">Case Studies</a></li>
            <li><a href="index.html#timeline">Process</a></li>
            <li><a href="index.html#player">About</a></li>
          </ul>
        </div>

        <!-- Column 3: Trust -->
        <div>
          <h3 class="footer-col-title">Trust</h3>
          <ul class="footer-links">
            <li><a href="index.html#player">Wall of Love</a></li>
            <li><a href="blog.html">Blog</a></li>
            <li><a href="index.html#build-together">Contact</a></li>
            <li><a href="index.html#build-together">Book a Call</a></li>
          </ul>
        </div>

        <!-- Column 4: Legal -->
        <div>
          <h3 class="footer-col-title">Legal</h3>
          <ul class="footer-links">
            <li><a href="terms.html">Terms</a></li>
            <li><a href="privacy.html">Privacy</a></li>
            <li><span style="font-size: 0.75rem; color: rgba(0, 0, 0, 0.85); display: block; margin-top: 4px;">hello@boldlabs.studio</span></li>
          </ul>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="footer-bottom">
        <div class="container" style="padding: 0; width: 100%; display: flex; justify-content: space-between; align-items: center;">
          <span>© 2026 Boldlabs Studio — Bhuvanesh. All rights reserved.</span>
          <span style="font-family: var(--font-display); font-size: 0.7rem;">PROTAGONIST LOADED</span>
        </div>
      </div>
    </div>
  </footer>

  <!-- Global Configurations -->
  <script src="firebase-config.js" defer></script>
  <!-- EmailJS SDK -->
  <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js" defer></script>

  <!-- Interactive Logic -->
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      // Mobile navigation menu toggle
      const toggleBtn = document.getElementById('menu-toggle-btn');
      const linksContainer = document.getElementById('navbar-links-container');
      
      if (toggleBtn && linksContainer) {
        toggleBtn.addEventListener('click', () => {
          const expanded = toggleBtn.getAttribute('aria-expanded') === 'true';
          toggleBtn.setAttribute('aria-expanded', !expanded);
          linksContainer.classList.toggle('active');
        });
      }

      // Initialize country codes in select element
      const countryCodeSelect = document.getElementById('lead-country-code');
      if (countryCodeSelect) {
        const countries = [
          { code: '91', name: 'IN' },
          { code: '1', name: 'US' },
          { code: '1', name: 'CA' },
          { code: '44', name: 'GB' },
          { code: '61', name: 'AU' },
          { code: '971', name: 'AE' },
          { code: '65', name: 'SG' }
        ];
        countryCodeSelect.innerHTML = '';
        countries.forEach(country => {
          const opt = document.createElement('option');
          opt.value = country.code;
          opt.textContent = `${country.name} (+${country.code})`;
          countryCodeSelect.appendChild(opt);
        });
      }

      // Contact form submit logic
      const leadForm = document.getElementById('lead-capture-form');
      const leadFormStatus = document.getElementById('lead-form-status');
      
      const isGoogleSheetConfigured = typeof firebaseConfig !== 'undefined' && firebaseConfig.googleSheetUrl;
      const isEmailjsConfigured = typeof emailjsConfig !== 'undefined' && emailjsConfig.publicKey !== "YOUR_PUBLIC_KEY";

      if (leadForm && leadFormStatus) {
        if (typeof emailjs !== 'undefined' && isEmailjsConfigured) {
          emailjs.init(emailjsConfig.publicKey);
        }

        leadForm.addEventListener('submit', async (e) => {
          e.preventDefault();
          const name = document.getElementById('lead-name').value.trim();
          const email = document.getElementById('lead-email').value.trim();
          const countryCode = document.getElementById('lead-country-code').value;
          const rawWhatsapp = document.getElementById('lead-whatsapp').value.trim();
          const question = document.getElementById('lead-question').value.trim();
          const contactMethod = document.getElementById('lead-contact-method').value;
          const timestamp = new Date().toISOString();
          
          const cleanPhone = rawWhatsapp.replace(/[^0-9]/g, '');
          const cleanWhatsappNumber = `${countryCode}${cleanPhone}`;
          const leadWhatsappLink = `https://wa.me/${cleanWhatsappNumber}`;
          const formattedWhatsapp = `+${countryCode} ${rawWhatsapp}`;

          const leadData = {
            name,
            email,
            whatsapp: formattedWhatsapp,
            contactMethod,
            question,
            sourcePage: 'Blog Home',
            timestamp
          };

          try {
            // Save lead locally to localStorage
            const mockLeads = JSON.parse(localStorage.getItem('boldlabs_mock_leads') || '[]');
            mockLeads.push(leadData);
            localStorage.setItem('boldlabs_mock_leads', JSON.stringify(mockLeads));

            // Save to Google Sheets
            if (isGoogleSheetConfigured) {
              const formData = new URLSearchParams();
              formData.append('name', name);
              formData.append('email', email);
              formData.append('whatsapp', formattedWhatsapp);
              formData.append('contactMethod', contactMethod);
              formData.append('question', question);
              formData.append('sourcePage', 'Blog Home');
              
              try {
                await fetch(firebaseConfig.googleSheetUrl, {
                  method: 'POST',
                  mode: 'no-cors',
                  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                  body: formData.toString()
                });
                console.log("Lead successfully dispatched to Google Sheets Apps Script.");
              } catch (err) {
                console.error("Error dispatching to Google Sheets:", err);
              }
            }

            // EmailJS trigger
            if (typeof emailjs !== 'undefined' && isEmailjsConfigured) {
              emailjs.send(emailjsConfig.serviceId, emailjsConfig.templateId, {
                lead_name: name,
                lead_email: email,
                lead_whatsapp: formattedWhatsapp,
                lead_contact_method: contactMethod,
                lead_question: question,
                lead_whatsapp_link: leadWhatsappLink
              });
            }

            const statusMsg = document.getElementById('lead-status-msg');
            if (contactMethod === 'WhatsApp') {
              const whatsappText = `Hi Boldlabs Studio, I would like to request a discovery call from your Blog page.\n\n*Name*: ${name}\n*Email*: ${email}\n*WhatsApp*: ${formattedWhatsapp}\n*Details*: ${question}`;
              const whatsappUrl = `https://wa.me/${emailjsConfig.yourWhatsappNumber || '918870341570'}?text=${encodeURIComponent(whatsappText)}`;
              window.open(whatsappUrl, '_blank');
              if (statusMsg) {
                statusMsg.textContent = "Thank you! We've opened a new window to chat on WhatsApp. Please send the pre-filled message to connect with us instantly.";
              }
            } else {
              if (statusMsg) {
                statusMsg.textContent = `Thank you! Your request has been sent, and a confirmation email has been dispatched to ${email}. Bhuvanesh will review your request and get back to you shortly.`;
              }
            }

            leadForm.style.display = 'none';
            leadFormStatus.style.display = 'block';
          } catch (error) {
            console.error("Error capturing lead:", error);
            alert("Error sending request. Please email directly to hello@boldlabs.studio");
          }
        });
      }
    });
  </script>
</body>
</html>
"""

# Programmatically generate cards for the published list (sorted descending by date)
cards_html = []
published_posts = sorted(published_posts, key=lambda x: x["date"], reverse=True)

for p in published_posts:
    card = f"""          <!-- Card: {p['title']} -->
          <div class="service-card" style="position: relative; padding: var(--space-lg); border: var(--border-width) solid var(--color-border); background: var(--color-bg-card); display: flex; flex-direction: column; justify-content: space-between; min-height: 380px; cursor: pointer;" onclick="window.location.href='blog/{p['slug']}.html'">
            <div>
              <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--color-text-muted); display: block; margin-bottom: var(--space-sm);">{p['date_display']} · {p['category']}</span>
              <h3 style="font-family: var(--font-display); font-size: 1.1rem; margin-bottom: var(--space-sm); text-transform: uppercase; line-height: 1.2; color: var(--color-text);">{p['title']}</h3>
              <p style="font-size: 0.8rem; color: var(--color-text-muted); line-height: 1.6; margin-bottom: var(--space-md);">{p['question'][:150]}...</p>
            </div>
            <a href="blog/{p['slug']}.html" class="pill-btn pill-btn-primary" style="align-self: flex-start; padding: 8px 16px; font-size: 0.75rem; border-radius: 0; border: 1.5px solid var(--color-text-dark); text-align: center; position: relative; z-index: 2;">Read Mission</a>
          </div>
"""
    cards_html.append(card)

rendered_home = blog_home_template
rendered_home = rendered_home.replace("{{PUBLISHED_COUNT}}", str(len(published_posts)))
rendered_home = rendered_home.replace("{{BLOG_CARDS}}", "\n".join(cards_html))

with open(os.path.join(workspace_root, "blog.html"), "w", encoding="utf-8") as f:
    f.write(rendered_home)
print("Regenerated blog.html with correct footer styling and clickable cards.")


# 2. Regenerate sitemap.xml to include only published blog links
sitemap_base = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://goboldlabs.com/</loc>
    <lastmod>2026-06-30</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://goboldlabs.com/business-website.html</loc>
    <lastmod>2026-06-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://goboldlabs.com/landing-page.html</loc>
    <lastmod>2026-06-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://goboldlabs.com/ecommerce-website.html</loc>
    <lastmod>2026-06-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://goboldlabs.com/monthly-care.html</loc>
    <lastmod>2026-06-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://goboldlabs.com/ai-automations.html</loc>
    <lastmod>2026-06-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://goboldlabs.com/whatsapp-automation-clinics.html</loc>
    <lastmod>2026-07-23</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://goboldlabs.com/white-label-agencies.html</loc>
    <lastmod>2026-06-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://goboldlabs.com/web-development-madurai.html</loc>
    <lastmod>2026-06-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://goboldlabs.com/web-development-tamil-nadu.html</loc>
    <lastmod>2026-06-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://goboldlabs.com/web-development-uk.html</loc>
    <lastmod>2026-06-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://goboldlabs.com/web-development-canada.html</loc>
    <lastmod>2026-06-30</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://goboldlabs.com/privacy.html</loc>
    <lastmod>2026-06-30</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://goboldlabs.com/terms.html</loc>
    <lastmod>2026-06-30</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://goboldlabs.com/blog.html</loc>
    <lastmod>2026-06-30</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
"""

for p in published_posts:
    sitemap_base += f"""  <url>
    <loc>https://goboldlabs.com/blog/{p['slug']}.html</loc>
    <lastmod>{p['date']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>\n"""

sitemap_base += "</urlset>\n"

with open(os.path.join(workspace_root, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_base)
print("Regenerated sitemap.xml with active scheduled URLs.")


# 3. Regenerate llms.txt to include active posts
llms_txt_base = """# Boldlabs Studio

> https://goboldlabs.com

Boldlabs Studio is a premier web development and web design agency based in Madurai, Tamil Nadu, India, serving B2B and local service businesses globally (including India, UK, Canada, and USA). Founded and led by Bhuvanesh Karnan (Founder & Head Developer).

## Core Capabilities
- **Booking-First Websites**: Custom web development integrated with automated booking systems, reminders, and follow-ups.
- **Custom Web Development**: Blazing-fast React applications (Next.js/Vite) and high-performance custom WordPress/WooCommerce and Shopify storefronts.
- **AI Operational Automations**: Bespoke workflow automations connecting web forms to CRM databases (Airtable, Notion, Slack, Google Sheets) and WhatsApp redirects.
- **White-Label Retainers**: Outsourced Figma-to-Code engineering partners for design and marketing agencies.

## Key Information
- **Founder**: Bhuvanesh Karnan (LinkedIn: https://www.linkedin.com/in/bhuvaneshkarnan/)
- **Physical Address**: Madurai, Tamil Nadu, India (Postal Code: 625001)
- **WhatsApp Contact**: +918870341570
- **Email Contact**: hello@boldlabs.studio
- **Pricing & Model**: Month-to-month subscription plans, no setup fees, cancel anytime.

## Navigation & Page Index
- [Homepage](https://goboldlabs.com/) - Overview of services, stats (31+ service businesses served), interactive developer card, pricing, and consultation booking.
- [Custom Business Websites](https://goboldlabs.com/business-website.html) - Custom React and WordPress development with local SEO and speed optimizations.
- [High-Converting Landing Pages](https://goboldlabs.com/landing-page.html) - Single-page funnels optimized for Google/Facebook Ads.
- [Custom E-Commerce Stores](https://goboldlabs.com/ecommerce-website.html) - Shopify and WooCommerce custom design and checkout optimization.
- [Website Maintenance & Care](https://goboldlabs.com/monthly-care.html) - Daily backups, security updates, and monthly SEO maintenance retainer.
- [AI automations & CRM Integration](https://goboldlabs.com/ai-automations.html) - Workflow pipelines using Make, Zapier, and Python to automate lead tracking.
- [Clinic WhatsApp Automation](https://goboldlabs.com/whatsapp-automation-clinics.html) - 24/7 AI WhatsApp receptionist for medical clinics: instant replies, AI booking flow, auto confirmations, reminders, and 5-star Google review collection.
- [White-Label Agency Retainers](https://goboldlabs.com/white-label-agencies.html) - Figma-to-code partnership program for agencies with 24-48h turnarounds.
- [Madurai Local Landing Page](https://goboldlabs.com/web-development-madurai.html) - Web development services customized for local businesses in Madurai, India.
- [Tamil Nadu Regional Page](https://goboldlabs.com/web-development-tamil-nadu.html) - Regional web design and development services for Tamil Nadu, India.
- [UK International Landing Page](https://goboldlabs.com/web-development-uk.html) - Web development services optimized for UK service providers.
- [Canada International Landing Page](https://goboldlabs.com/web-development-canada.html) - Web design and development services optimized for B2B firms in Canada.
- [The Blog](https://goboldlabs.com/blog.html) - Directory of insights on web design, SEO, and operations automation.
"""

for p in published_posts:
    llms_txt_base += f"- [{p['title']}](https://goboldlabs.com/blog/{p['slug']}.html) - {p['question'][:120]}...\n"

with open(os.path.join(workspace_root, "llms.txt"), "w", encoding="utf-8") as f:
    f.write(llms_txt_base)
print("Regenerated llms.txt with active blog links.")

# 4. Generate IndexNow Key verification file and ping API (Bing / ChatGPT Search)
indexnow_key = "601c45012586419ca62df1a415ff68f8"
indexnow_file = os.path.join(workspace_root, f"{indexnow_key}.txt")
with open(indexnow_file, "w", encoding="utf-8") as f:
    f.write(indexnow_key)

# Build URL list to submit
submit_urls = [
    "https://goboldlabs.com/",
    "https://goboldlabs.com/blog.html",
    "https://goboldlabs.com/business-website.html",
    "https://goboldlabs.com/landing-page.html",
    "https://goboldlabs.com/ecommerce-website.html",
    "https://goboldlabs.com/monthly-care.html",
    "https://goboldlabs.com/ai-automations.html",
    "https://goboldlabs.com/whatsapp-automation-clinics.html",
    "https://goboldlabs.com/white-label-agencies.html",
    "https://goboldlabs.com/web-development-madurai.html",
    "https://goboldlabs.com/web-development-tamil-nadu.html",
    "https://goboldlabs.com/web-development-uk.html",
    "https://goboldlabs.com/web-development-canada.html"
]
for p in published_posts:
    submit_urls.append(f"https://goboldlabs.com/blog/{p['slug']}.html")

payload = {
    "host": "goboldlabs.com",
    "key": indexnow_key,
    "keyLocation": f"https://goboldlabs.com/{indexnow_key}.txt",
    "urlList": submit_urls
}

import urllib.request
import urllib.error

print("Submitting active URLs to IndexNow (Bing/ChatGPT Search)...")
try:
    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=10) as response:
        status_code = response.getcode()
        print(f"IndexNow submission succeeded! Status code: {status_code}")
except urllib.error.URLError as e:
    print(f"IndexNow submission failed: {e}")
except Exception as e:
    print(f"IndexNow submission encountered an unexpected error: {e}")

