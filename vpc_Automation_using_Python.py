import boto3

client = boto3.client('ec2', region_name="ap-south-1")

print ("Enter the CIDR For VPC:")
vpc_cidr = input()
create_vpc = client.create_vpc(CidrBlock=vpc_cidr)
print (create_vpc['Vpc']['VpcId'])
vpcid = create_vpc['Vpc']['VpcId']

print ("Enter the CIDR For Subnet:")
subnet_cidr = input()
create_subnet = client.create_subnet(CidrBlock=subnet_cidr,VpcId=vpcid)
subnetid = create_subnet['Subnet']['SubnetId']
print(subnetid)

# TODO: create and attach an internet gateway
# TODO: create a route table and associate it with the subnet
