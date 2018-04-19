## PyDart2

<table>
<tr>
<td>  
  <img src="https://github.com/dartsim/dart/raw/master/doxygen/DART%20logo.png" width="150" height="50" />
</td>
<td>
  <img src="https://www.python.org/static/community_logos/python-logo.png" width="150" height="50" />
</td>
</tr>
</table>

- News!
 + [2016/09/24] PyDART2 now supports both Python2 and Python3.
 + [2016/08/05] PyDART is upgraded to PyDART2, for easier installation and richer APIs.

======
PyDART2 is an open source python binding of DART, an open source physics
simulator. Its APIs are designed to provide concise and powerful control on
DART physics worlds. Further, a user can write simulations with a numerous
python scientific libraries, such as NumPy(linear algebra),
SciPy(optimization), scikit-learn (machine learning), PyBrain(machine
learning), and so on.

======
## Environment
+ Ubuntu 16.04
+ Python2 / Python 3
+ DART 6.1.0 (or higher. Tested on DART 6.4): https://github.com/dartsim/dart/

======
## Build Status

[![Build Status](https://api.travis-ci.org/sehoonha/pydart2.svg)](https://travis-ci.org/sehoonha/pydart2)
[![Doc Status](https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat)](http://pydart2.readthedocs.io/en/latest/)
[![Code Health](https://landscape.io/github/sehoonha/pydart2/master/landscape.svg?style=flat)](https://landscape.io/github/sehoonha/pydart2/master)

======
## Building and installation from source 
For Python2 users, please apply the following commands:

```bash
   sudo apt-get install swig python-pip python-qt4 python-qt4-dev python-qt4-gl
```

First, please check out the repository.

```bash
   git clone https://github.com/riturajkaushik/pydart2.git
   cd pydart2
```

The next step is to compile the package using setup.py

On the cluster/server, use the branch ```on_cluster``` as it has conditional building of graphics related things depending upon the availability of graphics headers in dart/includes.

If you have installed Dart from source and it was built it with option **'-DDART_ENABLE_SMID=ON'**, then your dart library was built with CXX flag **'-march=native'**. So to match that, you have to build pydart2 with that CXX flag enabled. Otherwise pydart2 will give runtime error (stack smashing). So to compile pydart2 with '-march=native' flag, do the following:

```bash
    python setup.py build build_ext -DART_ENABLE_SIMD=ON 
```

Otherwise, do the following:

```bash
    python setup.py build build_ext
```

The final step is to install the python package as a development.

```bash
    python setup.py develop
```

======
## Documentation
+ http://pydart2.readthedocs.io/en/latest/

======
## Contact
Please contact me when you have questions or suggestions: sehoon.ha@gmail.com
Note: I am much more responsive for emails than pull-requests!
