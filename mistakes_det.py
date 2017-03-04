
# coding: utf-8

import ast, argparse
from itertools import chain

def mistakes(f1, f2, **kwargs):
    """
    Returns the html-file with syllables marked:
    black -- correctly stressed/not stressed
    red -- incorrectly stressed
    blue -- incorrectly not stressed.
    
    Parameters:
    f1 -- txt-file with syllables stressed athomatically
    f2 -- txt-file with syllables stressed in ethalon 
    """

    text1 = open(f1, 'r', encoding = 'utf-8') # automated
    lines1 = text1.readlines()

    text2 = open(f2, 'r', encoding = 'utf-8') # ethalon
    lines2 = text2.readlines()

    ll1, ll2 = list(), list()

    for i in range(0,len(lines1)):
        ll1.append(ast.literal_eval(lines1[i]))
        ll2.append(ast.literal_eval(lines2[i]))  
        
    total1 = list(chain.from_iterable(ll1))
    total2 = list(chain.from_iterable(ll2))    

    fname = f1.split('.')[0].split('_')[0]

    #print(ll1)
    style = """<style type='text/css'>
    html {
      font-family: Courier;
    }
    r {
      color: #ff0000;
    }
    b {
      color: #0000ff;
    }
    bl {
      color: #000000;
    }
    </style>"""

    
    RED = 'r'
    BLACK = 'bl'
    BLUE = 'b'
    
    def write_html(f, type, str_):
        f.write('<%(type)s>%(str)s</%(type)s>' % {
                'type': type, 'str': str_ } )
    
    f = open(fname + '_with_mistakes.html', 'w')
    f.write('<html>')
    f.write(style)
    
    
    def compare(s1, s2):
        if s1.isupper() and s2.islower():
            write_html(f, RED, s1 + ' ')
        if s1.islower() and s2.isupper():
            write_html(f, BLUE, s1 + ' ')
        if (s1.isupper() and s2.isupper()) or (s1.islower() and s2.islower()):
            write_html(f, BLACK, s1 + ' ')    
    
    for i in range(0, len(total1)):
        
        compare(total1[i], total2[i])
    f.write('</html>')
    
parser = argparse.ArgumentParser()
parser.set_defaults(method = mistakes)
parser.add_argument('f1', action = 'store')
parser.add_argument('f2', action = 'store')

args = parser.parse_args()
args.method(**vars(args))

