Plant database
======================================

.. documentation master file.

Nature-Based Solutions (NBS) for river engineering experience incresing popularity to leverage flood risk and ecosystem management in the light of climate change. Even though the demand for NBS is high, there design regarding scale and placement still is an important challenge. In some cases, missing knowledge and trust in NBS lead to overestimations of costs and time. This plant database constitutes an important step in the design of NBS with a plant data base for river engineering. 


.. This documentation is also as available as style-adapted PDF (`download <https://.readthedocs.io/plantDB/downloads/en/latest/pdf/>`_).

Installation
============

Use ``git`` to download the ``plantDB`` repository (make sure to
`install Git Bash`_):

1. Open *Git Bash* (or any other git-able *Terminal*)
2. Create or select a target directory for ``plantDB`` (e.g., in your
   *Python* project folder)
3. Type ``cd "D:/Target/Directory/"`` to change to the target
   installation directory.
4. Clone the repository.

.. code:: console

   $ cd "D:/Target/Directory/"
   $ git clone https://github.com/Lukas-create/plantDB.git

Now, ``plantDB`` lives in ``"D:/Target/Directory/plantDB/plantDB"``.

Usage
=====

Import
~~~~~~~

1. Run *Python* and add the download directory of ``plantDB`` to the
   system path:

.. code:: python

   import os, sys
   sys.path.append("D:/Target/Directory/plantDB/")  # Of course: replace "D:/Target/Directory/", e.g., with  r'' + os.path.abspath('')

2. Import ``plantDB``:

.. code:: python

   import plantDB as 

Example
~~~~~~~
The following will show how the tool can be used to search for suitable vegetation
To choose between the three provided ways to search for vegetation, start by calling the ``question()`` function.


.. code:: python

   import plantDB as re

   re.search.question()


This results in an console output informing the user about the possible choices and asking for an decision.


::

   Enter 1 to search database by habitat with detailed information
   Enter 2 to search database by coordinates
   Enter 3 to search by habitat in csv file for a quick overview without detail
   habitat search options so far:
   Alpenvorland, Niederrheinisches Tiefland, Oberrheinisches Tiefland
   Enter here:


If you want to search for plant data in the database directly, call search_db_via_query() and provide an corresponding sql - query.


.. code:: python

   import plantDB as re

   query = "habitat = 'Alpenvorland'"
   re.search.search_db_via_query(query)


.. note:: If you start by calling question(),  you get asked for a query in the console and don't need to manually add it.


The above function call will print all plants including their parameters which are located in 'Alpenvorland'. ``plantDB`` supports arbitrary sql-querys over the datafields in the provided 'Pflanzendaten.db' database.
To search directly for vegetation via coordinate input without starting with question() first, simply call search_by_coordinates().


.. code:: python

   import plantDB as re

   re.search.search_by_coordinates()


By doing so, you will get asked to provide x and y coordinates in the console


::

    CRS used is EPSG:3857
    for reference check https://epsg.io/3857
    Enter x coordinate
    1267965.259120
    Enter y coordinate
    6090686.743663


The possibility to receive additional elevation data for the above entered coordinates is then offered through the then called function point_in_bound()  via the console.


::

    Enter 1 if you want elevation data for the coordinates
    Enter 2 if you dont want elevation data
    Enter here:


The last available search option is to search for vegetation in the csv file. To achieve this, call search_by_habitat().


.. code:: python

   import plantDB as re

   re.search.search_by_habitat()


You will get asked to provide a habitat name you want to search plants for, afterwards all plants where your input matches witch their habitat entry in the csv file will get printed.


::

    Enter name of habitat
    Alpenvorland

    scientific name:
    Alnus incana
    common german name:
    Grauerle
    status:
    1
    endangered?:
    not endangered


The example above is one plant that gets printed if you should choose to search for plants in the habitat 'Alpenvorland'.


Requirements
============

*  Python 3.x (read more on `hydro-informatics.github.io`_)
*  Dependencies:

   * numpy
   * gdal (read more on `hydro-informatics.github.io/geo-pckg <https://hydro-informatics.github.io/geo-pckg.html#gdal>`_)
   * geopandas
   * alphashape
   * shapely
   * tabulate
   * platform
   * os
   * sqlite3



Database
==================

The database ``Pflanzendaten`` used in this tool is an relational database which was created using SQL. The database consists of one table called ``plants`` which includes all the gathered plant data of the following types:

::

    species (str): scientific plant name
    name (str): common german plant name
    nativ (bool): equals 1 if the plant is nativ, 0 if its not
    habitat (str): habit name of the plant
    endangered (str): information about the endangerment status of the plant
    waterdepthmin (int): minimal required water depth [cm]
    waterdepthmax (int): maximum depth to groundwater [cm]
    rootdepth (int): average root depth [cm]
    groundwatertablechange (varchar): maximum change in groundwater table that the plant can survive [cm]
    floodheightmax (int): maximum flood height the plant can survive [cm]
    floodloss (float): losses during maximum flood height and flooding days that occured in plant population [%]
    flooddurationmax (int): maximum number of flooding days the plant can survive [d]

They are matching the arguments from the created class ``Plant``.
The entries species, name and habitat are defined as primary keys, preventing the insertion of possible duplicates.

Code Documentation
==================

Package structure
~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://https://github.com/Lukas-create/plantDB/raw/master/docs/img/w2p_structure.png
   :alt: structure



Scripts and functions
=====================


``plantDB`` 
~~~~~~~~~~~~~~~~~~~~~
.. automodule:: plant
   :members:

Search for vegetation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: search
   :members:

SQL mgmt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: sqlinput
   :members:


Contributing
=======================

How to document
~~~~~~~~~~~~~~~~

This package uses *Sphinx* `readthedocs <https://readthedocs.org/>`_ and the documentation regenerates automatically after pushing changes to the repositories ``main`` branch.

To set styles, configure or add extensions to the documentation use ``ROOT/.readthedocs.yml`` and ``ROOT/docs/conf.py``.

Functions and classes are automatically parsed for `docstrings <https://www.python.org/dev/peps/pep-0257/>`_ and implemented in the documentation. ``hylas`` docs use `google style <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_ docstring formats - please familiarize with the style format and strictly apply in all commits.

To modify this documentation file, edit ``ROOT/docs/index.rst`` (uses `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ format).

In the class or function docstrings use the following section headers:

For local builds of the documentation, the following packages are required:

.. code:: console

   $ sudo apt-get install build-essential
   $ sudo apt-get install python-dev python-pip python-setuptools
   $ sudo apt-get install libxml2-dev libxslt1-dev zlib1g-dev
   $ apt-cache search libffi
   $ sudo apt-get install -y libffi-dev
   $ sudo apt-get install python3-dev default-libmysqlclient-dev
   $ sudo apt-get install python3-dev
   $ sudo apt-get install redis-server

To generate a local html version of the ``hylas`` documentation, ``cd`` into the  ``docs`` directory  and type:

.. code:: console

   make html

Learn more about *Sphinx* documentation and the automatic generation of *Python* code docs through docstrings in the tutorial provided at `github.com/sschwindt/docs-with-sphinx <https://github.com/sschwindt/docs-with-sphinx>`_


