#!/usr/bin/env python
##
## generate-ec2-aliases.py
##
## EC2 — Boto 3 Docs 1.9.49 documentation
## https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html
##
import boto3

client = boto3.client('ec2')

response = client.describe_instances()
for reservation in response['Reservations']:
    for instance in sorted(reservation['Instances']):
        if instance['PublicDnsName'] == "":
            continue

        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                alias_phrase = str(
                    'alias ssh-' +
                    tag['Value'] +
                    '=\'ssh ' +
                    tag['Value'] +
                    '\''
                )
                print(alias_phrase)
