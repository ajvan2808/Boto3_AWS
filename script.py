import os
from dotenv import load_dotenv
import boto3
from utilities import (create_bucket, create_temp_file,
                       create_bucket_and_obj_instances, upload_file_to_s3,
                       download_file_from_s3, copy_object_to_bucket, delete_object)
from utilities import s3_resource

load_dotenv()
FIRST_S3_BUCKET_NAME = os.getenv('FIRST_S3_BUCKET_NAME')
SECOND_S3_BUCKET_NAME = os.getenv('SECOND_S3_BUCKET_NAME')

if __name__ == '__main__':
    first_bucket_name, first_bucket_response = create_bucket(bucket_prefix='firstpythonbucket',
                                                             s3_connection=s3_resource)
    # client_bucket_name, client_bucket_response = create_bucket(bucket_prefix='secondpythonbucket',
    #                                                            s3_connection=s3_resource.meta.client)

    # Get temp file
    file_name = create_temp_file(200, 'temp_file.txt', 'sunny ')
    print(file_name)

    # Create instances of bucket and object
    first_bucket_inst, first_object_inst = create_bucket_and_obj_instances(first_bucket_name, 'temp_file.txt')
    print(first_bucket_inst, first_object_inst)

    # Upload file
    upload_file_to_s3('temp_file.txt', first_object_inst)

    # Download the file
    download_file_from_s3(FIRST_S3_BUCKET_NAME, 'temp_file.txt')

    # Copying object to another bucket
    copy_object_to_bucket(first_bucket_name, SECOND_S3_BUCKET_NAME, 'temp_file.txt')

    # Delete an Object
    delete_object(FIRST_S3_BUCKET_NAME, 'temp_file.txt')
