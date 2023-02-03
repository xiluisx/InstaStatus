from instagrapi import Client
from getpass import getpass
import schedule
import random

# Load the list of status
bios = []
with open('bios.txt') as file:
    bios = [line.rstrip() for line in file]

for i in bios:
    print(i)

# Login user
username = input("Type username: ")
password = getpass()

cl = Client()
cl.login(username, password)

# Clear up fields
username = ""
password = ""

def set_random_bio():
    random_bio = random.choice(bios)
    cl.account_set_biography(random_bio)
    return

schedule.every().day.at("01:00").do(set_random_bio)
