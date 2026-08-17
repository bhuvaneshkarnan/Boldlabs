import os, re
count = 0
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ['.git', '.github', 'node_modules']]
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8') as file:
                    content = file.read()
            except Exception:
                continue
                
            orig = content
            content = re.sub(r'\s*<span class="marquee-item">SMART PARKNGO</span>', '', content, flags=re.IGNORECASE)
            content = re.sub(r'\s*<span class="marquee-item">AMIZHTHINI FOODS</span>', '', content, flags=re.IGNORECASE)
            
            if content != orig:
                with open(p, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"Updated {p}")
                count += 1
                
print(f'Removed from {count} files.')
