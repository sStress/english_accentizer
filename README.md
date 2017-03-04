## english_accentizer

en_accent.py is the modified version of the accentizer based on the one from Scandroid. It handles the following cases:

* confusions in stresses caused by differences between nouns and verbs (cases like INcrease vs inCREASE)
* confusions in stresses caused by insuffient rules in Scandroid (words containing EVER) 
* confusions in stresses caused by insuffient rules in Scandroid (two-syllable nouns starting with EN)

txt-files with texts should be placed in the same folder with en_accent.py. The function creates a folder ended with \_data.  Such a folder contains 3 files: a file with accentized syllables, a file with binary vectors for each line (1 -- stressed, 0 -- not stressed), and a file with indices of stressed syllables.

**Note:** this function requires the library *nltk*.

## stress_indices.py

stress_indices.py is the function that returns the indices of stressed syllables from the ethalon txt-file.

*Example of the command in console:*

python3 stress_indices.py ethalon.

## evaluator.py

evaluator.py is the function that evaluates the quality of English accentizer (calculates the presicion, the recall, and the F-measure). It requires two files at the input: a txt-file with indices of stressed syllables (defined by accentizer) and a txt-file with indices of stressed syllables from ethalon.

*Example of the command in console:*

python3 evaluator.py indices_program.txt indices_ethalon.txt

## mistakes_det.py

mistakes_det.py is the function that creates an html-file with mistakes made by the accentizer. The html-file involves all syllables from the text; correctly stressed/not stressed syllables are written in black, incorrectly stressed syllables are in red, and incorrectly not stressed syllables are in blue. 

The function requires two files: a txt-file with the stressed/not stressed syllables got by the accentizer, and a txt-file with the same syllables stressed by humans (ethalon).

*Example of the command in console*

python3 mistakes_det.py syll_program.txt syll_ethalon.txt

**Note:** example of the output html-file is 1984_with_mistakes.html in this directory.
