# $\sqrt \pi$ PyRoot

## Overview
this module will add your project root to the python path
this is mainly usefull when working with several repositories, where setting a global `PYTHONPATH` is less suitable

the modeule looks for a "marker" - a file that marks the project root
it can also be a relative path 

for example:
* `.git` will refer to the git root
* `../.git` will refer to one folder below the git root

different methods are provided for scripts and notebooks 

(as in notebooks the current file isn't avaiable, so the module relies on the working directory)

## Installation

`pip install git+https://github.com/ophiry/pyroot.git`


## Usage

```
from pyroot import notebook, script

notebook('.git')

script('../.git')
```

## Author
Ophir Yoktan
