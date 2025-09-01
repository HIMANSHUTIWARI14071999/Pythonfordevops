def print_buckets(s3_obj):
    for buckets in s3_obj.buckets.all():
        print(buckets.name)

def upload_file(s3_obj,file_name,bucket_name,file_path):
    file_obj = open(file_path,'rb')
    s3_obj.Bucket(bucket_name).put_object(Key=file_name,Body=file_obj)
    file_obj.close()

def bucketlist(s3_obj,bucket_name):
    print(f"The objects in s3 Bucket {bucket_name} are:")
    for object in s3_obj.Bucket(bucket_name).objects.all():
        print(object.key)
        
def createbucket(s3_object,bucket_name):
    s3_object.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint':'ap-south-1'})
    print(f"Bucket {bucket_name} created successfully")
    