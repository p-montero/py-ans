#!/usr/bin/env python
'''
Write a Python program using ciscoconfparse that parses the 'cisco_ipsec.txt'
config file. Note, this config file is not fully valid (i.e. parts of the
configuration are missing).
The script should find all of the crypto map entries in the file (lines that
begin with 'crypto map CRYPTO') and print out the children of each crypto map.
'''

from ciscoconfparse import CiscoConfParse
from pprint import pprint as pp

# cisco_ipsec.txt locally stored under /class1
cisco_cfg_file = 'cisco_ipsec.txt'

#
cisco_cfg = CiscoConfParse(cisco_cfg_file)

# Find all the lines starting with 'crypto map CRYPTO'
crypto_map_lines = cisco_cfg.find_objects(r"^crypto map CRYPTO")

# Let's find them
print ("LINES containing: crypto map CRYPTO :")
for k in crypto_map_lines:
    pp (k.text)
    for c in k.children:
        pp (c.text)
    print ("-:-")
print ("-- END --")
