import boto3
from aws_wrapper import print_buckets
from aws_wrapper import upload_file,bucketlist,createbucket
s3_obj = boto3.resource('s3')

#print_buckets(s3_obj)
file_path = 'demofile.txt'

#upload_file(s3_obj,'demofile.txt','pythonfordevops3',file_path)
bucketlist(s3_obj,"pythonfordevops3")
#createbucket(s3_obj,"pythonfordevops2")

