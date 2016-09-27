# RestrictedViews

Class based generic views that automatically check permissions

Enhanced and updated version of restricted views from humphreymurray on djangosnippets
https://djangosnippets.org/snippets/2317/

Simple wrappers around the new class-based generic views that also check permissions.

Quick start
-----------

1. Add "django_restricted_views" to your ``INSTALLED_APPS`` settings like this:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'django_restricted_views',
    ]

2. Example Usage (views.py):

.. code-block:: python

    from django_restricted_views.views import RestrictedListView, RestrictedUpdateView

    class MyListView(RestrictedListView):

        model = MyModel

    class MyUpdateView(RestrictedUpdateView):

        model = MyModel

        ...

Requirements
------------

No dependencies.

Tested on `Django`_ 1.9.9, 1.10.1 with Python 2.7, 3.4, 3.5

.. _Django: http://www.djangoproject.com/

