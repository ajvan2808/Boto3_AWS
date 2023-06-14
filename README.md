# Python, Boto3, and AWS S3 Practice

### 1. Boto3
Boto3 is the name of the Python SDK for AWS. It allows you to directly create, update, and delete AWS resources from your Python scripts. <br>
To run you must have **boto3** installed: <br>
`$ pip install boto3`

### 2. Client Versus Resource
At its core, all that Boto3 does is call AWS APIs on your behalf. For the majority of the AWS services, Boto3 offers two distinct ways of accessing these abstracted APIs:

- Client: low-level service access <br>
- Resource: higher-level object-oriented service access

- Boto3 generates the client and the resource from different definitions:_
- Boto3 generates the client from a JSON service definition file. The client’s methods support every single type of interaction with the target AWS service.
- Resources, on the other hand, are generated from JSON resource definition files.

With clients, there is more programmatic work to be done. The majority of the client operations give you a dictionary response. To get the exact information that you need, you’ll have to parse that dictionary yourself. With resource methods, the SDK does that work for you.

### 3. Blockers Solved
1. Invalid access token of while trying to create S3 bucket under IAM user
   * With AWS cli installed, manage user access token granted for 'Other' <br>
   * Checking aws configuration using `aws configure list`, `aws sts get-caller-identity`
2. Bucket name convention

![Screenshot 2023-06-14 at 17.58.57.png](..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Ffp%2Fbrc1mdxj6876kynp0m3sdnlntsg1h6%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_WOdE95%2FScreenshot%202023-06-14%20at%2017.58.57.png)