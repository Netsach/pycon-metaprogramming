.. title:: Metaprogramming for fun and profit with Python 3.6

:css: css/style.css
:skip-help: true


Metaprogramming for fun and profit
==================================


(with Python 3.6)
-----------------


@pa_schembri
++++++++++++

https://netsach.com
+++++++++++++++++++

https://github.com/Netsach/pycon-metaprogramming
++++++++++++++++++++++++++++++++++++++++++++++++





----






Quick intro
===========

- Me: HW/SW Engineer, Founder and CEO of Netsach
- Netsach: Technology Bridging & Automation
- Credits:

    + Guido Van Rossum [for Python]
    + David Beazley [for inspiration]



----






Agenda
======

- Metaprogramming: An introduction
- Decorators
- Descriptors
- Metaclasses
- Let's dive in !





----






Metaprogramming: An introduction
================================





----





Classic Programming
===================

- Manipulate data
- Help your end-user
- Good *UI / CLI* wanted
- I/O operations at some point


----





PEP 20: Zen of Python (extract)
===============================

- Explicit is better than implicit.
- Simple is better than complex.
- If the implementation is hard to explain, it's a bad idea.


----





Metaprogramming
===============

- Code is your data !
- Your end-user **is** a developer
- *PEP-20 ??*
- Good *API* wanted !


----






Decorators
==========





----






Decorators
==========

- A decorator *is* a function
- Takes a function as an input
- Returns another *altered* function
- Adds / removes features




----






Decorators
==========


Let's dive in
-------------


----






Descriptors
===========





----






Descriptors
===========


- A descriptor *is* an object instance of a special class
- The class defines ``__get__``, ``__set__`` and ``__delete__`` methods
- **New in Python 3.6** : ``__set_name__`` (PEP-487)
- Instantiated in *other* classes
- Performs its logic on *other* objects
- Invoked when using ``.`` (dot) operator



----






Descriptors
===========


Let's dive in
-------------




----






Metaclasses
===========





----






Metaclasses
===========


- Classes that makes classes
- Vocabulary is key: *instances of type*...
- Programmatically instantiate classes
- Like decorators but on steroids


----






Metaclasses
===========


- Override the builtin ``type`` class
- Propagates through *class hierarchies*
- Highest customization possible without frame hacking
- **New in Python 3.6** : ``__init_subclass__`` (PEP-487)




----






Metaclasses
===========


Let's dive in
-------------




----






Restrospect
===========





----






Usage in production
===================

- Data structures and utilities
- REST Datastore (**concrete**)
- Javascript generation at runtime
- GUI generation at runtime


----






Maintainability
===============

- Work methods and ethic
- Teach, learn, repeat.
- Pair programming


----






Q & A
=====

.. code:: text

    GET /end-of-talk/

    HTTP/1.1 406 Not Acceptable

    Reason: Questions ?


- https://github.com/Netsach/pycon-metaprogramming
- Netsach : https://netsach.com
- We're hiring ! http://hire.netsach.eu
