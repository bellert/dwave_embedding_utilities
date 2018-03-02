import sys
import os
from setuptools import setup

# add __version__, __author__, __authoremail__, __description__ to this namespace
_PY2 = sys.version_info.major == 2

# change directories so this works when called from other locations. Useful in build systems.
setup_folder_loc = os.path.dirname(os.path.abspath(__file__))
os.chdir(setup_folder_loc)

if _PY2:
    execfile(os.path.join(".", "dwave", "embedding", "utilities", "package_info.py"))
else:
    exec(open(os.path.join(".", "dwave", "embedding", "utilities", "package_info.py")).read())

setup(
    name='dwave_embedding_utilities',
    version=__version__,
    author=__author__,
    author_email=__authoremail__,
    description=__description__,
    url='https://github.com/dwavesystems/dwave_embedding_utilities',
    license='Apache 2.0',
    py_modules=['dwave_embedding_utilities']
)
