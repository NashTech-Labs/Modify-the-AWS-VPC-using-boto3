# MuZakkir Saifi
# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

REGION = input("Please enter the REGION")

# this is the configration for the logger_for

logger_for = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

client_for_VPC= boto3.client("ec2", region_name=REGION)


def modify_vpc(id, dns):
   
    try:
        res = client_for_VPC.modify_vpc_attribute(
            EnableDnsSupport={'Value': dns}, VpcId=id)
# This modify_vpc_attribute() will not return any type of output when it is done successful.

    except ClientError:
        logger_for.exception('This can not be modify.')
        raise
    else:
        return res


if __name__ == '__main__':
    VPC_ID = input("Enter the VPC ID")
    enableDnsSupport = True # input("Enter your answer in True or Flase: ")
    attribute = modify_vpc(VPC_ID, enableDnsSupport)
    logger_for.info(
        f'Your VPC has been modified. New value: {enableDnsSupport}'
    )