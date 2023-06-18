# Python, Boto3, and AWS S3 Practice

### ✨ Boto3
Boto3 is the name of the Python SDK for AWS. It allows you to directly create, update, and delete AWS resources from your Python scripts. <br>
To run you must have **boto3** installed: <br>
`$ pip install boto3`

### ✨ Client Versus Resource
At its core, all that Boto3 does is call AWS APIs on your behalf. For the majority of the AWS services, Boto3 offers two distinct ways of accessing these abstracted APIs:

- Client: low-level service access <br>
- Resource: higher-level object-oriented service access

- Boto3 generates the client and the resource from different definitions:_
- Boto3 generates the client from a JSON service definition file. The client’s methods support every single type of interaction with the target AWS service.
- Resources, on the other hand, are generated from JSON resource definition files.

With clients, there is more programmatic work to be done. The majority of the client operations give you a dictionary response. To get the exact information that you need, you’ll have to parse that dictionary yourself. With resource methods, the SDK does that work for you.

### ✨ Naming Your Files
In case of hosting a large number of files in your S3 bucket, keep this in mind. <br>
If all your file names have a deterministic prefix that gets repeated for every file, such as a timestamp format like _`YYYY-MM-DDThh:mm:ss`_, then you will soon find that you’re running into **performance issues** when you’re trying to interact with your bucket. <br>
>Because S3 takes the prefix of the file and maps it onto a partition. The more files you add, the more will be assigned to the same partition, and that partition will be very heavy and less responsive.<br>
>The easiest solution is to randomize the file name. By adding randomness to your file names, you can efficiently distribute your data within your S3 bucket. <br>

### ✨ Creating Buckets And Object Instances
💡 ️**How to integrate it into your S3 workflow:** &nbsp;&nbsp;&nbsp;&nbsp;

This is where the resource’s classes play an important role, as these abstractions make it easy to work with S3.
By using the resource, you have access to the high-level classes (Bucket and Object)

> Boto3 doesn’t make calls to AWS to create the reference (object instances). The bucket_name and the key are called identifiers, 
> and they are the necessary parameters to create an Object. Any other attribute of an Object, such as its size, is lazily loaded. 
> This means that for Boto3 to get the requested attributes, it has to make calls to AWS.

### ✨ Uploading A File
There are three ways you can upload a file:
- From an Object instance
- From a Bucket instance
- From the client

### ✨ Downloading A File
To download a file from S3 locally, you’ll follow similar steps as you did when uploading. But in this case, the Filename parameter will map to your desired local path

### ✨ Copying/Delete An Object Between Buckets
If you need to copy files from one bucket to another, Boto3 offers you that possibility using `.copy()` <br>
And delete an object using `.delete()`

## 💫✨💥 Advanced Configuration
### 💥 ACL (Access Control Lists)
Access Control Lists (ACLs) help you manage access to your buckets and the objects within them. They are considered the **legacy way of administrating permissions to S3**. <br>
By default, when you upload an object to S3, that object is private. You can set the object’s ACL to be public at creation time


### ✨ Blockers Solved
1. Invalid access token of while trying to create S3 bucket under IAM user
   * With AWS cli installed, manage user access token granted for 'Other' <br>
   * Checking aws configuration using `aws configure list`, `aws sts get-caller-identity`
2. Bucket name convention
3. Bucket permissions with ACL enabled in case making any ACL update. Make sure to un-check `Block public access` if you need to change the object into `public-read`



![Screenshot 2023-06-14 at 17.58.57.png](..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Ffp%2Fbrc1mdxj6876kynp0m3sdnlntsg1h6%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_WOdE95%2FScreenshot%202023-06-14%20at%2017.58.57.png)