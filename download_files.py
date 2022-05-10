from boto3 import session
import os
from datetime import datetime
from dotenv import load_dotenv
import boto.s3.connection

load_dotenv() # a function that reads the .env file and stores those variables in os.env and makes them environment variables
ACCESS_ID = os.environ["ACCESS_ID"]
SECRET_KEY = os.environ["SECRET_KEY"]
SPACES_URL = "https://ams3.digitaloceanspaces.com"


# initiate session with spaces
session = session.Session()
client = session.client("s3", 
                        region_name = "ams3", 
                        endpoint_url = SPACES_URL,
                        aws_access_key_id = ACCESS_ID,
                        aws_secret_access_key=SECRET_KEY)



my_photos = client.list_objects(Bucket = 'mononokeros')['Contents']

for photo in my_photos:
    client.download_file('mononokeros', f"{photo['Key']}", f"{photo['Key']}")


