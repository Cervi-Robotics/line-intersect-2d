Usage
=====

First you need to create your
:class:`~line_intersect_2d.quadtrees.Path` objects.
Assume that paths you pass are numbered from 0 to n.

After you make them, you just pass them to

.. autofunction:: line_intersect_2d.quadtrees.check_intersection

Note that a `split_factor` will divide the grid into `(1/split_factor)**2`, so in case
of the default `split_factor` of 0.1 100 subrectangles will be made.

Which will return either a tuple of (:class:`~line_intersect_2d.basics.Segment`,
:class:`~line_intersect_2d.basics.Segment`) two segments from different paths
(which paths it will be stored in their
:py:obj:`~line_intersect_2d.basics.Segment.tag` attribute, the number that
was aforementioned) or `None` will be returned, if they don't collide

You can use later :meth:`line_intersect_2d.basics.Segment.intersection_point` to calculate
the intersection point.
