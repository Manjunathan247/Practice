import logging
import time
import datetime

start_time = time.time()
logging.basicConfig(filename='assignmentOne.log', filemode='a', level=logging.INFO,
                    datefmt='%d-%b-%y %H:%M:%S', format='%(asctime)s - %(levelname)s: %(message)s')
print("Date and Timestamp:", datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S"))

domain = "@pydemo.com"

logging.info("Open file which contains names")
with open("names.txt", "r") as f:
    namesList = []
    logging.info("Read the names from file and converting into lowercase")
    namesList = f.read().replace(" ", "_").lower().split()
    print(namesList)


def email(names):
    return names + domain


logging.info("Create mail id")

names_updated = list(map(email, namesList))
print(names_updated)

logging.info("Remove duplicate mail ids")
unique_mails = set(names_updated)
print(unique_mails)

with open("names_updated.txt", "w") as f2:
    for mail in unique_mails:
        f2.write(mail + '\n')
end_time = time.time()
print("Program executed in :", (end_time - start_time), "seconds")
