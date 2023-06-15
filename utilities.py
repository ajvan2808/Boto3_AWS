import os.path
import uuid
import boto3
from boto3 import session


# To connect to the high-level interface, you’ll follow a similar approach, but use resource()
# To connect to the low-level client interface, you must use Boto3’s client().
# You then pass in the name of the service you want to connect to

# BUT you can access the client directly via the resource like so:
''' `s3_resource.meta.client` '''
# Unless your region is in the United States, you’ll need to define the region explicitly
# when you are creating the bucket. Otherwise, you will get an `IllegalLocationConstraintException`

s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')


def create_s3_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return '-'.join([bucket_prefix, str(uuid.uuid4())])


def create_bucket(bucket_prefix, s3_connection) -> tuple:
    """
    :param bucket_prefix: str, bucket name prefix
    :param s3_connection: connection to s3 client/resource interface
    :return: tuple, full bucket name and response

    Ex responses:
    from resource: s3.Bucket(name='secondpythonbucket-b376e0...')
    from client: {'ResponseMetadata': {'RequestId': 'E1DCFE71EDE7C1EC', 'HostId': '..',
                    'HTTPStatusCode': 200, 'HTTPHeaders': etc...}
    """

    session_ = boto3.session.Session()
    current_region = session_.region_name
    bucket_name = create_s3_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(Bucket=bucket_name,
                                                  CreateBucketConfiguration={'LocationConstraint': current_region})
    # print(bucket_name, current_region, bucket_response)
    return bucket_name, bucket_response


def create_temp_file(size, file_name, file_content) -> str:
    """
    This allows you to pass in the number of bytes you want the file to have, the file name,
    and a sample content for the file to be repeated to make up the desired file size
    :param size: int, desired size
    :param file_name: str
    :param file_content: str, sample content
    :return: str, random file name
    """

    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(file_name, 'w') as f:
        f.write(file_content * size)

    return random_file_name

# first_file_name = create_temp_file(300, 'firstfile.txt', 'f')


# Creating bucket and object instances
def create_bucket_and_obj_instances(buck_name, file_to_integrate):
    """
    Bucket and Object are sub-resources of one another.
    Sub-resources are methods that create a new instance of a child resource.
    The parent’s identifiers get passed to the child resource.

    :param buck_name:
    :param file_to_integrate:
    :return:
    """
    s3_buck = s3_resource.Bucket(name=buck_name)
    first_object = s3_resource.Object(bucket_name=buck_name, key=file_to_integrate)

    # Create object directly from bucket variable
    # _another_object = s3_buck.Object(file_to_integrate)
    # Or get the bucket from the object
    # _get_bucket = first_object.Bucket()

    return s3_buck, first_object


# UPLOADING
def upload_file_to_s3(file_name, object_instance):
    """ Filename, which is the path of the file you want to upload
    - Using Object instance
    s3_resource.Object(bucket_name, file_name).upload_file(Filename=os.path.abspath(file_name))

    - Using Bucket instance
    s3_resource.Bucket(bucket_name).upload_file(Filename=os.path.abspath(file_name), Key=file_name)

    - Using the client
    s3_resource.meta.client.upload_file(Filename=os.path.abspath(file_name), Bucket=bucket_name, Key=file_name)
    """

    # Directly by the object instance
    return object_instance.upload_file(file_name)


# DOWNLOADING
def download_file_from_s3(bucket_name, file_name):
    # Filename parameter will map to your desired local path
    cur_dir = os.getcwd()
    return s3_resource.Object(bucket_name, file_name).download_file(f'{cur_dir}/tmp/{file_name}')


# COPYING
def copy_object_to_bucket(from_bucket, to_bucket, file_name):
    from_source = {
        'Bucket': from_bucket,
        'Key': file_name
    }

    return True if s3_resource.Object(to_bucket, file_name).copy(from_source) else False


# DELETING
def delete_object(bucket_name, file_name):
    return True if s3_resource.Object(bucket_name, file_name).delete() else False


# ACCESS CONTROL LIST (ACL)
def access_control_config(bucket):
    """
    - Uploading an object to S3, that object is private by default. To set the object’s ACL to be public at creation time
      Use `ExtraArgs={'ACL': 'public-read'}` attribute to make it accessible for everyone
    :return:
    """
    second_file = create_temp_file(200, 'acl-s3-temp.txt', 'h')
    second_object = s3_resource.Object(bucket.name, second_file)
    second_object.upload_file(second_file, ExtraArgs={'ACL': 'public-read'})

    # You can get the ObjectAcl instance from the Object, as it is one of its sub-resource classes
    second_object_acl = second_object.Acl()

    # To see who has access to your object, use the grants attribute
    _grants = second_object_acl.grants

    # Make your object private, without needing to re-upload
    _response = second_object_acl.put(ACL='private')

    return second_object_acl