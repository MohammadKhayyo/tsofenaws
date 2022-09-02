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


def create_new_policy(policy_name, policy_filename):
    creds = read_my_credentials()
    if creds:
        client = boto3.client('iam', aws_access_key_id=creds['access-key-id'],
                              aws_secret_access_key=creds['secret-access-key'],
                              region_name=creds['region'])
        if client:
            try:
                with open(os.getcwd() + '/aws/' + policy_filename, 'r') as f:
                    policy = json.load(f)
                    policy = json.dumps(policy)
                    client.create_policy(
                        PolicyName=policy_name, PolicyDocument=policy)
            except FileNotFoundError as e:
                print(f"file not found: {e}")
            except Exception as e:
                print(f"Other error {e}")


create_new_policy('no-delete-user-policy-python', 'policy.json')
