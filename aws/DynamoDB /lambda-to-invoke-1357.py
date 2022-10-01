import json
import boto3
import uuid
import hashlib
s3 = boto3.client('s3')
client = boto3.client('dynamodb')


def lambda_handler(event, context):
    try:
        bucket_invoker = event["bucket"]
        key_invoker = event["key"]
        response = s3.get_object(Bucket=bucket_invoker, Key=key_invoker)
        text_bytes = response["Body"].read()
        readable_hash = hashlib.sha256(text_bytes).hexdigest()
        data = client.scan(TableName='DynamoDB-to-invoke')
        for item in data['Items']:
            if readable_hash == item['hashlib-sha256-for-content']['S']:
                occurrence = 2
                if 'occurrence' in item.keys():
                    occurrence = int(item['occurrence']['N']) + 1
                new_item = {
                    'hashlib-sha256-for-content': {
                        'S': item['hashlib-sha256-for-content']['S'],
                    },
                    'url': {
                        'S': item['url']['S']
                    },
                    'name': {
                        'S': item['name']['S']
                    },
                    'size': {
                        'N': item['size']['N']
                    },
                    'list of words of the first line': {
                        'SS': item['list of words of the first line']['SS']
                    },
                    'occurrence': {
                        'N': f'{occurrence}'
                    }
                }
                response = client.put_item(
                    TableName='DynamoDB-to-invoke',
                    Item=new_item,
                    ReturnConsumedCapacity='TOTAL'
                )
                return json.dumps({'status': 200, 'message': 'Success!'})
        url = f'https://{bucket_invoker}.s3.amazonaws.com/{key_invoker}'
        name = key_invoker
        size = response["ContentLength"]
        text_string = text_bytes.decode('ASCII')
        first_line = text_string.split('\n', 1)[0]
        list_of_words_of_the_first_line = first_line.split()
        new_item = {
            'hashlib-sha256-for-content': {
                'S': readable_hash,
            },
            'url': {
                'S': url
            },
            'name': {
                'S': name
            },
            'size': {
                'N': f'{size}'
            },
            'list of words of the first line': {
                'SS': list_of_words_of_the_first_line
            }
        }
        response = client.put_item(
            TableName='DynamoDB-to-invoke',
            Item=new_item,
            ReturnConsumedCapacity='TOTAL'
        )
        s3.put_object(Body=text_string,
                      Bucket='bucket-lambda-to-invoke-1357', Key=key_invoker)
        return json.dumps({'status': 200, 'message': 'Success!'})
    except Exception as e:
        print("e", e)
        return json.dumps({"status": 500, "message": e})
