import os
from aws import s3_logs
from parser import parse_log
from elasticsearch import elasticsearch
import json

# # Get configuration from environment variables
s3_bucket = os.getenv('BUCKET_NAME', False)
s3_prefix = os.getenv('PREFIX', False)


while True:
    # Get list of objects in s3 from bucket/prefix
    log_files = s3_logs.list_objects(s3_bucket, s3_prefix)

    # Iterate through list of files
    for log_file in log_files:

        # Read the file from S3
        log = s3_logs.read_object(s3_bucket, log_file)

        # Parse ALB or ELB log depending on type and save to elasticsearch
        if log['Type'] == 'ALB':
            print 'ALB'
            for entry in log['Content']:
                elasticsearch.put_document('logs', 'alb', json.dumps(parse_log.alb(entry)))
        if log['Type'] == 'ELB':
            print 'ELB'
            for entry in log['Content']:
                elasticsearch.put_document('logs', 'elb', json.dumps(parse_log.elb(entry)))

        # Delete the log file after finishing
        s3_logs.delete_object(s3_bucket, log_file)

