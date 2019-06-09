#!C:\Users\meroz\PycharmProjects\news\venvw\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'google-alerts==0.2.1','console_scripts','google-alerts'
__requires__ = 'google-alerts==0.2.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('google-alerts==0.2.1', 'console_scripts', 'google-alerts')()
    )
