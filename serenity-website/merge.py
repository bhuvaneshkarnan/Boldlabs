import glob, os
def merge(target, pattern):
    files = sorted(glob.glob(pattern))
    with open(target, 'w', encoding='utf-8') as out:
        for f in files:
            with open(f, 'r', encoding='utf-8') as src:
                out.write(src.read())
            os.remove(f)
    print(f"Merged {len(files)} files into {target} ({os.path.getsize(target)} bytes)")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 2:
        merge(sys.argv[1], sys.argv[2])