import re

# Read the file
with open('your_file_name', 'r') as file:
    content = file.read()


email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'


emails = re.findall(email_regex, content)

# Printing the extracted email addresses
print("Found email addresses:")
for email in emails:
    print(email)
