from bs4 import BeautifulSoup as bs
import requests
from github import Github

# Step 1: Extract text from a webpage and save it to a file
response = requests.get("https://en.wikipedia.org/wiki/Tablet_(pharmacy)")
soup = bs(response.text, 'html.parser')
plain_text = soup.get_text()

file_name = "wikipedia_tablet_pharmacy.txt"

with open(file_name, 'w', encoding='utf-8') as file:
    file.write(plain_text)

print(f'Text content saved to {file_name}')

# Step 2: Upload the file to GitHub
# Note: Replace your token with an appropriate token for security reasons.
g = Github("Github-Token")

# Get the authenticated user
user = g.get_user()

# Create a new repository named "demo"
repo = user.create_repo("demo")

# Read the content of the file
with open(file_name, 'r', encoding='utf-8') as file:
    content = file.read()

# Create a new file in the repository with the extracted text
repo.create_file(file_name, "Initial commit - Added wikipedia text", content)

print(f'File {file_name} has been uploaded to the GitHub repository "demo".')
