# This is a simple script that uses the AWS Boto3 python SDK to connect to S3 and download a file.

import boto3

# Variables, specify values here
bucket_name = '' # S3 bucket name
object_key = '' # Example 'some-file.txt'
download_to_path = '' # local path to download the file to

# Optional: Enabling logs allows us to see request and response data
boto3.set_stream_logger(name='botocore')

# Connect to resource
s3 = boto3.resource('s3') # Optional: you may specify region here with region_name, e.g. region_name='us-east-1'

# Download file
s3.Object(bucket_name, object_key).download_file(download_to_path)
