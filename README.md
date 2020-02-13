# Welcome to utilspy documentation!
[![Documentation Status](https://readthedocs.org/projects/utilpy/badge/?version=latest)](https://utilpy.readthedocs.io/en/latest/?badge=latest)

Collection of python utils.

For detail [Here is Documentation](https://utilpy.readthedocs.io/en/latest/index.html)

# Install 
```bash
pip3 install utilpy
```

____

## utilspy package

```python

import time

from utilpy import log, files, decorator

# logger function 
logs = log.Logger()

logs.log("< started >")
time.sleep(2)
logs.log("running..")
time.sleep(1)
logs.log("</>")


# timeout
@decorator.timeout(5)
def add(x, y):
    return x+y

# other useful utils
files = utils.walk_directory('.')

```

#### other useful code
1. retry
```
# return 
from retrying import retry
@retry(wait_random_min=1000, wait_random_max=2000, stop_max_attempt_number=3)
def sum(x, y):
    return x/y
```

2. Memory
```
%load_ext memory_profiler
%mprun -f extract_all_pages x=extract_all_pages()
```
____