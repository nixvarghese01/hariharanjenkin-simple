# This is program is for listing VPC

import boto3

client = boto3.client('ec2', region_name = "us-west-2", aws_access_key_id = "AKIAREDACTED", aws_secret_access_key = "REDACTED")

list_VPC_response = client.describe_vpcs()
#print (list_VPC_response['Vpcs'])
for i in list_VPC_response['Vpcs']:
	print (i['VpcId'], i['CidrBlock'])
