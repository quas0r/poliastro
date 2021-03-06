.. poliastro

.. image:: http://poliastro.github.io/images/logo_text.png
   :target: http://poliastro.github.io/
   :alt: poliastro logo
   :width: 675px
   :align: center

.. |orcid| image:: https://img.shields.io/badge/id-0000--0002--2187--161X-a6ce39.svg
   :target: http://orcid.org/0000-0002-2187-161X

:Name: poliastro
:Website: https://poliastro.github.io/
:Author: Juan Luis Cano Rodríguez |orcid|
:Version: 0.7.dev0

.. |travisci| image:: https://img.shields.io/travis/poliastro/poliastro/master.svg?style=flat-square
   :target: https://travis-ci.org/poliastro/poliastro

.. |appveyor| image:: https://img.shields.io/appveyor/ci/Juanlu001/poliastro/master.svg?style=flat-square
   :target: https://ci.appveyor.com/project/Juanlu001/poliastro/branch/master

.. |codecov| image:: https://img.shields.io/codecov/c/github/poliastro/poliastro.svg?style=flat-square
   :target: https://codecov.io/github/poliastro/poliastro?branch=master

.. |codeclimate| image:: https://img.shields.io/codeclimate/github/poliastro/poliastro.svg?style=flat-square
   :target: https://lima.codeclimate.com/github/poliastro/poliastro

.. |docs| image:: https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat-square
   :target: http://poliastro.readthedocs.io/en/latest/?badge=latest

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
   :target: https://github.com/poliastro/poliastro/raw/master/COPYING

.. |doi| image:: https://zenodo.org/badge/12813/poliastro/poliastro.svg?style=flat-square
   :target: https://zenodo.org/badge/latestdoi/12813/poliastro/poliastro

.. |astropy| image:: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat-square
   :target: http://www.astropy.org/

.. |mailing| image:: https://img.shields.io/badge/mailing%20list-groups.io-8cbcd1.svg?style=flat-square
   :target: https://groups.io/g/poliastro-dev

|travisci| |appveyor| |codecov| |codeclimate|

|docs| |license| |doi| |astropy| |mailing|

poliastro is an open source pure Python package dedicated to problems arising in Astrodynamics and
Orbital Mechanics, such as orbit propagation, solution of the Lambert's
problem, conversion between position and velocity vectors and classical
orbital elements and orbit plotting, focusing on interplanetary applications.
It is released under the MIT license.

.. code-block:: python

    from poliastro.examples import molniya
    from poliastro.plotting import plot
    
    plot(molniya)

.. image:: https://github.com/poliastro/poliastro/raw/master/examples/molniya.png
   :align: center

Documentation
=============

|docs|

Complete documentation, including a user guide and an API reference, can be read on
the wonderful `Read the Docs`_.

http://poliastro.readthedocs.io/en/latest/

.. _`Read the Docs`: http://readthedocs.io/

Examples
========

.. |mybinder| image:: https://img.shields.io/badge/launch-binder-e66581.svg?style=flat-square
   :target: http://mybinder.org/repo/poliastro/poliastro

|mybinder|

In the examples directory you can find several Jupyter notebooks with specific
applications of poliastro. You can launch a cloud Jupyter server using `binder`_ to edit
the notebooks without installing anything. Try it out!

http://mybinder.org/repo/poliastro/poliastro

.. _binder: http://mybinder.org/

Requirements
============

poliastro requires the following Python packages:

* NumPy, for basic numerical routines
* Astropy, for physical units and time handling
* numba (optional), for accelerating the code
* jplephem, for the planetary ephemerides using SPICE kernels
* matplotlib, for orbit plotting
* SciPy, for root finding and numerical propagation

poliastro is usually tested on Linux, Windows and OS X on Python
3.5 and 3.6 against latest NumPy.

==============  ============  ===================
Platform        Site          Status
==============  ============  ===================
Linux & OS X    Travis CI     |travisci|
Windows x64     Appveyor      |appveyor|
==============  ============  ===================

Installation
============

The easiest and fastest way to get the package up and running is to
install poliastro using `conda <http://conda.io>`_::

  $ conda install poliastro --channel conda-forge

