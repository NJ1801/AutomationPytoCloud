from bs4 import BeautifulSoup as bs
import requests
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Web scraping part
response = requests.get("https://en.wikipedia.org/wiki/Academy_Awards")
soup = bs(response.text, 'html.parser')
plain_text = soup.get_text()

# Local file path
file_path = r"D:\Nj\Learning\seachflask\autowebscrap\wiki.txt"

# Save the scraped content to a text file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(plain_text)
print(f"Successfully saved into {file_path}")

# Azure Blob Storage part

# Replace with your connection string
connection_string = "DefaultEndpointsProtocol=https;AccountName={ACCOUNTNAME};AccountKey={ACCOUNTKEY};EndpointSuffix=core.windows.net"

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Replace with your container name
container_name = "pozent"
container_client = blob_service_client.get_container_client(container_name)

# Upload the file to Azure Blob Storage
blob_client = container_client.get_blob_client("wiki.txt")
with open(file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print("File Successfully Uploaded into Azure Blob Storage")

# List all blobs in the container
print("\nList of blobs in the container:")
blob_list = container_client.list_blobs()
for blob in blob_list:
    print(f" - {blob.name}")

# Download the file content from Azure Blob Storage
downloaded_blob = blob_client.download_blob().readall()
file_content = downloaded_blob.decode('utf-8')
print("\nDownloaded file content:\n")
#print(file_content)
print("Successfully file readed from Azure")