#!c:\users\magno\documents\projects\e-commerce\guacatea_market\guacatea\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'flask-swagger==0.2.14','console_scripts','flaskswagger'
__requires__ = 'flask-swagger==0.2.14'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('flask-swagger==0.2.14', 'console_scripts', 'flaskswagger')()
    )
