import os
import re

def fix_links(content, file_path):
    is_root = file_path == './index.html'
    is_blog_index = file_path == './blog/index.html'
    is_service_page = file_path.startswith('./') and file_path.endswith('/index.html') and not file_path.startswith('./blog/')
    is_blog_post = file_path.startswith('./blog/') and file_path != './blog/index.html'

    # Fix relative root references like ../index.html
    content = re.sub(r'href=[\'\"](?:\.\./)+index\.html(#.*?)[\'\"]', r'href="/\1"', content)
    content = re.sub(r'href=[\'\"](?:\.\./)+index\.html[\'\"]', r'href="/"', content)
    
    # Fix local index references
    content = re.sub(r'href=[\'\"]index\.html(#.*?)[\'\"]', r'href="/\1"', content)
    content = re.sub(r'href=[\'\"]index\.html[\'\"]', r'href="/"', content)
    
    # Fix blog index links in root or service pages
    content = re.sub(r'href=[\'\"](?:\.\./)*blog\.html[\'\"]', r'href="/blog/"', content)
    content = re.sub(r'href=[\'\"](?:\.\./)*blog/index\.html[\'\"]', r'href="/blog/"', content)
    
    # Fix internal links (any .html)
    def repl_html(match):
        path = match.group(1)
        if path.startswith('http'):
            return f'href="{path}"'
            
        clean_path = path.replace('../', '').replace('./', '')
        
        # Avoid things that are external or mailto etc if matched somehow
        if clean_path.startswith('/') or clean_path.startswith('mailto:') or clean_path.startswith('tel:'):
            return f'href="{path}"'
            
        if clean_path.startswith('blog/') and clean_path.endswith('.html'):
            slug = clean_path[5:-5]
            return f'href="/blog/{slug}"'
            
        if clean_path.endswith('.html'):
            slug = clean_path[:-5]
            return f'href="/{slug}"'
            
        return match.group(0)

    content = re.sub(r'href=[\'\"]([^\'\"]+\.html)[\'\"]', repl_html, content)
    
    # Fix onclick window.location.href
    def repl_onclick(match):
        path = match.group(1)
        clean_path = path.replace('../', '').replace('./', '')
        if clean_path.startswith('blog/') and clean_path.endswith('.html'):
            slug = clean_path[5:-5]
            return f'onclick="window.location.href=\'/blog/{slug}\'"'
        if clean_path.endswith('.html'):
            slug = clean_path[:-5]
            return f'onclick="window.location.href=\'/{slug}\'"'
        return match.group(0)
        
    content = re.sub(r'onclick=[\'\"]window\.location\.href=[\'\"]([^\'\"]+\.html)[\'\"][\'\"]', repl_onclick, content)

    # Fix relative links to other blog posts within blog posts
    if is_blog_post:
        def repl_blog_rel(match):
            path = match.group(1)
            if not path.startswith('/') and not path.startswith('http') and path.endswith('.html'):
                slug = path[:-5]
                return f'href="/blog/{slug}"'
            return match.group(0)
        content = re.sub(r'href=[\'\"]([^\'\"]+\.html)[\'\"]', repl_blog_rel, content)

    # Clean canonicals and OGs
    content = re.sub(r'<link rel=\"canonical\" href=\"(https://goboldlabs.com/[^\"]+)\.html\">', r'<link rel="canonical" href="\1">', content)
    content = re.sub(r'<meta property=\"og:url\" content=\"(https://goboldlabs.com/[^\"]+)\.html\">', r'<meta property="og:url" content="\1">', content)
    content = re.sub(r'<meta property=\"twitter:url\" content=\"(https://goboldlabs.com/[^\"]+)\.html\">', r'<meta property="twitter:url" content="\1">', content)

    return content

count = 0
for root, dirs, files in os.walk('.'):
    # Prune dirs in place to avoid descending into them
    dirs[:] = [d for d in dirs if d not in ['.git', '.github', 'node_modules']]
    
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8') as f_in:
                    old_content = f_in.read()
            except Exception as e:
                print(f"Failed to read {p}: {e}")
                continue
            
            new_content = fix_links(old_content, p.replace('\\\\', '/').replace('\\', '/'))
            
            if new_content != old_content:
                try:
                    with open(p, 'w', encoding='utf-8') as f_out:
                        f_out.write(new_content)
                    count += 1
                except Exception as e:
                    print(f"Failed to write {p}: {e}")

print(f'Fixed links in {count} HTML files.')
