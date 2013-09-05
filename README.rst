The python test assertion module
================================

Inspired by should.js and rspec

Install
=======

.. code:: bash

    pip install the

Usage
=====

.. code:: python

    from the import The

API
===

matcher methods
---------------

test ``==``
~~~~~~~~~~~

.. code:: python

    The(1).should.be.equal(1)

test ``isinstance``
~~~~~~~~~~~~~~~~~~~

.. code:: python

    The(1).should.be.an(int)
    The((1,2,3)).should.be.a(tuple)

test ``is``
~~~~~~~~~~~

.. code:: python

    The(None).Is(None)
    The([1,2,3]).is_not([1,2,3])

test ``>``
~~~~~~~~~~

.. code:: python

    The(1).should.be.above(0)

test ``<``
~~~~~~~~~~

.. code:: python

    The(0).should.be.below(1)

test match string
~~~~~~~~~~~~~~~~~

.. code:: python

    The('a small module for testing').should.match('module')

test ``len``
~~~~~~~~~~~~

.. code:: python

    The([1,2,3]).should.have.length(3)
    The([1,2,3]).should.have.size(3)

test ``in``
~~~~~~~~~~~

.. code:: python

    The(1).should.In([1,2,3])
    The(1).should.within([1,2,3])

test item ``in`` dict
~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    The({"a": 1, "b": 2}).should.have.item("a", 1)

test items ``in`` dict
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    The({"a": 1, "b": 2}).should.have.items(a=1, b=2)

test key ``in`` dict
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    The({"a": 1, "b": 2}).should.have.key("a")

test keys ``in`` dict
~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    The({"a": 1, "b": 2}).should.have.keys("a", "b")

test value ``in`` dict
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    The({"a": 1, "b": 2}).should.have.value(1)

test values ``in`` dict
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    The({"a": 1, "b": 2}).should.have.values(1, 2)

test object property
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    class A(object):
        def __init__(self):
            self.message = 'hello world'

    The(A()).should.have.property('message')
    The(A()).should.have.property('message', 'hello world')
    The(A()).should.have.attr('message')
    The(A()).should.have.attribute('message')

test object method
~~~~~~~~~~~~~~~~~~

.. code:: python

    The("hello").should.have.method("strip")
    The("hello").should.respond_to("strip")

test include
~~~~~~~~~~~~

.. code:: python

    The([1,2,3]).should.include(1)
    The([1,2,3]).should.includes(1)
    The([1,2,3]).should.contain(1)
    The([1,2,3]).should.contains(1)

test function
~~~~~~~~~~~~~

.. code:: python

    def fib(x):
        memo = {}
        def _fib():
            if x in (0, 1): return 1
            if x not in memo: memo[x] = fib(x-2) + fib(x-1)
            return memo[x]
        return _fib()

    The(fib).when.apply(1).should.Return(1)

    The(fib).when.apply(1,2,3,4).should.throw()

matcher property
----------------

These property will trigger the corresponding protected matcher methods,
which are not being called explicitly.

All the keywords
``python coders = {'nt', 'true', 'false', 'none', 'exist',            'ok', 'empty', 'Not', 'yes', 'exists',            'truthy', 'falsy', 'no'}``

test ``not``
~~~~~~~~~~~~

.. code:: python

    The(1).should.Not.be.a(str)
    The([1,2,3]).should.nt.be.a(str)

test ``true``
~~~~~~~~~~~~~

.. code:: python

    The(True).should.be.true

test ``false``
~~~~~~~~~~~~~~

.. code:: python

    The(False).should.be.false

test ``none``
~~~~~~~~~~~~~

.. code:: python

    The(None).should.be.none

test ``not none``\ (exist)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    The(1).should.exist
    The(1).exists
    The(1).should.Not.be.none

test ``falsy``\ ('', [], (), {}, False, None, 0)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    The([]).should.be.falsy
    The('').should.be.empty
    The([]).should.be.empty
    The([]).should.be.no

test ``truthy``
~~~~~~~~~~~~~~~

.. code:: python

    The(1).should.be.truthy
    The(1).should.be.ok
    The(1).should.be.yes
    The(1).should.Not.be.empty

Other buzzwords
---------------

.. code:: python

    them = {'should', 'to', 'have', 'has', 'must',
            'be', 'And', 'when', 'but', 'it'}

These words does nothing but return the object it self.

So, instead of writing ``The(1).Not.a(str)``, you write
``The(1).should.Not.be.a(str).but.be.a(int)``.

Sometimes they make your assertions more readable.

Feel free to add your words if you like.
``python The.them.add("whatever")``
