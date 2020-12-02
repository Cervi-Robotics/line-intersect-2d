Usage
=====

First you need to create your
:class:`~line_intersect_2d.quadtrees.Path` objects.
Assume that paths you pass are numbered from 0 to n.

After you make them, you just pass them to

.. autofunction:: line_intersect_2d.quadtrees.check_intersection

Which will return either a tuple of (:class:`~line_intersect_2d.basics.Segment`,
:class:`~line_intersect_2d.basics.Segment`) two segments from different paths
(which paths it will be stored in their
:py:obj:`~line_intersect_2d.basics.Segment.tag` attribute, the number that
was aforementioned) or `None` will be returned, if they don't collide
