"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket-asad-pulumi')

bucketObject = s3.BucketObject(
    'index.html',
    bucket=bucket,
    source=pulumi.FileAsset('index.html')
)

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
