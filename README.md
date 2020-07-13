# minimal_python_package 📦 🐍

Who is this for:

* 🙋 You know how to write python code
* 🙋‍♀️ You know how to write python functions
* 🙋‍♂️ You want to know how to write python packages and you're more of a doer than a reader

README Outline:
* ⬇️ [Overview and usage](#overview-and-usage): Proving that this repo holds an installable & functional package.
* 📄 [More on packages](#more-on-packages): Very brief writeups & resource links to address python package concepts shown in this repo.
* 🏋️ [Practice prompts](#practice-prompts): Prompts for how to practice packages using this repo.  Extend and create.

## Overview and usage

### Installation

*The package itself isn't too useful.  So these instructions are more to show that this repo does hold everything for an installable, usable, & functional package.*

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

`__init__.py` is the magic sauce to change a directory of Python files into a package.  For instance, the IDE PyCharm has an option to create a new Python Package, and this option creates a directory with a single file in it, `__init__.py`.  In this repo, the package is the directory `my_pkg`, take a second to look in the folder and the files' contents.  We have 2 files containing functions and then the good ole `__init__.py`.

In the `__init__.py` we can specify how users can reach our functionality.  For example, core functionality might be listed out here so users can access easier.  In this package the area functions might be considered more core because they're listed in `__init__.py`.  Note in `example_using_pkg.py` how this effects how we interact with the area vs perimeter functions.

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

## Practice Prompts

### Modifying / Extending this package

* Add the functions for the area & perimeter of a circle
  * Add the area function to `__init__.py` in the same way the other area functions have been done
  * Add an example of using these functions to `example_using_pkg.py`
* Add a new file to the package to hold helper functions for calculating `volume` of some shapes (rectanglur prism, cube, sphere, etc.)
  * Add an example of using these functions to `example_using_pkg.py`
* Add a `Rectangle` class ([An intro to writing classes](https://www.w3schools.com/python/python_classes.asp))
  * In your classes `__init__` method, store width, height, area, and perimeter as instance variables (use the packages functions for area & perimeter).
  * Add a method called `transpose` that swaps the width and height attributes (i.e. if `w=2` and `h=3`; this method should change it so that `w=3` and `h=2`)
  * Add an example of using this class.  In the example, print out the attributes you added to ensure they're correct.

### Creating a package from scratch following this architecture

1. Make up what your package will do (start with something not too useful)
   * One dumb idea that fits the bill is a meme generator package with functions like:
     * `spongebob_text()` that will convert inputted text to alternating capitilization (i.e. `"like this you see"` -> `"LiKe ThIs YoU sEe"`)
     * `top_bottom_text()` that takes in arguments for top/bottom text and makes the text all caps, prints out the top text, prints out whitespace, and then prints out bottom text.  Default the `top_text` argument to `"TOP TEXT"`; default the `bottom_text` argument to `"BOTTOM TEXT"`

2. Create a new GitHub repo to hold your package (create it with a python `.gitignore`, `LICENSE`, and `README.md`)
3. Clone your repo to begin working
4. Create the package following the structure laid out in this repo
   * [ ] Package itself including:
     * [ ] code
     * [ ] `__init__.py`
   * [ ] `requirements.txt`
   * [ ] `setup.py`

5. Push the code to GitHub
6. Test out installing and using your package

-----

Message me by opening up an issue / email / other means if you know other ways to contact me.  No promises I'll be able to answer everything in a timely manner (or at all), but I'd like to think I'll do my best to help you out with any problems.
