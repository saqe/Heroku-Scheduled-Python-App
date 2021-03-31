import requests
from os import getenv

page = requests.get(
    # WEBHOOK_LINK is a sample link to test, if the cronjob is working.
    getenv('WEBHOOK_LINK')
)

print( page.status_code )