import os
import boto3
import json


def read_my_credentials(credfile="cred.json"):
    try:
        with open(os.getcwd() + '/aws/' + credfile, 'r') as f:
            creds = json.load(f)
        return creds
    except FileNotFoundError as e:
        print(f"file not found: {e}")
    except Exception as e:
        print(f"Other error {e}")
    return None


def create_upload_download_delete_file_S3_Bucket(nameBucket):
    creds = read_my_credentials()
    if creds:
        s3 = boto3.client("s3", aws_access_key_id=creds['access-key-id'],
                          aws_secret_access_key=creds['secret-access-key'],
                          region_name=creds['region'])
        response = s3.list_buckets()
        exist = False
        for bucket in response['Buckets']:
            if nameBucket == bucket['Name']:
                exist = True
                break
        if not exist:
            location = {'LocationConstraint': creds['region']}
            s3.create_bucket(Bucket=nameBucket,
                             CreateBucketConfiguration=location)
        s3.upload_file(
            Filename=os.getcwd() + '/aws/'+"First practice - aws/hi.txt",
            Bucket=nameBucket,
            Key="hi2.txt",
        )
        s3.download_file(
            Bucket=nameBucket, Key="hi2.txt", Filename=os.getcwd() + '/aws/'+"First practice - aws/hi5.txt"
        )
        response = s3.list_objects(Bucket=nameBucket)
        for content in response.get('Contents', []):
            s3.delete_object(Bucket=nameBucket, Key=content.get('Key'))
        s3.delete_bucket(Bucket=nameBucket)


create_upload_download_delete_file_S3_Bucket("backet-via-console")
