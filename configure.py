import getpass
import sys
import os

username = os.getenv('EMAIL', 'you@example.com')
if len(sys.argv) > 1:
        username = sys.argv[1]
passwd = getpass.getpass('Enter password for %s: ' % username)
delay = 5.0  # in seconds
