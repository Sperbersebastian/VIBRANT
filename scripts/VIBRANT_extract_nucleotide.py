#! /usr/bin/env python3
# Author: Kristopher Kieft, UW-Madison

# VIBRANT v1.2.1
# Virus Identification By iteRative ANnoTation
# Release date: March 13 2020

# Usage: see VIBRANT_run.py

import sys
import os

# Add the VIBRANT base directory to sys.path
VIBRANT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if VIBRANT_DIR not in sys.path:
    sys.path.append(VIBRANT_DIR)
from scripts.fasta_utils import SimpleFastaParser
import subprocess

db_dict = {}
total = 0
with open(str(sys.argv[1]), 'r') as accnos:
    with open(str(sys.argv[2]), 'w') as fasta:
        with open(str(sys.argv[3]), 'r') as db:
            accnos_list = accnos.read().split("\n")
            if accnos_list[-1] == '':
                accnos_list = accnos_list[:-1]
            for name, seq in SimpleFastaParser(db):
                db_dict.update({name:seq})
            for item in accnos_list:
                if len(list(db_dict[item.strip(">")])) >= int(sys.argv[4]):
                    total += 1
                    fasta.write(">" + str(item).replace(" ", "$~&").replace('"','^@%') + "\n" + db_dict[item.strip(">")] + "\n")

if total == 0:
    subprocess.run('rm ' + str(sys.argv[1]), shell=True)
    subprocess.run('rm ' + str(sys.argv[2]), shell=True)
