#!/usr/bin/env python
'''
Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name).
Print these entries and their corresponding transform set name.
'''

from ciscoconfparse import CiscoConfParse
# from pprint import pprint as pp
# Using termcolor for some terminal colors - Not required but learning.
from termcolor import colored

# cisco_ipsec.txt locally stored under /class1
cisco_cfg_file = 'cisco_ipsec.txt'

#
cisco_cfg = CiscoConfParse(cisco_cfg_file)

# Find all the lines starting with 'crypto map CRYPTO'
crypto_map_lines = cisco_cfg.find_objects_wo_child(parentspec=r'crypto map CRYPTO', childspec=r'AES')

# Let's find them
print ("LINES containing: crypto map CRYPTO & no using AES as the transform-set")
print ("-:-")
for k in crypto_map_lines:
    print colored(k.text, 'green')
    for c in k.children:
        if 'transform-set' in c.text:
            print colored(c.text, 'blue')
            print ("-:-")
print ("END")
