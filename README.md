# Raspberry Pi zero with ZeroCam

A script to take pictures with the Raspberry Pi zero and the ZeroCam module.

## How it works

The script captures a picture and saves it locally as a temporary file. 
A session with a SPACES client (Digital Ocean) is initiated. The image is uploaded there and deleted from the local directory.

## Extra ideas

Use a cronjob to run once every certain amount of time.
