import boto3
from utilities import create_bucket

# To connect to the high-level interface, you’ll follow a similar approach, but use resource()
s3_resource = boto3.resource('s3')

# To connect to the low-level client interface, you must use Boto3’s client().
# You then pass in the name of the service you want to connect to
s3_client = boto3.client('s3')
# BUT you can access the client directly via the resource like so:
''' `s3_resource.meta.client` '''

# Unless your region is in the United States, you’ll need to define the region explicitly
# when you are creating the bucket. Otherwise, you will get an `IllegalLocationConstraintException`


if __name__ == '__main__':
    client_bucket_name, client_bucket_response = create_bucket(bucket_prefix='firstpythonbucket',
                                                               s3_connection=s3_resource.meta.client)