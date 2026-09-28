# hariharanjenkin-simple: AWS Automation with Python, Terraform and Jenkins

A collection of AWS automation scripts (boto3), Terraform and CloudFormation templates, and Jenkins pipelines that run them.

## Contents
| File | Purpose |
|---|---|
| `Jenkinsfile.groovy`, `pipeline.groovy` | Parameterised Jenkins pipelines that clone the repo and run the scripts |
| `Jenkins_pipeline_script.py` | IAM access-key report (takes the key and secret as arguments) |
| `ins-new.py` | Launch EC2 instances (region and credentials as arguments) |
| `listec2.py` | List EC2 instances |
| `boto3_list_vpc.py` | List VPCs |
| `vpc_Automation_using_Python.py` | Interactive VPC creation |
| `policy.py` | IAM policy helper |
| `main.tf`, `variable.tf` | Terraform: VPC, two subnets, internet gateway, route table |
| `ec2-withsecgroup` | CloudFormation: EC2 instance with a security group |
| `helloworld.java`, `sample/` | Sample Java file |

## Credentials
The scripts **don't contain credentials**. They use the standard AWS credential chain, so configure one of these before running them:
```bash
aws configure                      # or
export AWS_ACCESS_KEY_ID=... AWS_SECRET_ACCESS_KEY=...
```
In Jenkins, store keys as **Credentials** and bind them with `withCredentials`, not as plain string parameters.

## Run
```bash
pip install boto3
python listec2.py

terraform init && terraform apply
```
