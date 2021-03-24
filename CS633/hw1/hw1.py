"""
Write a python script that
(a) reads the AWS credentials from a file named awskeys
(b) prompts the user for his/her name,
(c) creates a text file locally to store the user's name,
(d) uploads it to Amazon S3
(e) reads the file back and displays the name from the file
(f) deletes the file from Amazon S3 storage.
"""
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
import boto3

# a
creds = open('awskeys.txt', 'r')
key1 = creds.readline()
key2 = creds.readline()

s3 = boto3.resource('s3')
b_name = 'john-robertson-bucket-1'
s3.create_bucket(Bucket=b_name)
bucket = s3.Bucket(b_name)

# b
u_name = input("Your name: ")

# c
f_name = 'u_name.txt'
f = open(f_name, 'w')
f.write(u_name)


# d
f.close()
s3client = boto3.client('s3')
s3client.upload_file(f_name, b_name, f_name)

# e
for obj in bucket.objects.all():
    key = obj.key
    body = obj.get()['Body'].read().decode('utf-8')
    print(body)

# f
s3.Object(b_name, 'u_name.txt').delete()
