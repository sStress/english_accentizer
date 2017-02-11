# english_accentizer

en_accent.py is the modified version of the accentizer based on the one from Scandroid. It handles the following cases:

* confusions in stresses caused by differences between nouns and verbs (cases like INcrease vs inCREASE)
* confusions in stresses caused by insuffient rules in Scandroid (words containing EVER) 
* confusions in stresses caused by insuffient rules in Scandroid (two-syllable nouns starting with EN)

txt-files with texts should be placed in the same folder with en_accent.py. The function creates a folder ended with \_data.  Such a folder contains 3 files: a file with accentized syllables, a file with binary vectors for each line (1 -- stressed, 0 -- not stressed), and a file with indices of stressed syllables.

**Attention:** this function requires the library *nltk*.
