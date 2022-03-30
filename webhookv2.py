from turtle import title
import requests

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{colors.OKGREEN} __   __ __ __  __  __        __ __      __  __      ___ __   ___ __ __  {colors.ENDC}")
print(f"{colors.OKGREEN}|  \|(_ /  /  \|__)|  \  |  ||_ |__)|__|/  \/  \|_/   | |_ \_/ | |_ |__) {colors.ENDC}")
print(f"{colors.OKGREEN}|__/|__)\__\__/| \ |__/  |/\||__|__)|  |\__/\__/| \   | |__/ \ | |__| \  {colors.ENDC}")
print(f"{colors.OKGREEN}                                                                         {colors.ENDC}")



print(f"{colors.OKBLUE}--------------------------------------------------{colors.ENDC}")
print(f"{colors.OKCYAN}pls enter username{colors.ENDC}")
user = input("> ")
print("")
print(f"{colors.OKCYAN}pls enter webhook URL{colors.ENDC}")
url = input("> ")
print(f"{colors.OKBLUE}--------------------------------------------------{colors.ENDC}")
print(f"{colors.OKCYAN}Title pls{colors.ENDC}")
title1 = input("> ")
print(f"{colors.OKCYAN}Description pls{colors.ENDC}")
desc = input("> ")


while (True):
    data = {
        "content" : "",
        "username" : user
    }


    data["embeds"] = [
        {
            "description" : desc,
            "title" : title1
        }
    ]

    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print(f"{colors.UNDERLINE}Message Sent!{colors.ENDC}")
        #print("Payload delivered successfully, code {}.".format(result.status_code))
        print("")
        print(f"{colors.OKCYAN}Title pls{colors.ENDC}")
        title1 = input("> ")
        print(f"{colors.OKCYAN}Description pls{colors.ENDC}")
        desc = input("> ")