#!/usr/bin/python3
import boto3
import os
numberOfSlaves = int(os.environ.get('NUMBER_OF_SLAVES'))
ec2Client = boto3.client('ec2')
responseSlave = ec2Client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                "Ansible-Kube-Slave"
            ]
        },
        {
            'Name': 'instance-state-name',
            'Values': [ "running" ]
        },

    ],
    MaxResults = 100 
)
#print(responseSlave)
for j in range(numberOfSlaves):
   print(responseSlave['Reservations'][0]['Instances'][j]['PublicIpAddress'])
