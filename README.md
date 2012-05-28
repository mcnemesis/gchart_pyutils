gchart_pyutils
==============

A collection of Python Utilites that make life easier when dealing with Google Chart API via Python (e.g Django)

Examples
========

Encoding Data for the Chart API
-------------------------------
    >>> from gchart_pyutils.encoding import *
    >>> values = [12,34.5,-10,500,223,0,2]
    >>> text_encode(values)
    't:12,34.5,-10,500,223,0,2'
    >>> simple_encode(values)
    's:BE_9bAA'
    >>> extended_encode(values)
    'e:BiEa__..ciAAAQ'
