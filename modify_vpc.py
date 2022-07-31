# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = input("Please enter the AWS_REGION")

# this is the configration for the logger

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_client = boto3.client("ec2", region_name=AWS_REGION)


def modify_vpc(vpc_id, dns_support):
   
    try:
        response = vpc_client.modify_vpc(
            EnableDnsSupport={'Value': dns_support}, VpcId=vpc_id)

    except ClientError:
        logger.exception('This can not be modify.')
        raise
    else:
        return response


if __name__ == '__main__':
    # VPC_ID = 'vpc-073f1851ba2a97029'
    VPC_ID = input("Enter the VPC ID")
    enableDnsSupport = True
    vpc_attribute = modify_vpc(VPC_ID, enableDnsSupport)
    logger.info(
        f'Your VPC has been modified. New value: {enableDnsSupport}'
    )