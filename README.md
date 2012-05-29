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

Don't forget

* text encoding: 
        is essentially simple floating point numbers from 0—100, inclusive.

* simple encoding:
        lets you specify integer values from 0—61, inclusive, encoded by a 
        single alphanumeric character. This encoding results in the shortest 
        data string of any of the data formats (if any values are greater than 9). 

* extended encoding:
        lets you specify integer values from 0—4095, inclusive, encoded by two 
        alphanumeric characters. Extended encoding is best suited to a chart with 
        a lot of data and a large data range.

