import json
import urllib.parse
import boto3
 
# Define the client to interact with AWS Lambda
client = boto3.client('lambda')
s3 = boto3.client('s3')
def lambda_handler(event,context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        print("bucket", event['Records'][0]['s3']['bucket'])
        inputParams = {
        "bucket"   : bucket,
        "key"  : key
        }
        response = client.invoke(
        FunctionName = 'arn:aws:lambda:us-east-1:697174678341:function:lambda-to-invoke-1357',
        InvocationType = 'RequestResponse',
        Payload = json.dumps(inputParams)
    )
 
        responseFromChild = json.load(response['Payload'])
        print(responseFromChild)
        return responseFromChild
    except Exception as e:
        print(e)
        raise e
 
    