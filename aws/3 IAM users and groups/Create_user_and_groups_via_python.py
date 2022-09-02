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


def demo_boto3():
    creds = read_my_credentials()
    if creds:
        client = boto3.client('sts', aws_access_key_id=creds['access-key-id'],
                              aws_secret_access_key=creds['secret-access-key'],
                              region_name=creds['region'])
        if client:
            print(client.get_caller_identity())


def add_new_user_to_new_group(user_name, group_name):
    creds = read_my_credentials()
    if creds:
        client = boto3.client('iam', aws_access_key_id=creds['access-key-id'],
                              aws_secret_access_key=creds['secret-access-key'],
                              region_name=creds['region'])
        if client:
            try:
                exist = False
                clients = client.list_users()
                print(clients)
                for item in clients['Users']:
                    if user_name == item['UserName']:
                        print(f"The client: {user_name} is already exists")
                        exist = True
                if not exist:
                    client.create_user(UserName=user_name)
                exist = False
                groups = client.list_groups()
                print(groups)
                for item in groups['Groups']:
                    if group_name == item['GroupName']:
                        print(f"The group: {group_name} is already exists")
                        exist = True
                if not exist:
                    client.create_group(GroupName=group_name)
                exist = False
                listsOfGroupsOfUser = client.list_groups_for_user(
                    UserName=user_name)
                print(listsOfGroupsOfUser['Groups'])
                for item in listsOfGroupsOfUser['Groups']:
                    if group_name == item['GroupName']:
                        print(
                            f"The client: {user_name} is already exists in {group_name}")
                        exist = True
                if not exist:
                    client.add_user_to_group(
                        UserName=user_name, GroupName=group_name)
            except Exception as e:
                print(f"Other error {e}")


add_new_user_to_new_group("userFromPython", "groupFromPython")
