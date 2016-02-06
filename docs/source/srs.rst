####################################
Software Requirements Specifications
####################################

:authors:
  Liam Bucci
:date:
  2016-02-04
:copyright:
  See LICENSE for copyright and licensing information.

1 Introduction
==============

The Eärendil library is used for manipulation, creation, and parsing of GNSS related data,
including NMEA strings and manufacturer specific data objects.

1.1 Purpose
-----------

This document defines the functional requirements of the Eärendil library. The intended audience
is developers, technical users familiar with the internal workings of Eärendil, and technical
users wishing to utilize the Eärendil library for their own projects.

1.2 Definitions
---------------

Deserialize
  Translate a GNSS message from a serial format, such as UBX or NMEA, to a Python data object or
  class.

NMEA Strings
  Standardized, human-readable strings containing GNSS and location data defined by the National
  Marine Electronics Association.

Serialize
  Translate a Python data object or class to a UBX message in the serial array format described in
  the UBX protocol.

UBX
  The u-blox specific, binary protocol used for communication of GNSS data.

1.3 System Overview
-------------------

The Eärendil library provides functionality for serializing, deserializing, parsing, and
manipulating GNSS data objects. These objects include:

* Standard NMEA strings
* u-blox UBX protocol
* u-blox PUBX protocol

The library is written in Python and provides an installable package which may then be imported
into end user applications.

The installable package includes the GNSS data object code as well as some basic tools to
manipulate the data in those objects.

The library also provides some basic example command line applications for interacting with GNSS
receivers via a serial port as well as doing post processing of data via log files.

1.4 References
--------------

1. NMEA 0183: https://en.wikipedia.org/wiki/NMEA_0183
2. u-blox 7 Receiver Description: https://www.u-blox.com/sites/default/files/products/documents/u-blox7-V14_ReceiverDescrProtSpec_(GPS.G7-SW-12001)_Public.pdf
3. IEEE 29148-2011: https://standards.ieee.org/findstds/standard/29148-2011.html

2 Overall Description
=====================

2.1 Product Perspective
-----------------------

There are two major parts to the Eärendil library: a Python package and command line tools. The
Python package is the actual library containing the GNSS data manipulation functionality and the
command line tools are example uses of that library as well as utilities for interacting with GNSS
receivers.

The library does not require the command line tools to be useful. It may be imported into any
Python project and the functions and classes provided may be used to serialize, deserialize, and
manipulate GNSS data.

The command line tools provide some basic interface capabilities for communicating with GNSS
receivers as well as parsing log files and generating commands.

2.1.1 System Interfaces
^^^^^^^^^^^^^^^^^^^^^^^

The Eärendil library is self contained and does not have any system requirements other than
Python. The command line tools require `pyserial` to be installed and available.

2.1.2 User Interfaces
^^^^^^^^^^^^^^^^^^^^^

The Python package provided by the Eärendil library exposes a public API, including function calls
and data objects for serializing, deserializing, and manipulating UBX message data.

The command line tools provided by the library provide a command line user interface for
interacting with the Python package's API. These tools offer simple command line switches, stdin,
and stdout as a means of interactive with the software.

2.1.3 Hardware Interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^

The command line tools provided by this library communicate (send and receive data) over any
serial port available to the computer running it. The tools must also be able to configure the
serial port, including bit configuration and baud rate in order to communicate with a connected
u-blox chip.

2.1.4 Software Interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^

The library and command line tools are all written in Python and therefore must interact with the
Python interpreter, including importing standard Python packages.

The library and command line tools must also be able to interact with the operating system on
which they are running. This is used for serial port communication, interacting with other
libraries, and reading and writing to files.

2.1.5 Communication Interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Eärendil command line tools may use a serial port to communicate with a u-blox chip via UART.

2.2 Product Functions
---------------------

TBD

2.3 User Characteristics
------------------------

Typical users of the Eärendil library will be developers who are familiar with Python and GNSS
applications.

2.4 Constraints
---------------

The Eärendil library is written in Python in order to be more portable as well as to encourage the
growth and learning of its author.

2.5 Assumptions and Dependencies
--------------------------------

TBD

3 Specific Requirements
=======================

3.1 External Interface Requirements
-----------------------------------

.. _REQ-0001:

REQ-0001
  All GNSS data objects shall provide a serialize function.

.. _REQ-0002:

REQ-0002
  All GNSS data objects shall provide a deserialize function.

.. _REQ-0003:

REQ-0003
  All GNSS data objects shall provide a function to generate a human-readable string from the GNSS
  data contained in the object (e.g. `__str__`).

.. _REQ-0004:

REQ-0004
  All GNSS data objects shall provide a function to generate JSON formatted data from the GNSS data
  contained in the object.

.. _REQ-0005:

REQ-0005
  All GNSS data objects shall provide accessors for all GNSS data contained in the object.

.. _REQ-0006:

REQ-0006
  All GNSS data objects shall provide mutators for all GNSS data contained in the object.

.. _REQ-0007:

REQ-0007
  All GNSS data objects shall initialize all GNSS data to sensible defaults.

3.2 Performance Requirements
----------------------------

None

3.3 Design Constraints
----------------------

None

3.4 Software System Attributes
------------------------------

3.4.1 Reliability
^^^^^^^^^^^^^^^^^

None

3.4.2 Availability
^^^^^^^^^^^^^^^^^^

None

3.4.3 Security
^^^^^^^^^^^^^^

None

3.4.4 Maintainability
^^^^^^^^^^^^^^^^^^^^^

None

3.4.5 Portability
^^^^^^^^^^^^^^^^^

.. _REQ-0008:

REQ-0008
  All code shall be compatible with the following versions of Python:

  * Python 2.6.x
  * Python 2.7.x
  * Python 3.0.x
  * Python 3.1.x
  * Python 3.2.x
  * Python 3.3.x
  * Python 3.4.x
  * Python 3.5.x

3.5 Test Requirements
---------------------

.. _REQ-0009:

REQ-0009
  Distributed library code shall be unit tested with minimum 90% LOC coverage.

.. _REQ-0010:

REQ-0010
  Distributed utility and tool code shall be unit tested with a minimum of 90% LOC coverage.

.. _REQ-0011:

REQ-0011
  Distributed library code shall be functionally tested using a realistic set of data which
  exercises the following interfaces of each GNSS data object:

  * serialization
  * deserialization
  * JSON creation

3.6 Other Requirements
----------------------

None