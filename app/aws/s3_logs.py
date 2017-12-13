import boto3
import gzip
import os

# Get AWS environment variables
aws_key = os.getenv("AWS_KEY", False)
aws_secret = os.getenv("AWS_SECRET", False)
aws_region = os.getenv("AWS_REGION", False)

# Check if the environment variables are defined
if not aws_key or not aws_secret or not aws_region:
    print('************ ERROR: check your AWS environment variables ***************')
    exit()

# The full s3 client syntax can be helpful if dealing with more than one region
s3 = boto3.client('s3', region_name=aws_region, aws_access_key_id=aws_key, aws_secret_access_key=aws_secret)

def list_objects(bucket, prefix):
    try:
        obj_list = s3.list_objects(Bucket=bucket, Prefix=prefix)['Contents']
        file_list = list(filter(lambda x: '.log' in x, list(map(lambda x: x['Key'], obj_list))))
        return file_list
    except Exception as e:
        print(e)
        exit()

def read_object(bucket, key):
    log_object = {
        'Type': '',
        'Content': []
    }

    if '.gz' in key:
        try:
            # Define the log type
            log_object['Type'] = 'ALB'

            # Read the contentent of the compressed object from S3
            obj = s3.get_object(Bucket=bucket, Key=key)
            compressed = obj['Body'].read()

            # Store to temporary file to use gzip
            file = open('tmp_file', 'w')
            file.write(compressed)
            file.close()

            # Use gzip tp read the compressed content
            with gzip.open('tmp_file') as log:
                log_object['Content'] = list(filter(lambda x: len(x), log.read().split('\n')))
                return log_object
        except Exception as e:
            print(e)
            exit()

    else:
        try:
            # Define the log type
            log_object['Type'] = 'ELB'

            # Read the content from the S3 object
            obj = s3.get_object(Bucket=bucket, Key=key)
            log_object['Content'] = list(filter(lambda x: len(x), obj['Body'].read().split('\n')))
            return log_object
        except Exception as e:
            print(e)
            exit()

def delete_object(bucket, key):
    try:
        response = s3.delete_object(
            Bucket=bucket,
            Key=key,
        )
        print response
    except Exception as e:
        print(e)
        exit()
