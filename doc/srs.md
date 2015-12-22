# Eärendil Software Requirements Specifications (SRS)

# 1 Introduction

The Eärendil library allows conversion between serialized UBX strings and human-readable strings or programmatic objects.

## 1.1 Purpose

This document defines the functional requirements of the Eärendil library. The intended audience is developers, technical users familiar with the internal workings of Eärendil, and technical users wishing to utilize the Eärendil library for their own projects.

## 1.2 Definitions

<dl>
<dt>UBX Data</dt>
<dd>Data that is encapsulated in a UBX protocol message format.</dd>

<dt>Deserialize</dt>
<dd>Translate a UBX message from the serial array format described in the UBX protocol to a Python data object or class, capable of being programmatically manipulated using 

## 1.3 System Overview

The Eärendil library provides functionality for serializing, deserializing, and manipulating UBX protocol data. The library is written in Python and provides an installable package which may then be imported into end user applications.

The library also provides some basic command line applications for interacting with a u-blox chip over a serial port. These applications allow a user to send and receive arbitrary UBX messages.

## 1.4 References

1. u-blox 7 Receiver Description: `https://www.u-blox.com/sites/default/files/products/documents/u-blox7-V14_ReceiverDescrProtSpec_(GPS.G7-SW-12001)_Public.pdf`
2. IEEE 29148-2011: `https://standards.ieee.org/findstds/standard/29148-2011.html`

# 2 Overall Description

## 2.1 Product Perspective

There are two parts to the Eärendil library: a Python package and command line tools. The Python package is the actual library containing the UBX data manipulation functionality and the command line tools are example uses of that library as well as utilities for interacting with u-blox GPS chips.

The library does not require the command line tools to be useful. It may be imported into any Python project and the functions and classes provided may be used to serialize, deserialize, and manipulate UBX data.

The command line tools provide a basic interface for communicating with a u-blox GPS chip and sending and receiving arbitrary UBX protocol messages.

### 2.1.1 System Interfaces

Because the Eärendil library is considered a single system it does not have any external, system interfaces.

### 2.1.2 User Interfaces

The Python package provided by the Eärendil library exposes a public API, including function calls and data objects for serializing, deserializing, and manipulating UBX message data.

The command line tools provided by the library provide a command line user interface for interacting with the Python package's API. These tools offer simple command line switches, stdin, and stdout as a means of interactive with the software.

### 2.1.3 Hardware Interfaces

The command line tools provided by this library communicate (send and receive data) over any serial port available to the computer running it. The tools must also be able to configure the serial port, including bit configuration and baud rate in order to communicate with a connected u-blox chip.

### 2.1.4 Software Interfaces

The library and command line tools are all written in Python and therefore must interact with the Python interpreter, including importing standard Python packages.

The library and command line tools must also be able to interact with the operating system on which they are running. This is used for serial port communication, interacting with other libraries, and reading and writing to files.

### 2.1.5 Communication Interfaces

The Eärendil command line tools may use a serial port to communicate with a u-blox chip via UART.

## 2.2 Product Functions

TBD

## 2.3 User Characteristics

TBD

## 2.4 Constraints

The Eärendil library is written in Python in order to be more portable as well as to encourage the growth and learning of its author.

## 2.5 Assumptions and Dependencies

TBD

# 3 Specific Requirements

## 3.1 External Interface Requirements

TBD

## 3.2 Performance Requirements

TBD

## 3.3 Design Constraints

TBD

## 3.4 Software System Attributes

TBD

## 3.5 Other Requirements

TBD
