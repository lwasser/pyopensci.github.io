---
layout: single # posts <- has a nice wider layout>
permalink: tutorials/make-installable-python-package.html
classes: wide
title: "Make your Python code installable"
excerpt: "More here"
header:
  overlay_color: "#666"
  overlay_filter: 0.6
author_profile: false
---

{% include packaging-toc %}

# TODO list

- make the pyproj toml explanation much shorter and link to the next lesson
- consolidate the pyproj description as it's in there twice now.
- i think it would be cool to have a package spectrum graphic. on the left is you just have code that you want to use, then the code can be installed, then you can build a package... etc etc so each tutorial would highlight a step across that spectrum
- the packaging guide pyproject.toml page is really poor right now as is.

<div class="notice" markdown="1">
## Learning Objectives

In this lesson you will learn:

- How to make your code installable into a Python environment
- How to create a basic `pyproject.toml` file to declare dependencies and metadata
- How to declare a build backend which will be used to build and install your package (learn more about what build back ends are here - link to guide)
- How to install your package in editable mode for interactive development
</div>

## Make your package installable

It’s time to create your Python package. To make your code installable you need:

- A `pyproject.toml` file
- An (optional but recommended) `__init__.py` file in your code directory
- a specific directory structure
- some code.

The directory structure you’ll create in this first section looks like this:

```toml
pyospackage/
     └─ pyproject.toml
     └─ src/  # the src directory ensures your tests always run on the installed
             └── pyospackage/ # package directory where code lives, use the package name
              	     ├── __init__.py
                      ├── add_numbers.py
                      └──# Add any other .py modules that you want here
```

If you already know what all of the elements of this package structure are, you can skip to the next section &lt;add link>. Otherwise keep reading to learn about each element of the above structure.

**Maybe have steps here and then add the explanation below??**

Notice a few things about the above layout

