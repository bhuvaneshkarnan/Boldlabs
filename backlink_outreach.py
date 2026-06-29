import csv
import urllib.parse
import os

def generate_outreach_campaign(csv_file, output_html):
    """
    Reads a CSV of targets (Name, Email, Website, Blog_Topic)
    Generates an HTML dashboard with 1-click 'mailto:' links for SEO backlink outreach.
    """
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found. Please create it with Name,Email,Website,Blog_Topic columns.")
        return

    html_content = """
    <html>
    <head>
        <title>Boldlabs SEO Outreach Dashboard</title>
        <style>
            body { font-family: monospace; padding: 2rem; background: #fafafa; }
            .card { background: white; padding: 1.5rem; border: 1px solid #ccc; margin-bottom: 1rem; border-radius: 4px; }
            a.btn { display: inline-block; padding: 10px 20px; background: #000; color: #fff; text-decoration: none; font-weight: bold; margin-top: 10px; }
            h1 { text-transform: uppercase; }
        </style>
    </head>
    <body>
        <h1>Month 3/4: Backlink Outreach Campaign</h1>
        <p>Click the buttons below to open your email client with a pre-written, highly personalized SEO pitch.</p>
    """

    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("Name", "Editor")
            email = row.get("Email", "")
            website = row.get("Website", "")
            topic = row.get("Blog_Topic", "web development trends")

            subject = f"Collaboration / Expert insights on {topic} for {website}"
            
            body = f"""Hi {name},

I loved your recent piece on {topic}. It's a topic we've been heavily researching at Boldlabs Studio.

I am Bhuvanesh Karnan, founder of a custom web development agency serving India and Canada. We recently published a deeply technical, 200-post engineering library on B2B conversion architectures and web performance.

I'd love to write a high-quality, free guest editorial for {website} diving into the technical mechanics of {topic}. No fluff—just actionable engineering insights for your readers. 

Would you be open to a quick draft?

Best,
Bhuvanesh Karnan
Founder, Boldlabs Studio
https://goboldlabs.com"""

            encoded_subject = urllib.parse.quote(subject)
            encoded_body = urllib.parse.quote(body)
            mailto_link = f"mailto:{email}?subject={encoded_subject}&body={encoded_body}"

            html_content += f"""
            <div class="card">
                <h3>Target: {website} ({name})</h3>
                <p><strong>Topic:</strong> {topic}</p>
                <a href="{mailto_link}" class="btn" target="_blank">Send Pitch to {email}</a>
            </div>
            """

    html_content += "</body></html>"

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Success! Outreach dashboard generated at {output_html}")

if __name__ == "__main__":
    # Create dummy CSV if it doesn't exist to show how it works
    if not os.path.exists("seo_targets.csv"):
        with open("seo_targets.csv", "w", encoding="utf-8") as f:
            f.write("Name,Email,Website,Blog_Topic\n")
            f.write("Tech Editor,editor@techblog.ca,TechBlog.ca,Headless E-Commerce\n")
            f.write("Local News,pitch@maduraitoday.in,MaduraiToday.in,Local Business Digitization\n")
            
    generate_outreach_campaign("seo_targets.csv", "outreach_dashboard.html")
