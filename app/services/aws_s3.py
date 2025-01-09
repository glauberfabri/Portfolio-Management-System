import boto3

def upload_file(file_path, bucket):
    s3 = boto3.client("s3")
    s3.upload_file(file_path, bucket, os.path.basename(file_path))