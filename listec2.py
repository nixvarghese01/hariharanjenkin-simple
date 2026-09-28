import boto3


def list_instances(region="ap-south-1"):
    client = boto3.client("ec2", region_name=region)
    paginator = client.get_paginator("describe_instances")

    for page in paginator.paginate():
        for reservation in page.get("Reservations", []):
            for instance in reservation.get("Instances", []):
                name = next(
                    (
                        tag["Value"]
                        for tag in instance.get("Tags", [])
                        if tag.get("Key") == "Name"
                    ),
                    "-",
                )
                print(
                    f"{instance['InstanceId']}\t"
                    f"{instance.get('InstanceType', '-')}\t"
                    f"{instance.get('LaunchTime', '-')}\t"
                    f"{instance.get('State', {}).get('Name', '-')}\t"
                    f"{name}"
                )


if __name__ == "__main__":
    print("Instance ID\tType\tLaunch time\tState\tName")
    list_instances()
