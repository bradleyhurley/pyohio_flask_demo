import os

try:
    API_KEY = os.environ['GOOGLE_API_KEY']
    CX_ID = os.environ['CX_ID']
except KeyError:
    print("Please Export The Keys")