You can also `install poliastro from PyPI`_ using pip, given that you already
have all the requirements::

  $ pip install poliastro

You can also `download poliastro source from GitHub`_ and type::

  $ pip install .

Development installations are also supported::

  $ pip install -e .

.. _`install poliastro from PyPI`: https://pypi.python.org/pypi/poliastro/
.. _`download poliastro source from GitHub`: http://github.com/poliastro/poliastro

.. warning::

    It is recommended that you **never ever use sudo** with distutils, pip,
    setuptools and friends in Linux because you might seriously break your
    system [1_][2_][3_][4_]. Options are `per user directories`_, `virtualenv`_
    or `local installations`_.

.. _1: http://wiki.python.org/moin/CheeseShopTutorial#Distutils_Installation
.. _2: http://stackoverflow.com/questions/4314376/how-can-i-install-a-python-egg-file/4314446#comment4690673_4314446
.. _3: http://workaround.org/easy-install-debian
.. _4: http://matplotlib.1069221.n5.nabble.com/Why-is-pip-not-mentioned-in-the-Installation-Documentation-tp39779p39812.html

.. _`per user directories`: http://stackoverflow.com/a/7143496/554319
.. _`virtualenv`: http://pypi.python.org/pypi/virtualenv
.. _`local installations`: http://stackoverflow.com/a/4325047/554319

Testing
=======

|codecov|

If installed correctly, the tests can be run using pytest::

  $ python -c "import poliastro.testing; poliastro.testing.test()"
  Running unit tests for poliastro
  [...]
  OK
  $ 

Contributing
============

.. image:: https://img.shields.io/waffle/label/poliastro/poliastro/1%20-%20Ready.svg?style=flat-square
   :target: https://waffle.io/poliastro/poliastro
   :alt: 'Stories in Ready'

poliastro is a community project, hence all contributions are more than
welcome! For more information, head to `CONTRIBUTING.rst`_.

.. _`CONTRIBUTING.rst`: https://github.com/poliastro/poliastro/blob/master/CONTRIBUTING.rst

Support
=======

|mailing|

Release announcements and general discussion take place on our `mailing list`_.
Feel free to join!

.. _`mailing list`: https://groups.io/g/poliastro-dev

https://groups.io/g/poliastro-dev

Citing
======

If you use poliastro on your project, please
`drop me a line <mailto:juanlu001@gmail.com>`_.

You can also use the DOI to cite it in your publications. This is the latest
one:

|doi|

And this is an example citation format::

 Juan Luis Cano Rodríguez et al.. (2015). poliastro: poliastro 0.4.0. Zenodo. 10.5281/zenodo.17462

License
=======

|license|

poliastro is released under the MIT license, hence allowing commercial
use of the library. Please refer to the COPYING file.

FAQ
===

What's up with the name?
------------------------

poliastro comes from Polimi, which is the shortened name of the Politecnico di
Milano, the Italian university where I was studying while writing this
software. It's my tiny tribute to a place I came to love. *Grazie mille!*

Can I do <insert awesome thing> with poliastro?
-----------------------------------------------

poliastro is focused on interplanetary applications. This has two consequences:

* It tries to be more general than other Flight Dynamics core libraries more
  focused on Earth satellites (see `Related software`_ for a brief list),
  allowing the algorithms to work also for orbits around non-Earth bodies.
* It leaves out certain features that would be too Earth-specific, such as
  TLE reading, SGP4 propagation, groundtrack plotting and others.

Keep that in mind when asking for a feature. For a software package focused on
Earth applications please refer to the `Python Astrodynamics Project`_, a
still in progress joint effort between several developers.

.. _`Related software`: http://poliastro.readthedocs.io/en/latest/about.html#related-software
.. _`Python Astrodynamics Project`: https://github.com/python-astrodynamics/astrodynamics

What's the future of the project?
---------------------------------

poliastro is actively maintained and will receive bug fixes and releases
in 2017, maintaining its focus on interplanetary applications. Expect better
algorithms, easier 3D plotting and optimization techniques. The best way
to get an idea of the roadmap is to check the Kanban board at Waffle.io
(see `Contributing`_).
