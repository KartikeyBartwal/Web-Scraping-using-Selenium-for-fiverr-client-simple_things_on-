from selenium import webdriver
import time
import re

# driver = webdriver.Chrome()

# url = "https://www.oehv.at/mitglieder/hotelverzeichnis/?filter.sortOrder=ASC&page=1"

# driver.get(url)
# time.sleep(20)

# page_source_given = False 
# while(True):
#     print("Entered the while block")
#     if(page_source_given == False):
#         page_source = driver.page_source 
#         with open("page_source.txt", "w", encoding="utf-8") as file:
#             file.write(page_source)
#             page_source_given = True 
#     pass
# driver.quit()


with open("page_source.txt", "r", encoding="utf-8") as file:
    file_content = file.read()

print(file_content)

# Find all occurrences of email addresses using the regex pattern
REGEX_EMAIL = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Find all occurrences of email addresses using the regex pattern in the file content
email_addresses = re.findall(REGEX_EMAIL, file_content)

# Print the extracted email addresses
for email in email_addresses:
    print(email)