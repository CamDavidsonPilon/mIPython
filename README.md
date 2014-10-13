#mIPython 

Do some fun analysis on your histortical IPython commands!

## To Run:

1. Edit the `mipython.py` file to use your `IPYTHON_HOME`.
2. From the command line, not the IPython Shell, run the `mipython.py` file. The program will go through the sqlite database that IPython uses to store all your commands and print out some neat summaries and recommendations. 

## Example output:

```
Most common imports:
[(u'lifelines', 378),
 (u'pandas', 163),
 (u'vertdb', 156),
 (u'sklearn', 141),
 (u'scipy', 137),
 (u'matplotlib', 103),
 (u'pymc', 78),
 (u'numpy', 69),
 (u'starscream', 61),
 (u'datetime', 49),
 (u'demographica', 49),
 (u'shopify', 49),
 (u'json', 46),
 (u'IPython', 36),
 (u'patsy', 31),
 (u'redshift', 22),
 (u'string', 16),
 (u're', 16),
 (u'itertools', 15),
 (u'glob', 13)]

Most common assignemnt variables
[(u'df', 671),
 (u'data', 542),
 (u'ax', 434),
 (u's', 269),
 (u'd', 207),
 (u'q', 203),
 (u'ix', 168),
 (u'x', 157),
 (u'N', 157),
 (u'fig', 150),
 (u'kmf', 143),
 (u'colours', 107),
 (u'T', 92),
 (u'aaf', 86),
 (u'X', 84),
 (u'C', 81),
 (u'p', 79),
 (u'mcmc', 79),
 (u't', 76),
 (u'pca', 74)]

We recommend adding the following imports to the startup file '~/.ipython/startup/00-imports.py'
import pandas as pd                        84
import vertdb                              72
from lifelines import KaplanMeierFitter    72
import json                                38
from scipy.stats import beta               36
```
