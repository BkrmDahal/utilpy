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

____