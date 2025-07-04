#! /usr/bin/env python3
# Author: Kristopher Kieft, UW-Madison

# VIBRANT
# Virus Identification By iteRative ANnoTation

# Usage: python3 simplify_faa-ffn.py <input.faa>

import sys
import os

# Add the VIBRANT base directory to sys.path
VIBRANT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if VIBRANT_DIR not in sys.path:
    sys.path.append(VIBRANT_DIR)
from scripts.fasta_utils import SimpleFastaParser as SFP

infile = sys.argv[1] # input fasta file

with open(infile, 'r') as fasta: # read in input vibrant (protein) file
    with open(str(infile).rsplit(".",1)[0]+'.simple.'+str(infile).rsplit(".",1)[1], 'w') as appended: # name of output file
        for name, seq in SFP(fasta): # Use SFP to grab name and sequence for the fasta file
            split = name.split('\t(',1)[0] # split by tab and parentheses because that should be specific to vibrant output
            appended.write('>' + split + '\n' + seq + '\n') # write out the split name and sequence
