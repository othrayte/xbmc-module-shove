Common object storage frontend that supports
dictionary-style access, object serialization
and compression, and multiple storage and caching
backends.

Currently supported storage backends are:

- Amazon S3 Web Service
- Apache Cassandra
- Berkeley Source Database
- DBM
- Durus
- FTP
- Filesystem
- Firebird
- Memory
- Microsoft SQL Server
- MySQL
- Oracle
- PostgreSQL
- Redis
- SQLite
- Subversion
- Zope Object Database (ZODB)

Currently supported caching backends are:

- Filesystem
- Firebird
- Memory
- Microsoft SQL Server
- MySQL
- Oracle
- PostgreSQL
- SQLite
- memcache

The simplest *shove* use case is:

>>> from shove import Shove
>>> store = Shove()

which creates an in-memory store and cache.

The use of other backends for storage and caching involves
passing an module URI or existing store or cache instance
to *shove* following the form:

>>> from shove import Shove
>>> <storename> = Shove(<store_uri>, <cache_uri>)

Each module-specific URI form is documented in its module. The
URI form follows the URI form used by SQLAlchemy:

    http://www.sqlalchemy.org/docs/core/engines.html

*shove* fully implements the Python dictionary/mapping API:

    http://docs.python.org/lib/typesmapping.html
