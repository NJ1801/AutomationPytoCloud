# Web Scrap code 
from bs4 import BeautifulSoup as bs
import requests

response = requests.get("https://en.wikipedia.org/wiki/Academy_Awards")
soup = bs(response.text,'html.parser')
#print(soup)
plain_text = soup.get_text()
#print(plain_text)

file_path =r"D:\Nj\Learning\seachflask\autowebscrap\wiki.txt"

with open(file_path,'w',encoding='utf-8')as file:
    file.write(plain_text)
print(f"Successfully saved into {file_path}")

#file upload into AWS 
import boto3

# Create an S3 resource using the keys from environment variables
s3 = boto3.resource(
    's3',
    aws_access_key_id='accesskey',
    aws_secret_access_key='secretaccesskey'
)

# Upload the file
s3.meta.client.upload_file(
    r"D:\Nj\Learning\seachflask\autowebscrap\wiki.txt",
    'mypozentbucket',#Bucketname 
    'wiki.txt' #folder/filename - Gif/pozent.png, filename - pozent.png
)

print("File Successfully Uploaded into AWS")


# file read from AWS 
for bucket in s3.buckets.all():
    print(bucket.name)

bucket_objects = bucket.objects.all()
for obj in bucket_objects:
    print(f" - {obj.key}")

bucke = s3.Bucket('mypozentbucket')

file_obj = bucket.Object('wiki.txt').get()

file_content = file_obj['Body'].read().decode('utf-8')
print(file_content)
