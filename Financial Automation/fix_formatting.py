import re
import glob
for f in glob.glob('*.py'):
    with open(f, 'r') as fi:
        content = fi.read()
    content = re.sub(r'&amp;#10;', '
', content)
    content = re.sub(r'
', '
', content)
    with open(f, 'w') as fo:
        fo.write(content)
    print(f'Fixed {f}')