1. Your package code lives within a `src/packagename` directory. While it’s fine if you wish to use a [flat layout](https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-structure.html#about-the-flat-python-package-layout) containing no `src/` directory, we suggest a src directory as it will make it easier for you to ensure you are always running tests on the installed version of your code. [More here on that](https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-structure.html#the-src-layout-and-testing)
2. Within the `src/` directory you have a package directory called pyospackage/. Use the name of your package for that directory name..
   1. You also have an `__init__.py` file and all of your python modules in your package directory.
3. The pyproject.toml file lives at the root directory of your package.

## Init.py and pyproject.toml files

The `__init__.py` and pyproject.toml files in the above layout are important to understand.

### What is an init.py file?

The `__init__.py` file tells python that the directory it’s in should be treated as a Python package. The `__init__.py` file also

- Allows you to organize multiple modules within the package.
- Allows you to create shortcuts for importing specific functions, and classes into your code (more on that later!)
- Allows you to create a version object for people to call **version**
- What else??

**TIP:** You can technically install a package without an `__init__.py` file since Python 3.3, we suggest that you include it in your package structure as it allows you to make some important customizations to your package’s user experience.
{: .notice--info }

### What is a pyproject.toml file?

The **pyproject.toml** file is:

- where you store your project’s metadata (including its name, authors, license, etc)
- where you store dependencies (the packages that it depends on)
- used to specify and configure what build back end you want to use to create your package.

A **pyproject.toml**: This file is critical for both installing your package and publishing to pyPi. This is where you will declare your project build system tools, dependencies and metadata. More on that later

After the `__init__.py` and pyproject.toml files have been added, your package can be built and distributed as an installable Python package using tools like pip.

Note that the `pyproject.toml` file needs to have the a few basic things for this to work including

- the build backend that you want to use,
- the project name, and a few other metadata elements.

Tip: **If you try to pip install a package with no `pyproject.toml` you will get the following error:**

```bash
GitHub/pyospackage/testme
➜ pip install .
ERROR: Directory '.' is not installable. Neither 'setup.py' nor 'pyproject.toml' found.
```

**Tip:** The `pyproject.toml` file replaces some of the functionality of both the setup.py file and setup.cfg files.
{: .notice .notice--tip}

## Try it yourself - Create your package structure!

Let’s get started. Create a directory structure similar to the structure below. If you don’t wish to make each of the elements below, you can always [fork and clone and customize the pyOpenSci example package, here](https://github.com/pyOpenSci/pyosPackage)

## Step 1: Set Up the Package Directory Structure

Create a new directory for your package. Choose a name for your package, preferably in lowercase and without spaces (e.g., "pyospackage").

Inside the package directory,

- Create a `src/` directory
- Within the `src/` directory, create a directory that is named after your package. This subdirectory will contain your package’s code.
- It is ok if the main directory of your package and the directory in `src/` have the same name

Next create two files:

- Inside the package directory, create a new file named `__init__.py` . This file ensures Python sees this directory as a package. You will use this file to customize how parts of your package are imported and to declare your package’s version in a future lesson.
- At the root of your directory, create a file called `pyproject.toml`

Your final package directory structure should look like this:

```
pyospackage/
     └─ pyproject.toml
     └─ src/
             └── pyospackage/
              	     ├── __init__.py
```

## Step 2: Add Code to Your Package

Within the `pyospackage` subdirectory, add 1 or more Python modules
(.py files) containing the code that you want your package to access and run.
If you don't have code already and are just learning how to create a python
package, then create an empty `add_numbers.py` file.

**Tip:** When you see the word module, we are referring to a .py file containing Python code.
{: .notice .notice--info }

```
pyospackage/
     └─ pyproject.toml
     └─ src/
             └── pyospackage/
              	    ├── __init__.py
                    ├── add_numbers.py

```

## Add some code to your add_numbers module

If you are following along and making a python package from scratch then you can add the code below to your `add_numbers.py` module. The function below adds two integers together and returns the result. Notice that the code below has a few features that we will review in future tutorials:

1. It has a [numpy-style docstring ](https://www.pyopensci.org/python-package-guide/documentation/write-user-documentation/document-your-code-api-docstrings.html#three-python-docstring-formats-and-why-we-like-numpy-style)
2. It uses [typing](https://www.pyopensci.org/python-package-guide/documentation/write-user-documentation/document-your-code-api-docstrings.html#adding-type-hints-to-your-docstrings)

If you aren’t familiar with docstrings or typing yet, that is ok. We will get
to it later in our tutorial series. Or You can review the pyOpenSci [packaging guide](https://www.pyopensci.org/python-package-guide/documentation/write-user-documentation/document-your-code-api-docstrings.html)
for an overview.

```python
def add_num(a: int, b: int) -> int:
    """
    Add two numbers.

    Parameters
    ----------
    a : int
        The first number to be added.
    b : int
        The second number to be added.

    Returns
    -------
    int
        The sum of the two input numbers (a + b).

    Examples
    --------
    >>> add_num(3, 5)
    8
    >>> add_num(-2, 7)
    5
    """
    return a + b
```

## Add metadata to your `pyproject.toml` file

Next, you will add some information to your `pyproject.toml` file. You are
are welcome to copy the file we have in our example repo here. <add link>

# TODO: add link to repo when it's ready

# below: add links to the packaging guide for build tools etc etc...

### A brief overview of the TOML file

The TOML format consists of tables and variables. Tables are sections of information denoted by square brackets:

`[this-is-a-table]`.

Tables can contain variables within them defined by an variable name and
an `=` sign. For
instance, a `build-system` table most often holds 2 variables:

1. `requires = `, which tells a build tool what tools it needs to install prior to building your package. in this case is
   [hatchling](https://pypi.org/project/hatchling/)
2. `build-backend` is used to define specific build-backend name, (in this example we are using `hatchling.build`).

TOML organizes data structures, defining relationships within a configuration
file. You will learn more about the pyproject.toml format in the
[next lesson when you add additional metadata / information to this file.](/python-package-tutorial/pyproject-toml.html)

```toml
# An example of the build-system table which contains two variables - requires and build-backend
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

- Open up your `pyproject.toml` file in your favorite text editor.
- Add the metadata below to your `pyproject.toml`

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "pyospackage_gh_user_name" # rename this if you plan to publish to test pypi
# Here you add the package version manually. You will learn how to setup # dynamic versioning in a followup tutorial.
version="1.1"

```

Note that above you manually add your package's version number to the
`pyproject.toml` file. You will learn how to automate defining a package
version using git tags in the version and release your package lesson. <ADD LINK>

**Tip** The core basic information that you need in a `pyproject.toml` file in order to publish on PyPI is the name of your package and the version. However, we suggest that you flesh out your metadata early on in the `pyproject.toml` file. Once you have your project metadata in the pyproject.toml file, you will
rarely update it. In the next lesson you’ll add more metadata and structure to this file.
{: .notice .notice--info }

## Install your package locally

At this point you should have:

1. A project directory structure with a `pyproject.toml` file at the root
2. A package directory containing an empty `__init__.py` file and
3. At least one Python module (e.g. `add_numbers.py`)

You are now ready to install (and build) your Python package!.

Let’s try it out.

- First `cd` into your package directory
- Activate the Python environment that you wish to use. (maybe show venv and conda examples here??)
- Next, open bash and run

# TODO: this requires an environment is setup. so have them set one up in a lesson before this lesson.

# TODO: add venv example too or atleast add it as a comment. then also run conda list and add pip list in a comment??

```bash
# Activate your environment using conda or venv
> conda activate pyosdev
(pyosdev)
>> conda info
     active environment : pyosdev
    active env location : /Users/your-path/mambaforge/envs/pyosdev
# Install the package
>> python -m pip install -e .

Obtaining file:///Users/leahawasser/Documents/GitHub/pyos/pyosPackage
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done

# Check to see if the package is installed
> conda list
# use pip list instead of conda list here if you are working in an venv environment rather than a conda envt
```

`python -m pip install -e .` installs your package into the current active
Python active environment in **editable mode**. Installing your package in
editable mode, allows you to work on your code and then test the updates
interactively. If you wish to install the package regularly (not in editable
mode) you can use:

- `python -m pip install . `

**Tip:** `python -m` you use this to ensure that you are calling the version of pip associated with your current active environment.
{: .notice .notice--info }

After installing your package, type “python” at the command prompt to start
a Python session in your active python environment.

You can now import your package and access the `add_num` function.

```bash
➜ python
Python 3.11.4 | packaged by conda-forge | (main, Jun 10 2023, 18:08:41) [Clang 15.0.7 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyospackage
>>> pyospackage.add_num(1, 2)
3
```

## Customize access to Python functions using the `__init__.py` file

> TODO: note that they may or may not understand modules etc... I have some text on this but make sure to link to that in the intro tutorials on the basics of packaging. Could this also introduce problematic behavior if users are learning and just add functions to the init file...it could...

Let's make one more tweak to the code.

If `add_num` is a function that you think users will use often, you may want to add it to your `__init__.py` file to allow them to import the function directly from the package rather than from the module.

### Add functions to your `__init__.py` file

To make a function or class available at the package level to a user, you can add it to the `__init__.py` file.

- Open the `__init__.py` file .
- At the top of the file add the import below.

```python
from pyospackage.add_numbers import add_num
```

Save the file.

Now, open up a NEW python terminal or restart your Python kernel.

It's important that you restart your Python kernel if you wish to access the changes to your code that you just made.
{: .notice .notice--important }

```python
> python
Python 3.10.12 | packaged by conda-forge | (main, Jun 23 2023, 22:41:52) [Clang 15.0.7 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from pyospackage import add_num
>>> add_num(1,2)
3
```

The decision to add specific functions, methods or classes to your
`__init__.py` file is up to you. However be sure that you do this thoughtfully
considering what functionality in your package you want to "elevate" to the top
level vs. what makes the most sense to keep in individual modules.

> TODO: Guidelines for when and how to add methods and such to the `__init__.py` file here.

> `__all__ = ['add_num']`

### Congratulations! You created your first Python package

You did it! You have now created a Python package that you can install into any Python environment. While there is still more to do, you have completed the first major step.

In the upcoming lessons you will

1. Flesh out metadata for your package within your `pyproject.toml` file.
2. Learn how to build your learn how to build your package distribution files (**sdist** and **wheel**) and
3. Learn how to publish your package on **testpypi**.

If you have a package that is ready for the mainstream user then you can also publish your package on PyPI.

### NOTES on this lesson

- Have something on pip and conda list to see the package in the envt…
- Could create a clean envt using venv first and then conda
- Then look at the list of installed things…
- Then define **all** = [“”] to avoid issues with pylance / mypy
