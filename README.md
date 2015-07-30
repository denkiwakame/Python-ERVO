Python bindings for Optimal Reciprocal Collision Avoidance
==========================================================

This repository contains the RVO2 framework, as described below, along with
[Cython](http://cython.org/)-based Python bindings.

Building & installing
----------------------

Run `python setup.py build` to build, and `python setup.py install` to install.

Only tested with Python 3.4 on Ubuntu Linux. If you have success (or failure)
stories, please share them!

Differences with the C++ version
--------------------------------

The `Vector2` and `Line` classes from the RVO2 library are _not_ wrapped. Instead,
vectors are passed as tuples `(x, y)` from/to Python. Lines are passed as tuples
`(point x, point y, direction x, direction y)`.

An example:

```python
#!/usr/bin/env python

import rvo2

sim = rvo2.PyRVOSimulator(1/60, 1.5, 5, 1.5, 2, 0.4, 2)
a0 = sim.addAgent((0, 0), 0.4)
a1 = sim.addAgent((1, 0), 0.4)
a2 = sim.addAgent((1, 1), 0.4)
a3 = sim.addAgent((0, 1), 0.4)

sim.setAgentPrefVelocity(a0, (1, 1))
sim.setAgentPrefVelocity(a1, (-1, 1))
sim.setAgentPrefVelocity(a2, (-1, -1))
sim.setAgentPrefVelocity(a3, (1, -1))

print('Simulation has %i agents and %i obstacle vertices in it.' %
      (sim.getNumAgents(), sim.getNumObstacleVertices()))

print('Running simulation')

for step in range(20):
    sim.doStep()

    positions = ['(%5.3f, %5.3f)' % sim.getAgentPosition(agent_no)
                 for agent_no in (a0, a1, a2, a3)]
    print('step=%2i  t=%.3f  %s' % (step, sim.getGlobalTime(), '  '.join(positions)))
```


Optimal Reciprocal Collision Avoidance
======================================

<http://gamma.cs.unc.edu/RVO2/>

Copyright &copy; 2008-2013 University of North Carolina at Chapel Hill. All
rights reserved.

[![Build Status](https://travis-ci.org/snape/RVO2.png?branch=master)](https://travis-ci.org/snape/RVO2)

Permission to use, copy, modify, and distribute this software and its
documentation for educational, research, and non-profit purposes, without fee,
and without a written agreement is hereby granted, provided that the above
copyright notice, this paragraph, and the following four paragraphs appear in
all copies.

Permission to incorporate this software into commercial products may be obtained
by contacting the authors ([geom@cs.unc.edu](mailto:geom@cs.unc.edu)) or the
Office of Technology Development at the University of North Carolina at Chapel
Hill ([otd@unc.edu](mailto:otd@unc.edu)).

This software program and documentation are copyrighted by the University of
North Carolina at Chapel Hill. The software program and documentation are
supplied "as is," without any accompanying services from the University of North
Carolina at Chapel Hill or the authors. The University of North Carolina at
Chapel Hill and the authors do not warrant that the operation of the program
will be uninterrupted or error-free. The end-user understands that the program
was developed for research purposes and is advised not to rely exclusively on
the program for any reason.

IN NO EVENT SHALL THE UNIVERSITY OF NORTH CAROLINA AT CHAPEL HILL OR THE AUTHORS
BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR
CONSEQUENTIAL DAMAGES, INCLUDING LOST PROFITS, ARISING OUT OF THE USE OF THIS
SOFTWARE AND ITS DOCUMENTATION, EVEN IF THE UNIVERSITY OF NORTH CAROLINA AT
CHAPEL HILL OR THE AUTHORS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

THE UNIVERSITY OF NORTH CAROLINA AT CHAPEL HILL AND THE AUTHORS SPECIFICALLY
DISCLAIM ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE AND ANY STATUTORY
WARRANTY OF NON-INFRINGEMENT. THE SOFTWARE PROVIDED HEREUNDER IS ON AN "AS IS"
BASIS, AND THE UNIVERSITY OF NORTH CAROLINA AT CHAPEL HILL AND THE AUTHORS HAVE
NO OBLIGATIONS TO PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR
MODIFICATIONS.

Please send all bug reports to [geom@cs.unc.edu](mailto:geom@cs.unc.edu).

The authors may be contacted via:

Jur van den Berg, Stephen J. Guy, Jamie Snape, Ming C. Lin, and Dinesh Manocha  
Dept. of Computer Science  
201 S. Columbia St.  
Frederick P. Brooks, Jr. Computer Science Bldg.  
Chapel Hill, N.C. 27599-3175  
United States of America
