**Repo closed as of April 25th 2014.**

This was a convenient place for us to all push code to during
the PyCon 2014 sprints. Different pieces are being moved into seperate
repos where we can maintain them as the seperate libraries they should be. Any
questions or suggestions, get in touch:
https://groups.google.com/a/webfoundation.org/forum/#!forum/public-ocds-dev

Contributors
----------------------
Many thanks to all our contributors from PyCon 2014. In
alphanetical order:

* Eric Canen
* Aaron Cohen
* Andreas Dewes
* Noé Domínguez Porras
* Simon Frid
* Michael Glaude
* Bryan Gorges
* Brittain Hard
* Brantley Harris
* Matt Lamberti
* Dan Langer
* Herb Linchberg
* Teddy McWilliams
* Aaron Rothenberg
* David Street
* Nick Zaccardi

With additional thanks to: Jean-Paul, Ian Ward, Olivier, Bob Lannon for their
tips and pointers along the way.

From the open contracting data team:

* Sarah Bird
* Ana Branducescu
* Tim Davies
* Michael Roberts


Open Contracting Data
===================

We are trying to provide public data on government contracting and to build open 
standards on its publication. This enables everyone to better track and 
understand where and how money flows around the world.

Four Initiatives for this sprint:

- Datamap Landscape
- Data Comparison
- Usecase Documentation

Resources:

- Hackpads with more information: https://opencontractingdata.hackpad.com/
- Existing datasets: http://ocds.stage.aptivate.org/opendatacomparison/datasets/


Data Landscape
---------------

Creating an overall understanding about the types and format of existing
published contracting data.

Sprint goals:

    - Classification of Dataset Fields
      We want to classify each field/column in our various datasets into 
      "buckets" that build a picture of the sort of data we have available.
      Sub goals:
        - Manually classify many fields
        - Find the feasability of doing it with supervised machine learning
        - Explore unspervised clustering
    - Build visualization of the landscape

Resources:

    - Machine learning talk: http://pyvideo.org/video/2612/enough-machine-learning-to-make-hacker-news-reada
    - Work on manually classifying fields: https://docs.google.com/spreadsheet/ccc?key=0AqLP9fZSKM8jdFg2WGhHQi1QbE54Wml5aDNyaUVDRGc&usp=sharing#gid=0

Setup:

    Mac OS:
    - brew install gfortran
    - cd landscape
    - virtualenv env
    - env/bin/pip install -r requirements.txt
    - ipython notebook

Open Data Comparison
---------------------

The data comparison is a site based on open-comparison.  Our goals are to
make it useable to find and compare datasets.

    - Bugfixing
    - Make community usable

Use Case Comparison
-------------------

Collecting and documenting use cases for Open Contracting data and providing a
tool for people to submit new use cases.
