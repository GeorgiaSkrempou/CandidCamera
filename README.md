# Candid Camera

## Raspberry Pi zero with ZeroCam module

- `upload-files.py`: A script to take pictures with the Raspberry Pi zero and the ZeroCam module and upload them to Digital Ocean Spaces
- `download-files.py`: A script to download the images from Spaces locally
- `timelapse.py`: A script to read the downloaded files and create a timelapse video

## How to use it

- Use a cronjob to run the `upload-files.py` once every certain amount of time. I use it to take one pic of my cactus every day
- After a certain amount of time, download all of the images
- Create a timelapse video
- Voila! You can see you plant growing!
