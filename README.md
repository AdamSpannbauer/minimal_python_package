# minimal_python_package

## Overview and usage

### Installation

*The package itself isn't too useful.  So these instructions are more to show that this does repo does hold everything for an installable, usable, & functional package.*

The package in this repo can be installed with:

```
pip install git+https://github.com/AdamSpannbauer/minimal_python_package
```

Alternatively, this package can be installed by:

1. Cloning the repo
2. `cd minimal_python_package`
3. `pip install .`

### Usage

The file `example_using_pkg.py` shows how we can import and use functions from the package.

## More on packages

### What makes a package?

`__init__.py` is the magic sauce to change a directory of Python files into a package.  For instance, the IDE PyCharm has an option to create a new Python Package, and this option creates a directory with a single file in it, `__init__.py`.

### Importing code

Note, you can import functions file to file without using a package.  Packages aren't needed to re-use code; they have some functionality to help with this though.

```
.
├── area.py
└── geometry_homework.py
```

Let's say we have the above structure.  In `area.py` let's say we have the function `rect_area()`.  In the file `geometry_homework.py`, we could have the import `import area` and then use `area.rect_area()` (we could alternatively use `from area import rect_area()`).

### `requirements.txt`

Lists out the package requirements for your project (package names and versions).  [This is a good resource](https://note.nkmk.me/en/python-pip-install-requirements/) for more.

Note, your project doesn't need to be a package for this file to be useful.  Whenever starting a new project, I like to have this item of my getting started todo list.

### `setup.py`

This file is what leads our package to be easily installed with `pip`.  It contains some info on the package as well as sometimes duplicating some of the dependency info we have in `requirements.txt`.  See [here for `setup.py` vs `requirements.txt`](https://caremad.io/posts/2013/07/setup-vs-requirement/).

### Distributing packages (aka "how do i upload my package to pypi so anyone can install it"?)

I'll default to [this resource](https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives).