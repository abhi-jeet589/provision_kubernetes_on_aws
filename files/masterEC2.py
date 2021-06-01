#!/usr/bin/python3
import boto3
import os
numberOfMasters = int(os.environ.get('NUMBER_OF_MASTERS'))
ec2Client = boto3.client('ec2')
responseMaster = ec2Client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                'Ansible-Kube-Master',
            ]
        },
        {
            'Name': 'instance-state-name',
            'Values':[
                 'running',
                ]
        },
    ],
    MaxResults = 100
)
for i in range(numberOfMasters):
    print(responseMaster['Reservations'][0]['Instances'][i]['PublicIpAddress'])
