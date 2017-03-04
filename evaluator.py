
# coding: utf-8

import ast, glob, argparse
from itertools import chain

#f1  automated
#f2  ethalon

def evaluation(f1, f2, **kwargs):
    """
    Returns three measures of quality of the accentizer:
    precision, recall, F-measure.
    
    Parameters:
    f1 - a txt-file with indices of stressed syllables (defined by authomatic accentizer)
    f2 - a txt-file with indices of stressed syllables (derived from the ethalon)
    """
    
    text1 = open(f1, 'r', encoding = 'utf-8')
    lines1 = text1.readlines()

    text2 = open(f2, 'r', encoding = 'utf-8')
    lines2 = text2.readlines()

    ll1, ll2 = list(), list()

    for i in range(0,len(lines1)):
        ll1.append(ast.literal_eval(lines1[i]))
        ll2.append(ast.literal_eval(lines2[i]))  
        
    total_syl = len(list(chain.from_iterable(ll1)))

    tp = sum([len(set(ll2[i]) & set(ll1[i])) for i in range(0, len(ll1))]) # correclty stressed by programm
    fp = sum([len(set(ll1[i]) - set(ll2[i])) for i in range(0, len(ll1))]) # incorrectly stressed by programm
    fn = sum([len(set(ll2[i]) - set(ll1[i])) for i in range(0, len(ll1))]) # incorrectly not stressed by programm

    precision = tp/(tp + fp) * 100
    recall = tp/(tp + fn) * 100
    f_score = 2 * precision * recall / (precision + recall)
    
    print('total number of syllables: ', total_syl)
    print('precision: ', precision)
    print('recall: ', recall)
    print('F-score: ', f_score)
    return

parser = argparse.ArgumentParser()
parser.set_defaults(method = evaluation)
parser.add_argument('f1', action = 'store')
parser.add_argument('f2', action = 'store')

args = parser.parse_args()
args.method(**vars(args))


