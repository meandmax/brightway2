.. _intro:

Introduction
============

Data structure
--------------

Brightway2 is a framework for life cycle assessment (LCA). The word framework was chosen carefully, and the most powerful way to use Brightway2 is as a component of something bigger you want to build.

The basic organization is hierarchical:

.. image:: images/org-scheme.png
    :align: center

At the top, we have projects. A project is a workspace with its own databases, LCI methods, and any other data you need. Each project is completely independent of other projects. Each project is a subdirectory in the file system.

Inside a project we have a number of objects that store data. Some of this data can be specific to a project, and not about LCA at all. For example, a database of vehicle registrations and lifetimes could be used to generate a fleet-based functional units for mobility assessments. However, the most common data objects as inventory *databases* and impact assessment *methods*.

The default way to store inventory databases is in a `SQLite <https://www.sqlite.org/>`__ database with two tables: *activities* and *exchanges*. Brightway2 shortens "inventory database" to just database, and a database is data that describes a supply chain graph. Nodes in this graph are called "activities", and include transforming and market activities, but also products and biosphere flows. Edges are called "exchanges", and describe a link between two nodes. An exchange could describe the input of a product to a transforming activity, or an emission of a biosphere flow by an activity, or the name and amount of a product produced by an activity.

Databases can include all kinds of nodes, including activities and biosphere flows. Edges can link from one database to another, and database can include circular dependencies (where A links to B, B links to C, and C links to A).

SimaPro differentiates between projects and libraries, but both would be databases in Brightway2.

Unique IDs
``````````

Activities are identified by their database name and a unique ``code``. A code is a string of letters and numbers that uniquely identifies an activity within the database. Codes can be written by humans, e.g. ``"Chris's first pony"``, or generated by by the computer using an algorithm.

Activities do not have very many required fields; aside from ``database`` and ``code``, the only other required field  is ``name``, but most activities will have a ``location`` and ``unit`` as well.

If no ``type`` is specified for an activity, then the activity is assumed to be a ``process``. Other types include ``product`` and ``biosphere`` for biosphere flows. Activity ``type``s are used to determine whether an activity should be placed in the biosphere or technosphere matrices during LCA calculations.

Exchanges are links between two activities of any type. Exchanges have an ``input`` and an ``output``: ``input`` is the activity being consumed or produced, and ``output`` is the consumer or producer. Exchanges should also have an ``amount`` and a ``type``. Common types include ``technosphere``, ``biosphere``, and ``production``. Multiple exchanges between two activities are allowed, and will be added together during LCA calculations.

Many activities have a reference product, which is an exchange of type ``production`` where the ``input`` is the same as the ``output``.

Brightway2 allows multioutput processes; you are responsible for making sure the final system make mathematical sense (see `multioutput processes in LCA <http://chris.mutel.org/multioutput.html>`__).