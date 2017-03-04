
# coding: utf-8

import ast, glob, os, argparse
from itertools import chain

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)

def stress_indicator(f, **kwargs):
    """
    Returns a txt-file with the indices of stressed syllables
    (indices for each line)
    
    Parameters:
    
    f is the txt-file with the stressed/not stressed syllables.
    """
    
    # input file - txt with lists of accentized syllables
    
    file_input = open(f, 'r', encoding = 'utf-8')
    lines = file_input.readlines()
    
    # output file - txt with lists of indices of stressed syllables
    
    name = f.split('.')[0] + '_ind.txt'
    f_out = open(os.path.join(dname, name), 'w')
    
    # read and process input file
    
    ll = list()

    for i in range(0, len(lines)):
        ll.append(ast.literal_eval(lines[i]))

    for l in ll:
        indices = list()
        for s in l:
            if s.isupper():
                indices.append(l.index(s))
        f_out.write(str(indices))
        f_out.write('\n')
    
    f_out.close()
    file_input.close()
    

parser = argparse.ArgumentParser()
parser.set_defaults(method = stress_indicator)
parser.add_argument('f', action = 'store')

args = parser.parse_args()
args.method(**vars(args))
