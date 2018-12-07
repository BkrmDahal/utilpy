.. email documentation master file, created by
   sphinx-quickstart on Thu Aug  9 13:47:11 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to utils's documentation!
=================================

Collection of python utils.

Install
========
   pip install git+https://github.com/BkrmDahal/utilspy.git

Utilspy Examples
=================

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

Examples:
=========

.. toctree::
   :maxdepth: 2

   examples


Utilpy Packages:
=================

.. toctree::
   :maxdepth: 2

   utilpy


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
