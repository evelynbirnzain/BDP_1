# This your assignment report

It is a free form. you can add:

* your designs
* your answers to questions in the assignment
* your test results
* etc.

The best way is to have your report written in the form of point-to-point answering the assignment.

## Part 1: Design

1. Explain your choice of the application domain and generic types of data to be supported and
   technologies for ``mysimbdp-coredms``. Explain your assumption about the tenant data sources and
   how one could get data from the sources. Explain under which situations/assumptions, your platform
   serves for big data workload. (1 point)
2. Design and explain the interactions among main platform components in your architecture of
   ``mysimbdp``. Explain how would the data from the sources will be ingested into the platform. Explain
   which would be the third parties (services/infrastructures) that you do not develop for your
   platform. (1 point)
3. Explain a configuration of a cluster of nodes for ``mysimbdp-coredms`` so that you prevent a single-
   point-of-failure problem for ``mysimbdp-coredms`` for your tenants. (1 point)
4. You decide a pre-defined level of data replication for your tenants/customers. Explain the level of
   replication in your design, how many nodes are needed in the deployment of mysimbdp-coredms for
   your choice so that this component can work property (e.g., the system still supports redundancy in
   the case of a failure of a node). (1 point)
5. Consider the platform data center, the tenant data source locations and the network between them.
   Explain where would you deploy ``mysimbdp-dataingest`` to allow your tenants using ``mysimbdp-dataingest`` to push
   data into ``mysimbdp``, based on which assumptions you have. Explain the
   performance pros and cons of the deployment place, given the posibilities you have. (1 point)

## Part 2: Implementation

1. Design, implement and explain one example of the data schema/structure for a tenant whose data
   will be stored into ``mysimbdp-coredms``. (1 point)
2. Given the data schema/structure of the tenant (Part 2, Point 1), design a strategy for data
   partitioning/sharding, explain the goal of the strategy (performance, data regulation and/or what),
   and explain your implementation for data partitioning/sharding together with your design for
   replication in Part 1, Point 4, in ``mysimbdp-coredms``. (1 point)
3. Assume that you are the tenant, emulate the data sources with the real selected dataset and write a
   ``mysimbdp-dataingest`` that takes data from your selected sources and stores the data into
   ``mysimbdp-coredms``. Explain what would be the atomic data element/unit to be stored. Explain
   possible consistency options for writing data in your ``mysimdbp-dataingest``. (1 point)
4. Given your deployment environment, measure and show the performance (e.g., response time,
   throughputs, and failure) of the tests for 1,5, 10, .., n of concurrent ``mysimbdp-dataingest writing
   data into mysimbdp-coredms`` with different speeds/velocities together with the change of the
   number of nodes of ``mysimbdp-coredms``. Indicate any performance differences due to the choice of
   consistency options. (1 point)
5. Observing the performance and failure problems when you push a lot of data into ``mysimbdp-coredms`` (you do not need
   to worry about duplicated data in ``mysimbdp``), propose the change of your
   deployment to avoid such problems (or explain why you do not have any problem with your
   deployment). (1 point)

Note: in the implementation, we do not require you to implement ``mysimbdp-daas``. It is up to you to
decide. Furthermore, a condition in performance testing is to also change the number of nodes of
``mysimbdp-coredms``. Therefore, if you use public cloud deployment of your selected databases, you
must be able to manipulate the number of nodes.

## Part 3: Extension

1. Using your ``mysimdbp-coredms``, a single tenant can run ``mysimbdp-dataingest`` to create many
   different databases/datasets. The tenant would like to record basic lineage of the ingested data,
   explain what types of metadata about data lineage you would like to support and how would you do
   this. Provide one example of a lineage data. (1 point)
2. Assume that each of your tenants/users will need a dedicated ``mysimbdp-coredms``. Design the data
   schema of service information for ``mysimbdp-coredms`` that can be published into an existing registry
   (like ZooKeeper, consul or etcd) so that you can find information about which ``mysimbdp-coredms`` is
   for which tenants/users. (1 point)
3. Explain how you would change the implementation of ``mysimbdp-dataingest`` (in Part 2) to integrate
   a service discovery feature (no implementation is required). (1 point)
4. Assume that now only ``mysimbdp-daas`` can read and write data into ``mysimbdp-coredms``, how would
   you change your ``mysimbdp-dataingest`` (in Part 2) to work with ``mysimbdp-daas``? (1 point)
5. Assume that the platform allows the customer to define which types of data (and) that should be
   stored in a hot space and which should be stored in a cold space in the ``mysimbdp-coredms``. Provide
   one example of constraints based on characteristics of data for data in a hot space vs in a cold space.
   Explain how would you support automatically moving/extracting data from a hot space to a cold
   space. (1 point)