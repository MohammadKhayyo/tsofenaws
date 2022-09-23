import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')
client = boto3.client('sns')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response=client.publish(TopicArn="arn:aws:sns:us-east-1:697174678341:topic-via-console",Message=f'https://{bucket}.s3.amazonaws.com/{key}')
        if not response:
            print('Error publish')
            raise "ERROR"
        return ' Success! '
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
