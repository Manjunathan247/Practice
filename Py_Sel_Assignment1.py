import logging
import time
import datetime

start = time.time()
logging.basicConfig(level=logging.INFO)
print("Date and Timestamp:", datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S"))

logging.info("Open names file")

with open("names.txt", "r") as f:
    namesList = []
    logging.info("read the names from file and converting into lowercase")
    namesList = f.read().replace(" ", "_").lower().split()
    print(namesList)


# function to create an email
def email(namesList):
    return namesList + "@pydemo.com"


names_updated = list(map(email, namesList))
print(names_updated)

# Remove duplicate mail ids using set function
unique_mails = list(set(names_updated))
print(unique_mails)

with open("names_updated.txt", "w") as f2:
    for mail in unique_mails:
        f2.write(mail + '\n')

print("Time taken to execute the script is : ", time.time() - start)