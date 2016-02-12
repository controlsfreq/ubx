.. _sdd:

###########################
Software Design Description
###########################

:authors:
  Liam Bucci
:date:
  2016-02-04
:copyright:
  See LICENSE for copyright and licensing information.

1 Introduction
==============

1.1 Purpose
-----------

This document is intended to layout the Eärendil library design as well as the background, context,
and rationale for that design. The intended audience is developers and technical users wishing to
either utilize the Eärendil library for their own projects or to enhance and expand the library
itself.

1.2 Definitions
---------------

Also, see definitions in the :ref:`srs`.

1.3 Overview
------------

The Eärendil library is composed of a series of Python packages and modules. The packages each
contain a closely related set of modules, for instance all NMEA specific code. The code in these
packages may be used to either generate and serialize GNSS related data objects for transmission to
a receiver or to deserialize and manipulate GNSS data captured from a receiver.

The Eärendil library also contains several packages of utility code that may be helpful in the
manipulation of GNSS data.

1.4 References
--------------

1. My favorite reference: http://example.com
2. My second favorite reference: http://en.wikipedia.com

Also, see references in the :ref:`srs`.

2 System Overview
=================

The Eärendil library is composed of four packages:

* Core  - Core functionality used commonly throughout the rest of the library.
* NMEA  - NMEA serialization, deserialization, manipulation, and data objects.
* UBX   - U-blox UBX protocol and PUBX sentence serialization, deserialization, manipulation, and
  data objects.
* Tools - Useful GNSS data manipulation functions.

Alongside the library, example and testing code (both unit and functional tests) is maintained.
This code is not distributed directly with the library, however, it is made available as separate
packages for those interested in installing and running them.

3 Specific Architecture
=======================

3.1 Architectural Design
------------------------

From the overview above the basic structure of the library is given, with four packages: Core,
NMEA, UBX, and Tools. Here we'll break down the structure further.

3.1.1 The Core Package
^^^^^^^^^^^^^^^^^^^^^^

The Core package contains base classes, functions, and helper code that is used throughout rest of
the library.

3.1.1.1 Base Classes
""""""""""""""""""""



* ``dump()``
* ``load()``

3.1.2 The NMEA Package
^^^^^^^^^^^^^^^^^^^^^^

The NMEA package is dedicated to serializing, deserializing, and storing GNSS data found in NMEA
sentences. Each NMEA sentence is represented by one module (or python file) with a single class
which stores the data present in that sentence. Every NMEA sentence class also contains the
following functions:

* ``serialize()``   - Converts the data contained in the class to an NMEA sentence in string form.
* ``deserialize()`` - Parses a provided NMEA sentence in string form and stores the data inside the
  class. This data may then be accessed via accessors.

3.1.3 The UBX Package
^^^^^^^^^^^^^^^^^^^^^

3.1.4 The Tools Package
^^^^^^^^^^^^^^^^^^^^^^^

3.2 Design Rationale
--------------------

Why did you choose the design you did?
Why is it better than other explored designs?

4 Data Design
=============

Describe the data structures used by the design.

4.1 Data Description
--------------------

Describe how data structures are generated.
Describe how data flows through the system.
Describe how data is stored, processed, and organized.

4.2 Data Dictionary
-------------------

List all major data structures and objects.
Describe what parts of memory they reside in, their sizes, types, and scope, descriptions of their purpose, and which components utilize them.
May be in the form of a table.

5 Component Design
==================

Subsections dedicated to describing in detail each component listed in 3.1 (Architectural Design).
Pseudocode is appropriate here.

6 Interface Design
==================

Describe all places where data can flow into or out of the product or between components.

6.1 Internal Interfaces
-----------------------

Detailed description of both public and private interfaces that face another component in the product.
Error handling between components may be discussed here.
Describe internal APIs.
Link to classes, functions, and/or groups using `@ref`.

6.2 External Interfaces
-----------------------

Detailed description of both public and private interfaces that face the rest of the system/user.
Example uses are helpful.
Error handling may be discussed here.
Describe external APIs.