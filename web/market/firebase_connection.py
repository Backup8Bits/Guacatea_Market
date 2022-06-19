import secrets

import firebase_admin
from firebase_admin import credentials, storage
from PIL import Image

cred = credentials.Certificate("/code/market/serviceAccountKey.json")
app = firebase_admin.initialize_app(cred, {"storageBucket": "guacatea-market.appspot.com"})

def upload_file(image):
    picture_path = secrets.token_hex(12)
    bucket = storage.bucket()
    img = Image.open(image)
    img.thumbnail((800, 800))
    resize_img = img.save(picture_path + '.' + img.format)
    path = picture_path + '.' + img.format
    blob = bucket.blob(str(resize_img))
    blob.upload_from_filename(path)
    blob.make_public()
    print("your file url", blob.public_url)
    return blob.public_url
