Utilpy Examples
================

Install
--------
   pip install git+https://github.com/BkrmDahal/utilspy.git

Examples
---------

.. code-block:: python

    import time

    from utilpy import log, files, decorator

    # logger funcation 
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