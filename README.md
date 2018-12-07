# Welcome to utilspy documentation!
[![Documentation Status](https://readthedocs.org/projects/utilspy/badge/?version=latest)](https://utilspy.readthedocs.io/en/latest/?badge=latest)

Collection of python utils.

For detail [Here is Documentation](https://utilspy.readthedocs.io/en/latest/index.html)

# Install 
```bash
pip install git+https://github.com/BkrmDahal/utilspy.git
```

____

## utilspy package

```python

import time

from utilspy import log, files, decorator

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