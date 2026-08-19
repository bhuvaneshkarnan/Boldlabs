import glob
import re

files_to_process = []
files_to_process.append('index.html')
files_to_process.append('blog/index.html')
files_to_process.extend(glob.glob('blog/*/index.html'))
files_to_process.extend(glob.glob('*/index.html'))
files_to_process = list(set(files_to_process))

count = 0
for p in files_to_process:
    try:
        with open(p, 'r', encoding='utf-8') as f_in:
            content = f_in.read()
    except Exception as e:
        continue
    
    orig = content

    pattern = re.compile(r'const\s+deck\s*=\s*document\.getElementById\(\'player-deck\'\);\s*const\s+cards\s*=\s*Array\.from\(deck\.children\);\s*cards\.forEach\(card\s*=>\s*\{\s*card\.addEventListener\(\'click\',\s*\(\)\s*=>\s*\{\s*if\s*\(card\.classList\.contains\(\'active-card\'\)\)\s*return;\s*// Remove active state from all cards\s*cards\.forEach\(c\s*=>\s*\{\s*c\.classList\.remove\(\'active-card\'\);\s*\}\);\s*// Make the clicked card active\s*card\.classList\.add\(\'active-card\'\);\s*\}\);\s*\}\);', re.MULTILINE)
    
    def replacer(m):
        return '''const deck = document.getElementById('player-deck');
      if (deck) {
        const cards = Array.from(deck.children);
        cards.forEach(card => {
          card.addEventListener('click', () => {
            if (card.classList.contains('active-card')) return;
            cards.forEach(c => c.classList.remove('active-card'));
            card.classList.add('active-card');
          });
        });
      }'''
    
    content = pattern.sub(replacer, content)
    
    if content != orig:
        with open(p, 'w', encoding='utf-8') as f_out:
            f_out.write(content)
        count += 1

print(f'Fixed JS exception in {count} files.')
