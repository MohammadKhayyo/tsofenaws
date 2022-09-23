import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print("event", event['Records'][0]['s3'])
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        text = response["Body"].read().decode('ASCII')
        text = text.split()
        replace = False
        index = 0
        for word in text:
            if replace == True:
                text[index] = ''.join(['_' for w in word])
                replace = False
            if word.lower() == "password" or word.lower() == "pass":
                replace = True
            index += 1
        s = ' '.join(text)

        s3.put_object(Body=s, Bucket='clean-bucket-135', Key=key)
        print("The Body: ", s)
        return ' Success! '
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
