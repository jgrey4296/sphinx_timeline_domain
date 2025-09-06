.. ..  index.rst -*- mode: ReST -*-

.. _index:

==========================
Sphinx Timeline Domain
==========================

.. contents:: Table of Contents


------------
Introduction
------------

A Sphinx Domain for Timeline files.


----------------------
The Timeline Directive
----------------------

::
   .. timeline::
   
      1925 "An Event" 
      1925.CE -> 1930.CE "A Period" :timeline:tags:"blah,bloo"
      1950 "An Event" location :ref:`person`
   

Results in:


.. timeline::
   
      1925 "An Event" 
      1925.CE -> 1930.CE "A Period" :timeline:tags:"blah,bloo"
      1950 "An Event" location :ref:`person`


------------
Installation
------------

To install, run ``uv add sphinx_timeline_domain` and sync
Then, in your ``conf.py``:

.. code:: python
 
   extensions =  ["sphinx_timeline_domain"]
          
   # To enable .timeline file parsing:
   source_suffix = {".timeline": "timeline"}



.. _repo:

---------------
Repo And Issues
---------------

The repo can be found `here <https://github.com/jgrey4296/sphinx_timeline_domain>`_.

If you find a bug, bug me, unsurprisingly, on the `issue tracker <https://github.com/jgrey4296/sphinx_timeline_domain/issues>`_.


.. .. Main Sidebar TocTree
.. toctree::
   :maxdepth: 3
   :glob:
   :hidden:
      
   [a-z]*/index

   _docs/*
   genindex
   modindex
   API Reference <_docs/_autoapi/sphinx_timeline_domain/index>
   

.. .. Links

.. _extension: https://www.sphinx-doc.org/en/master/development/index.html

.. _directive: https://www.sphinx-doc.org/en/master/glossary.html#term-directive

.. _roles: https://www.sphinx-doc.org/en/master/glossary.html#term-role
