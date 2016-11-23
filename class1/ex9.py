#!/usr/bin/env python
'''
Find all of the crypto map entries that are using PFS group2
'''

from ciscoconfparse import CiscoConfParse
# from pprint import pprint as pp

# cisco_ipsec.txt locally stored under /class1
cisco_cfg_file = 'cisco_ipsec.txt'

#
cisco_cfg = CiscoConfParse(cisco_cfg_file)

# Find all the lines starting with 'crypto map CRYPTO'
crypto_map_lines = cisco_cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO', childspec=r'pfs group2')

# Let's find them
print ("LINES containing: crypto map CRYPTO & using PFS Group2 >")
print ("-:-")
for k in crypto_map_lines:
    print k.text
#    print "  {0}".format(k.text)
    print ("-:-")
print ("END")
