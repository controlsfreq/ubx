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

Provides an overview of the entire SDD.

1.1 Purpose
-----------

Delineate the purpose of the SDD.
Specify intended audience.

Example: This document is intended to layout the software application design of the <insert name> as well as the background, context, and rationale for that design. It is written for an Airware developer audience and may contain technical descriptions and Airware specific terminology.

1.2 Definitions
---------------

Provide definitions of all terms, acronyms, and abbreviations.
May reference an appendix.

1.3 Overview
------------

Short summary of system.
Identify software product(s) to be produced by name.
Explain succinctly what the software product(s) will do, including a very general description of the implementation.
Describe the application of the software being described, including relevant benefits, objectives, and goals.

1.4 References
--------------

List all references used in the creation of the SRS.
May reference an appendix.

1. My favorite reference: http://example.com
2. My second favorite reference: http://en.wikipedia.com

2 System Overview
=================

Describe the entire system and how the product(s) fit into that system.
High-level, system diagrams are very useful here (especially showing where the product interfaces with other system components).

3 Specific Architecture
=======================

Describe the structure of the design.

3.1 Architectural Design
------------------------

Describe the high-level structure of the design including all components.
What are the basic functions of each component?

3.2 Decomposition Description
-----------------------------

Describe in greater detail how the components interact.
How does data flow through the product?
Decomposition diagrams, sequence diagrams, data flow diagrams, and hierarchy diagrams are excellent here.

3.3 Design Rationale
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