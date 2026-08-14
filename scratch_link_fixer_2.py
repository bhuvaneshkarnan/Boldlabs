import os

count = 0
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ['.git', '.github', 'node_modules']]
    
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as f_in:
                content = f_in.read()
            
            orig = content
            
            # Simple replacements for known problematic strings
            content = content.replace('href=\"../index.html#', 'href=\"/#')
            content = content.replace('href=\"../index.html\"', 'href=\"/\"')
            content = content.replace('href=\"index.html#', 'href=\"/#')
            content = content.replace('href=\"index.html\"', 'href=\"/\"')
            content = content.replace('href=\"../blog.html\"', 'href=\"/blog\"')
            content = content.replace('href=\"blog.html\"', 'href=\"/blog\"')
            content = content.replace('href=\"../blog/index.html\"', 'href=\"/blog\"')
            content = content.replace('href=\"/blog/index.html\"', 'href=\"/blog\"')
            
            # Additional simple replacements for links to specific blogs from blog index
            # These are href=\"blog/slug.html\"
            # We want them to be href=\"/blog/slug\"
            if p == '.\\blog\\index.html' or p == './blog/index.html':
                # Just replace .html with nothing for everything starting with blog/
                import re
                content = re.sub(r'href=\"blog/([^\"]+)\.html\"', r'href=\"/blog/\1\"', content)
                content = re.sub(r'href=\"([^\"]+)\.html\"', r'href=\"/\1\"', content)
                content = re.sub(r'onclick=\"window\.location\.href=\'blog/([^\']+)\.html\'\"', r'onclick=\"window.location.href=\'/blog/\1\'\"', content)
            
            if p.startswith('.\\blog\\') and p != '.\\blog\\index.html':
                import re
                # inside a blog post, links to other blog posts are href="slug.html"
                content = re.sub(r'href=\"([^\"]+)\.html\"', r'href=\"/blog/\1\"', content)
            
            if p == '.\\index.html' or p == './index.html':
                import re
                # replace href="slug.html" with href="/slug"
                content = re.sub(r'href=\"([^\"]+)\.html\"', r'href=\"/\1\"', content)
                
            # Clean canonicals and OGs
            import re
            content = re.sub(r'<link rel=\"canonical\" href=\"(https://goboldlabs.com/[^\"]+)\.html\">', r'<link rel=\"canonical\" href=\"\1\">', content)
            content = re.sub(r'<meta property=\"og:url\" content=\"(https://goboldlabs.com/[^\"]+)\.html\">', r'<meta property=\"og:url\" content=\"\1\">', content)
            content = re.sub(r'<meta property=\"twitter:url\" content=\"(https://goboldlabs.com/[^\"]+)\.html\">', r'<meta property=\"twitter:url\" content=\"\1\">', content)
            
            if content != orig:
                with open(p, 'w', encoding='utf-8') as f_out:
                    f_out.write(content)
                count += 1

print(f'Fixed {count} files.')
