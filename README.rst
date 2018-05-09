
==================
icindirect
==================

:Version: 0.1.0
:Source: https://github.com/sergei-maertens/icindirect
:Keywords: ``NS, Intercity Direct, Delay, Restitution``

|build-status| |requirements|

``Easily claim restitutions for the Intercity Direct``

Developed by `Regex IT`_.


Introduction
============

The Dutch railways operate the Intercity Direct, which is a train using the
high speed line between Breda and Amsterdam. This train is often plagued by
delays and general unreliabelity.

As a passenger, you pay a supplement between Schiphol Airport and Rotterdam,
making this line quite pricey. As soon as 15 minutes delay occurred, you can
claim a restitution to recover some of the costs.

The official restitution form is very convoluted and makes bulk operations
hard. This project aims to make it possible to remember the (excessive amount
of) data that is required to fill out the form, and handles the multi-step
submission for you, greatly lowering the treshold to make claims.

In the future, connections with OpenOV data will be leveraged to simplify the
process even further.


Privacy
=======

This tool relays a lot of personal information that's required by the official
NS claim forms. This personal information is not stored in the database of
ICIndirect. A feature exists to save your data for convenience, which is
implemented as a browser-local feature. This does mean that your data is not
shared between devices.

I urge everyone to read the source code of this project to verify no funky
business is happening.


Documentation
=============

See ``INSTALL.rst`` for installation instructions, available settings and
commands.


References
==========

* `Issues <https://github.com/sergei-maertens/icindirect/issues>`_
* `Code <https://github.com/sergei-maertens/icindirect/>`_


.. |build-status| image:: http://jenkins.maykin.nl/buildStatus/icon?job=icindirect
    :alt: Build status
    :target: http://jenkins.maykin.nl/job/icindirect

.. |requirements| image:: https://requires.io/github/sergei-maertens/icindirect/requirements.svg?branch=develop
     :target: https://requires.io/github/sergei-maertens/icindirect/requirements/?branch=develop
     :alt: Requirements status


.. _Regex IT: https://regex-it.nl
