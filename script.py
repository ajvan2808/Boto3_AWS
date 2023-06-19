import os
from dotenv import load_dotenv
import boto3
from utilities import (create_bucket, create_temp_file,
                       create_bucket_and_obj_instances, upload_file_to_s3,
                       download_file_from_s3, copy_object_to_bucket, delete_object,
                       encrypt_object_and_storage, versioning_bucket,
                       get_object_version_id, fetch_buckets, fetch_objects,
                       del_objects, del_bucket)
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
    file_name = create_temp_file(100, 'temp_file_2.txt', 'Ny ')
    file_name_2 = create_temp_file(100, 'temp_file_3.txt', 'Haha ')
    print(file_name)

    # Create instances of bucket and object
    first_bucket_inst, first_object_inst = create_bucket_and_obj_instances(FIRST_S3_BUCKET_NAME, 'temp_file.txt')
    s3_resource.Object(FIRST_S3_BUCKET_NAME, 'temp_file.txt').upload_file('temp_file_3.txt')
    print(first_bucket_inst, first_object_inst)

    # Upload file
    upload_file_to_s3('temp_file.txt', first_object_inst)

    # Download the file
    download_file_from_s3(FIRST_S3_BUCKET_NAME, 'temp_file.txt')

    # Copying object to another bucket
    copy_object_to_bucket(first_bucket_name, SECOND_S3_BUCKET_NAME, 'temp_file.txt')

    # Delete an Object
    delete_object(FIRST_S3_BUCKET_NAME, 'temp_file.txt')

    # Object ACL
    first_object_acl = first_object_inst.Acl()
    print(first_object_acl)
    print(first_object_acl.grants)

    # make your object private/public again, without needing to re-upload it
    update_request = first_object_acl.put(ACL='public-read')

    # Encrypt files/object and define storage class
    encrypt_request = encrypt_object_and_storage(first_object_inst)

    # Versioning bucket
    print(versioning_bucket(FIRST_S3_BUCKET_NAME))
    # return the latest available version of your objects
    print(get_object_version_id(s3_resource.Object(FIRST_S3_BUCKET_NAME, 'temp_file.txt')))

    # Retrieve buckets and objects
    fetch_buckets()
    print(fetch_objects(first_bucket_inst))

    # Delete Objects and Buckets
    del_objects(FIRST_S3_BUCKET_NAME)   # with versioned objects
    del_objects(SECOND_S3_BUCKET_NAME)  # non-versioned objects

    del_bucket(SECOND_S3_BUCKET_NAME)
