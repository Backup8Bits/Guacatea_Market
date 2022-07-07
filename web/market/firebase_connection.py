import os
import secrets

import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials, storage
from PIL import Image

load_dotenv()

cred = credentials.Certificate("/code/market/serviceAccountKey.json")
app = firebase_admin.initialize_app(cred, {"storageBucket": "g-market-5f76f.appspot.com"})

def upload_file(image):
    random_path = secrets.token_hex(12)
    bucket = storage.bucket()
    img = Image.open(image)
    img = img.convert('RGB')
    img.thumbnail((800, 800))
    filename = random_path + '.' + 'png'
    img.save(filename) # Save format
    blob = bucket.blob(str(filename))
    blob.upload_from_filename(filename)
    blob.make_public()
    print("Your file url", blob.public_url)
    return blob.public_url
