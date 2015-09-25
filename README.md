Python bindings for Optimal Reciprocal Collision Avoidance
==========================================================

This repository contains the RVO2 framework, as described below, along with
[Cython](http://cython.org/)-based Python bindings. Its home is
[GitHub](https://github.com/sybrenstuvel/Python-RVO2). New updates are released
there. There are no explicit version numbers -- all commits on the master
branch are supposed to be stable.


Building & installing
----------------------

Building requires [CMake](http://cmake.org/) and [Cython](http://cython.org/) to be installed.
Run `pip install -r requirements.txt` to install the tested version of Cython, or run
`pip install Cython` to install the latest version.

Run `python setup.py build` to build, and `python setup.py install` to install.
Alternatively, if you want an in-place build that puts the compiled library right in
the current directory, run `python setup.py build_ext --inplace'

Only tested with Python 2.7 and 3.4 on Ubuntu Linux. The setup.py script uses CMake to build
the RVO2 library itself, before building the Python wrappers. If you have success (or failure)
stories, please share them!


Differences with the C++ version
--------------------------------

The `Vector2` and `Line` classes from the RVO2 library are _not_ wrapped. Instead,
vectors are passed as tuples `(x, y)` from/to Python. Lines are passed as tuples
`(point x, point y, direction x, direction y)`.


Example code
------------

```python
#!/usr/bin/env python

import rvo2

sim = rvo2.PyRVOSimulator(1/60, 1.5, 5, 1.5, 2, 0.4, 2)

# Pass either just the position (the other parameters then use
# the default values passed to the PyRVOSimulator constructor),
# or pass all available parameters.
a0 = sim.addAgent((0, 0))
a1 = sim.addAgent((1, 0))
a2 = sim.addAgent((1, 1))
a3 = sim.addAgent((0, 1), 1.5, 5, 1.5, 2, 0.4, 2, (0, 0))

# Obstacles are also supported.
o1 = sim.addObstacle([(0.1, 0.1), (-0.1, 0.1), (-0.1, -0.1)])

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


Threading support
--------------------------------

Calling Python-RVO2 from multiple threads has not been tested. However, code that
may take longer to run (`doStep()`, `processObstacles()` and `queryVisibility(...)`)
release the Global Interpreter Lock (GIL) so that other Python threads can run while
RVO2 is processing.


Optimal Reciprocal Collision Avoidance
======================================

<http://gamma.cs.unc.edu/RVO2/>

Copyright &copy; 2008-2013 University of North Carolina at Chapel Hill. All
rights reserved.

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
