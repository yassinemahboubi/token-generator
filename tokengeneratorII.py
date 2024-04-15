import secrets
import requests, threading, os, sys, time, random, os.path
import string

os.system('title Mail Access Checker - By spider_no_limit')

logo = """   
   _____       _     __                             ___           _ __
  / ___/____  (_)___/ /__  _____  ____  ____       / (_)___ ___  (_) /_
  \__ \/ __ \/ / __  / _ \/ ___/ / __ \/ __ \     / / / __ `__ \/ / __/
 ___/ / /_/ / / /_/ /  __/ /    / / / / /_/ /    / / / / / / / / / /_
/____/ .___/_/\__,_/\___/_/____/_/ /_/\____/____/_/_/_/ /_/ /_/_/\__/
    /_/                  /_____/          /_____/   """

def generate_token(length=20):
    """Generate a random token."""
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for _ in range(length))
    return token

def save_tokens_to_file(num_lines, filename):
    """Generate random tokens and save them to a file."""
    with open(filename, 'w') as file:
        for _ in range(num_lines):
            token = generate_token()
            file.write(token + '\n')

# ch7al mn line f dial tokens / smiya t txt
def main():
  os.system('cls')
print(f"\n{logo}\n")
num_lines = int(input("number of lines generated : "))
filename = input("Enter the name of the text file: ")


save_tokens_to_file(num_lines, filename)
print(f"{num_lines}tokens saved to {filename}.")
