import hashlib as hb
import argparse as ae
import pandas as pd
import os
import sys
from colorama import Fore, init
# Auto reset colors
init(autoreset=True)

algorithms = ['sha256.', 'sha224.', 'sha3_224.', 'sha384', 'shake_128', 'shake_256', 'sha3_384', 'md5', 'sha1', 'sha3_256', 'blake2b', 'blake2s', 'sha3_512', 'sha512']
IDs = [ID for ID in range(1, len(algorithms)+1)]

# list_modules function is responsible for listing all available hashing algorithms alongside their IDs.
# Pandas module is used to convert data into DataFrame in order to list them as a table. 
def list_modules():
    data = pd.DataFrame({'Algorithm':algorithms, 'ID':IDs})
    data.set_index('Algorithm', inplace=True)
    print(data)

# argparse module is used to parse command-line arguments.
ar = ae.ArgumentParser(description="This tool can be used to carry out certain hashing functionality against an input plaintext")
ar.add_argument('-p', '--PlainText', help='The plain text to be hashed.', required=False)
ar.add_argument('-a','--Algorithm',type = int, help='The hashing algorithm ID to be used.', required=False)
ar.add_argument('-m', '--Modules',action='store_true', help='List all available hashing algorithms along with their IDs.', required=False)
ar.add_argument('-b', '--Bruteforcing', help='To enable bruteforcing mode.', required=False, action='store_true')
ar.add_argument('-d', '--Dictionary', help='Provide a wordlist to be used with bruteforcing.', required=False)
ar.add_argument('-c', '--Hash', help='Hashed text', required=False)
arg = ar.parse_args()
# If the user wanna list modules, then he will set the flag `Modules` so it will be equal to True or logical 1. 
if arg.Modules:
    list_modules()
    sys.exit(0)
# To ensure that the command provided by user is a legal command from a logical point of view.
if not ((arg.Algorithm and arg.PlainText and not arg.Bruteforcing and not arg.Hash and not arg.Dictionary) or (arg.Bruteforcing and arg.Algorithm and arg.Dictionary and arg.Hash and not arg.PlainText)):
    print(Fore.RED+"You have entered an illegal command!")
    sys.exit(1)
# To ensure that the user enter an Algorithm ID which exists.
if not (arg.Algorithm in IDs):
    print(Fore.RED+'You have specified an illegal algorithm ID.',Fore.RESET+'\nAvailable algorithms:\n')
    list_modules()
    sys.exit(404)
ID = arg.Algorithm

# This function is responsible for generating hexdigests based on the user input.
def hash_return(plainText):
    if ID == 1: return hb.sha256(plainText.encode()).hexdigest()
    elif ID == 2: return hb.sha224(plainText.encode()).hexdigest()
    elif ID == 3: return hb.sha3_224(plainText.encode()).hexdigest()
    elif ID == 4: return hb.sha384(plainText.encode()).hexdigest()
    elif ID == 5: return hb.shake_128(plainText.encode()).hexdigest(length=128)
    elif ID == 6: return hb.shake_256(plainText.encode()).hexdigest(length=256)
    elif ID == 7: return hb.sha3_384(plainText.encode()).hexdigest()
    elif ID ==8: return hb.md5(plainText.encode()).hexdigest()
    elif ID == 9: return hb.sha1(plainText.encode()).hexdigest()
    elif ID == 10: return hb.sha3_256(plainText.encode()).hexdigest()
    elif ID == 11: return hb.blake2b(plainText.encode()).hexdigest()
    elif ID == 12: return hb.blake2s(plainText.encode()).hexdigest()
    elif ID == 13: return hb.sha3_512(plainText.encode()).hexdigest()
    elif ID == 14: return hb.sha512(plainText.encode()).hexdigest()

# Bruteforcing function, to perform dictionary attack.
def bruteforcer(dictionary, digest):
    wordlist = open(dictionary, 'r', errors='ignore')
    for password in wordlist:
        password = password.strip()
        if hash_return(password) == digest:
            print(Fore.GREEN+f"The plaintext {password} corresponds to the hash [{digest}]")
            sys.exit(0)
    print(Fore+'The corresponding plaintext was not found into the wordlist {}'.format(dictionary))


# If the user set the flag `Bruteforcing` it will be equal to True
if arg.Bruteforcing:
    if not os.path.exists(arg.Dictionary):
        print(Fore.RED+f"The dictionary {arg.Dictionary} was not found.")
        sys.exit(404)
    bruteforcer(arg.Dictionary, arg.Hash)
else:
    print(Fore.GREEN+f"{hash_return(arg.PlainText)}")