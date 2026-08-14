import glob
import re

files_to_process = []
files_to_process.append('index.html')
files_to_process.append('blog/index.html')
files_to_process.extend(glob.glob('blog/*/index.html'))
files_to_process.extend(glob.glob('*/index.html')) # e.g. business-website/index.html
# Deduplicate
files_to_process = list(set(files_to_process))

count = 0
for p in files_to_process:
    try:
        with open(p, 'r', encoding='utf-8') as f_in:
            content = f_in.read()
    except Exception as e:
        continue
    
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
    
    # Specific targeted replacements for blog items inside index files
    if p == 'blog\\index.html' or p == 'blog/index.html' or p == 'index.html':
        content = re.sub(r'href=\"blog/([^\"]+)\.html\"', r'href=\"/blog/\1\"', content)
        content = re.sub(r'href=\"([^\"]+)\.html\"', r'href=\"/\1\"', content)
        content = re.sub(r'onclick=\"window\.location\.href=\'blog/([^\']+)\.html\'\"', r'onclick=\"window.location.href=\'/blog/\1\'\"', content)
    
    # Specific targeted replacements inside blog posts
    if p.startswith('blog\\') or p.startswith('blog/'):
        if p != 'blog\\index.html' and p != 'blog/index.html':
            # Relative links to other blogs
            content = re.sub(r'href=\"([^\"]+)\.html\"', r'href=\"/blog/\1\"', content)
    
    # Clean canonicals and OGs
    content = re.sub(r'<link rel=\"canonical\" href=\"(https://goboldlabs.com/[^\"]+)\.html\">', r'<link rel=\"canonical\" href=\"\1\">', content)
    content = re.sub(r'<meta property=\"og:url\" content=\"(https://goboldlabs.com/[^\"]+)\.html\">', r'<meta property=\"og:url\" content=\"\1\">', content)
    content = re.sub(r'<meta property=\"twitter:url\" content=\"(https://goboldlabs.com/[^\"]+)\.html\">', r'<meta property=\"twitter:url\" content=\"\1\">', content)
    
    if content != orig:
        with open(p, 'w', encoding='utf-8') as f_out:
            f_out.write(content)
        count += 1

print(f'Fixed {count} files.')
