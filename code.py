import requests
from os import getenv

page = requests.get(
    getenv('TEST_WEBHOOK_LINK')
)

print( page.status_code )