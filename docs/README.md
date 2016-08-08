# Documentation

This is the documentation document for the work-at-olist project, bellow is
described each endpoint available in the API:

* **/channels/**

    Lists existing channels

* **/channel/<channel_uuid>**

    List all categories and subcategories of a channel, in a parent -> children
    structure

    params: Channel UUID

* **/category/<category_uuid>**

    Return a single category with their parent categories and subcategories.
    (eg. the category family)

    params: Category UUID

## Running Tests

The tests can be run using tox, in the repository root:

```
pip install -r requirements-test.txt
tox
```

Or directly running py.test:

```
pip install -r requirements-test.txt
cd work-at-olist
py.test
```

## Implementation Decisions

This section contains some implementation decisions taken during the
development.

### The use of UUIDs:

The README recommends not exposing IDs in the URL, a natural solution for this
would be using channel and category names/slug, but the fact that we can have
multiple categories with the same name in different tree positions or in
different channels made it cumbersome to generate a URL using names, and since
this recommendation 'usually' is related to the security problem of having
'sequential' IDs in the URL, that could be exploited if no restriction is added in
object access level, I decided to use UUIDs for identifying both channels and
categories, and that also for the API urls simplyfing them.

### The use of django-mptt:

The REAME also asks for tree read performance, and django-mptt is my go for
solution in these cases, that way I could create the API endpoint that responds
with the tree using a minimal number of queries by using the django-mptt
builtin capability of caching nodes.
