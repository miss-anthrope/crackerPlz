#!/usr/bin/env python
# coding: utf-8
'''
Project 8 03/2022
@Witch_Sec
https://github.com/miss-anthrope
-
MD5 Hash Generator: https://www.md5hashgenerator.com/ (Credit to Dan'sTools)
Dictionary for our wordlist: http://weakpasswords.net/ (Credit to TrustedSec)
Class: https://www.udemy.com/course/python-for-pentesters (Credit to Cristi Zot https://www.udemy.com/user/cristivlad2/)
'''
print("MD5 Hash cracker project")
print("\n Mmm... hash.")
print("\n What do they call a Big Oof in France?")
print("\n Le Grande Ouef.")

import hashlib
import argparse

parser=argparse.ArgumentParser(description="MD5 cracker project")
parser.add_argument("-md5",dest="hash",help="md5 hash",required=True)
parser.add_argument("-w",dest="wordlist",help="wordlist",required=True)
parsed_args=parser.parse_args()

def main(): 
	hash_cracked=""
	with open(parsed_args.wordlist) as file:
		for line in file:
			line=line.strip()
			if hashlib.md5(bytes(line,encoding="utf-8")).hexdigest()==parsed_args.hash:
				hash_cracked=line
				print("\nMD5-hash has been successfully cracked. You must have a very big dict! \nThe value of the hash is %s."%line)
				print("\nNice.")
	if hash_cracked=="":
		print("\nYour dict is too small. Sad. Plz ask your big brother to come try for you.")



if __name__ =="__main__":
	main()