#!/usr/bin/env python3
##
## generate-ec2-ssh-config.py
##
## EC2 - Boto 3 Docs 1.9.49 documentation
## https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html
##
import boto3

client = boto3.client('ec2')

response = client.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        if instance['PublicDnsName'] == "":
            continue

        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                print('Host ' + tag['Value'])
        print('  HostName ' + instance['PublicDnsName'])

        login_name_exist = None
        print('  User ', end='')
        for tag in instance['Tags']:
            if tag['Key'] == 'login_name':
                print(tag['Value'])
                login_name_exist = 'EXIST'
        if login_name_exist is None:
            print('ec2-user')

        print('  IdentityFile ~/.ssh/' + instance['KeyName'] + '.pem')
        print()
