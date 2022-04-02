from picamera import PiCamera
#from time import sleep
from boto3 import session
from botocore.client import Config
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv() # a function that reads the .env file and stores those variables in os.env and makes them environment variables
ACCESS_ID = os.environ["ACCESS_ID"]
SECRET_KEY = os.environ["SECRET_KEY"]
SPACES_URL = os.environ["SPACES_URL"]


# initiate session with spaces
session = session.Session()
client = session.client("s3", 
                        region_name = "ams3", 
                        endpoint_url = SPACES_URL,
                        aws_access_key_id = ACCESS_ID,
                        aws_secret_access_key=SECRET_KEY)


# capture image
camera = PiCamera()
now = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
path = f"/tmp/image{now}.jpeg"

camera.capture(path)

# upload image
try:
    client.upload_file(path, "picamera_photos", f"image{now}.jpeg")
    print("Successful upload")
except Exception:
    print("Failed client connection")
    exit(1)

# delete image
os.remove(path)

