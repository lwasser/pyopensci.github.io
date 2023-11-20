---
layout: single
permalink: /python-package-tutorial/pyproject-toml.html
classes: wide
title: "Get your Python package PyPI ready - add metadata to your pyproject.toml file"
excerpt: "More here"
header:
  overlay_color: "#666"
  overlay_filter: 0.6
author_profile: false
---

myst-nb or nbsphinx to run code
https://learn.scientific-python.org/development/guides/packaging-simple/ <i can use this as a template to setup hatchling + vcs >

{% include packaging-toc %}

# TODO: they haven't added other files yet such as readme and license.

Below you will learn how to create this file and what to include in the file. If you are migrating from a **setup.py** or **setup.cfg** file, there are sections at the bottom of this lesson the cover what you might need to know when migrating.

<div class="notice" markdown="1">
## Learning Objectives

In this lesson you will learn:

1. sdf

</div>

## About the pyproject.toml file

Every modern Python package should include a `pyproject.toml` file. If your project is pure Python and you're using a "setup.py" file to describe its metadata, you should consider removing the metadata and pure python build information from the setup.py file and to a `pyproject.toml` file.

If your project isn’t pure-python, you might still require a "setup.py" file to build the non python extensions. However, a pyproject.toml file should still be used to store your project’s metadata.

### What is a pyproject.toml file?

The `pyproject.toml` file is a human and machine-readable TOML file that serves several purposes:

The pyproject.toml file tells your build tool:

- What build backend to use to build your package (e.g. setuptools, hatchling, pdm.build, etc)
- (in some cases) how to retrieve the package version (dynamically vs statically defined)
- What dependencies you are using
- It also provides metadata about your package that is stored in a METADATA file when you build your package.

For people looking at your GitHub repo, it’s a file that makes it easy for anyone to quickly understand:

- How your package is built,
- What python versions and operating systems it supports
- What it does, who maintains it, etc
- And more

The file is also often used to configure tools such as static type checkers (e.g. mypy), linters (eg black, ruff), and other tools.

<div class = "notice" markdown="1">
Prior to August 2017, Python package metadata was stored either in the setup.py file or a setup.cfg file. In recent years, there has been a shift to storing Python package metadata in a much more user-readable `pyproject.toml` format. Having all metadata in a single file:

- simplifies package management,
- allows you to use a suite of different [build backends](https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-build-tools.html#build-back-ends) such as (flit-core, hatchling, pdm-build), and
- aligns with modern best practices.
</div>

[Learn more](https://www.pyopensci.org/python-package-guide/package-structure-code/pyproject-toml-python-package-metadata.html) about the basics of the pyproject.toml file in our pyOpenSci packaging guide.

## Create your pyproject.toml file

In the previous lesson, you learned how to create a basic example of a pyproject.toml file that allowed you to install your python package into a local environment. In this file you defined:

1. The build tools to use (contained in the `[build-system`] table and
2. The package name and version (contained in the `[project]`table)

The pyproject.toml file that you created, looked like this:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "pyospackage"
version="1.1"
```

While the example above uses the `hatchling` build back-end you can chose
to use `setuptools` or any other tool you wish to create and build
your package.

[Learn more about packaging tools here](https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-build-tools.html)

**Tip:** Note that when using the toml format, each section is defined with a `[section-here]` and that section is commonly referred to as a "table".
{: .notice .notice--info }

### Things to consider in your pyproject.toml file

When creating your pyproject.toml file, consider the following:

1. As highlighted above, there are only two tables or tables that you need to install and publish your package: the **[build-system]** table and the **[project]** section.
2. The **[project]** table stores your package's metadata. There are only two _required_ fields in the **[project]** table: **name=** and **version=**. However, you should add more metadata here as it will make it easier for users to find your project on PyPI.
3. When you are adding classifiers to the [project] table, only use valid values from [PyPI’s classifier page](https://PyPI.org/classifiers/). An invalid value here will raise an error when you build your package or publish to PyPI.
4. There is no specific order for tables in the pyproject.toml file. However fields need to be placed within the correct table sections. For example `requires =` always need to be associated with the **[build-system]** table.
5. Related to the above while this is not required, we suggest that you include your **[build-system]** table at the top of your `pyproject.toml` file.

## Metadata in a pyproject toml

When you create your pyproject.toml file, there are numerous metadata fields that you can use. Below we suggest specific fields to get you started that support publication on PyPI and users finding your package.

[An overview of all of the project metadata elements can be found here. ](https://packaging.python.org/en/latest/specifications/core-metadata/#project-url-multiple-use)

### Required fields for the [project] table

As mentioned above, your pyproject.toml file needs to have a **name** and **version** field in order to properly build your package:

- Name: This is the name of your project provided as a string
- Version: This is the version of your project. If you are using a scm tool for versioning (using git tags to determine versions), then the version may be dynamic (more on that below).

### Optional fields to include int he [project] table

We strongly suggest that you also add the metadata keys below as they will
help users finding your package on PyPI. These fields will make it
clear how your package is structured, what platforms you support and
what dependencies your package requires.

- **Description:** this is a short one-line description of your package.
- **Readme:** A link to your README.md file is used for the long long-description. This information will be published on your packages PyPI landing page.
- **Requires-python** (used by pip): this is a field that is used by pip. Here you tell the installer whether you are using python 2.x or 3.x. Most projects will be using 3.x.
- **License:** the license you are using
- **Authors:** these are the original authors of the package. Sometimes the authors are different from the maintainers. Other times they might be the same.
- **Maintainers:** you can choose to populate this or not. You can populate this using a list with a sub element for each author or maintainer name, email

```toml
authors = [
  {name = "A. Random Developer", email = "author@example.com" }
]
```

- **dependencies:** dependencies are optional but we strongly suggest you include them in your pyproject.toml. Dependencies will be installed by pip when your project is installed creating a better user-experience.

- **`[project.optional-dependencies]`:** the optional or development dependencies will be installed if someone runs `pip install projectname[dev]`. This is a nice way to include your development dependencies for users who may wish to contribute to your project.

- **keywords:**these are the keywords that will appear on your PyPI landing page. Think of them as words that people might use to search for your package.
- **classifiers:** The classifiers section of your metadata is also important for the landing page of your package in PyPI and for filtering of packages in PyPI. A list of [all options for classifiers can be found her](https://PyPI.org/classifiers/)e. Some of the classifiers that you should consider including
  - Development Status
  - Intended Audience
  - Topic
  - LIcense
  - Programming language

### The project.urls table

`[project.urls]`: project.urls is its own table. This table contains links that are relevant for your project. You might want to include:

- **Homepage:** the documentation link for your project
- **Bug reports:** a link to your issues / discussions or wherever you want users to report bugs
- **Source:** the GitHub / GitLab link for your project.

## Example pyproject.toml file

Below is an example of a more fleshed out pyproject.toml file.

Check out the [pypa documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-pyproject-toml) if you are interested in setting build configurations for other tools.
{: .notice .notice--info }

![random image??](https://hackmd.io/_uploads/ByPoPOyyp.png)

# TODO - redundant with above??

Remember that each section of your toml file is defined by a section header encased in square brackets like this:
`[text-here]`
Each each section is referred to as a table in TOML. [Learn more about this file in our packaging guide.](https://www.pyopensci.org/python-package-guide/package-structure-code/pyproject-toml-python-package-metadata.html)

## Example file highlights

Notice a few things about the pyproject.toml file:

1. At the top, we specify the [build backend](https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-build-tools.html#build-back-ends)- being used. This is valuable as a user and potential new contributor can quickly understand what tools you're using to build your package. While you don’t need to list this at the top we suggest that you do. That way it’s easy for a contributor to quickly understand what tools you are using to create your package.
2. Below there is a `[project]` section. This is where you store your project's metadata. For the most part, this metadata is what PyPI will use to populate your landing page for your project.
3. There is:
   - a metadata section specifying python versions that your package supports (which is what PyPI uses to index your package)
   - and a `requires-python = ">=3.10"` that is important to have for pip.

![](https://hackmd.io/_uploads/HJ-p2J223.png)

\*NOTE: If you do not [use standard classifier values](https://PyPI.org/classifiers/), when you try to publish to PyPI your package distrobution will be rejected.

## Example pyproject.toml file

```toml
# You can delete all of the comments once you have created your own pyproject.toml file.

# The build system table. Here we use pdm.backend as the build back end tool.
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

# The [project] section contains your package's metadata
# notice that the version is setup to be dynamically generated using dynamic=[“version”]

[project]
name = "pyospackage"
# dynamic = ["version"] # you will learn how to dynamically set the version in lesson XX
version = "1.2" # manually assign version (not preferred)
description = "Tools that update the pyOpenSci contributor and review metadata that is posted on our website"
authors = [{ name = "Firstname lastname", email = "email@pyopensci.org" }]

# maintainers section is optional but suggested.
maintainers = [
    { name = "firstname lastname", email = "admin@pyopensci.org" }, # Optional
]

# Classifiers have set values - be sure to only use classifier values from the
# PyPI page here: https://PyPI.org/classifiers/

classifiers = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    "Development Status :: 4 - Beta",

    # Indicate who your project is intended for
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",

    # Pick your license (using syntax from the classifier page). We suggest MIT, BSD3 or Apache if you are corporate
    "License :: OSI Approved :: MIT License",

    # Specify the Python versions ensuring that you indicate you support Python 3.
    # this is only for PyPI and other metadata associated with your package - for your users to see
    "Programming Language :: Python :: 3 :: Only", # BE sure to specify that you use python 3.x
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]

# Optional, but suggested. You can decide whether you wish to pin or not pin dependencies. for most projects you want to avoid pinning dependencies
dependencies = ["ruamel-yaml>=0.17.21", "requests", "python-dotenv", "pydantic"]
# This is the metadata that pip reads to understand what versions your package supports
requires-python = ">=3.10"
readme = "README.md"
license = { text = "MIT" }

# Examples listed include a pattern for specifying where the package tracks
# issues, where the source is hosted, where to say thanks to the package
# maintainers, and where to support the project financially. The key is
# what's used to render the link text on PyPI.
[project.urls] # Optional
"Homepage" = "https://www.pyopensci.org"
"Bug Reports" = "https://github.com/pyopensci/pyosmeta/issues"
#"Funding" = ""
"Source" = "https://github.com/pyopensci/pyosmeta/issues"

# TODO: look into what hatch needs to recognize src/
# TODO: also look into how hatch vcs interacts
# TODO: look into how you define files that go into sdist with hatchling
# This config is important for telling pdm?? that the package should live in
# a src directory
#package-dir = "src"


# TODO: update this to work with hatchling
# [tool.pdm.version]
# # Note that you need to create the tag after all commits are created - otherwise
# # pdm adds dev info after the tag number which won't publish to PyPI
# source = "scm"
# write_to = "pyosmeta/_version_generated.py"
# write_template = "__version__ = 'v{}'"
```

## Example pyproject.toml file without comments

```toml
[build-system]
requires = <div></div>
build-backend = "hatchling.build"

[project]
name = "pyosmeta"
dynamic = ["version"]
description = "Tools that update the pyOpenSci contributor and review metadata that is posted on our website"
authors = [{ name = "Firstname lastname", email = "email@pyopensci.org" }]

maintainers = [
    { name = "firstname lastname", email = "admin@pyopensci.org" },
]

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3 :: Only", # BE sure to specify that you use python 3.x
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]

dependencies = ["ruamel-yaml>=0.17.21", "requests", "python-dotenv", "pydantic"]

requires-python = ">=3.10"
readme = "README.md"
license = { text = "MIT" }

[project.urls] # Optional
"Homepage" = "https://www.pyopensci.org"
"Bug Reports" = "https://github.com/pyopensci/pyosmeta/issues"
#"Funding" = ""
"Source" = "https://github.com/pyopensci/pyosmeta/issues"


# TODO: fix this to be hatchling focused
# [tool.pdm.version]
# source = "scm"
# write_to = "pyosmeta/_version_generated.py"
# write_template = "__version__ = 'v{}'"
```

### Advanced options

- **`[project.scripts]` (Entry points):** Entry points are optional. If you have a command line tool that runs a specific script hosted in your package, you may include an entry point to call that script directly at the command line (rather than at the python shell).
  - Here is an example of[ a package that has entry point script](https://github.com/pyOpenSci/update-web-metadata/blob/main/pyproject.toml#L60)s. Notice that there are several core scripts defined in that package that perform sets of tasks. pyOpenSci is using those scripts to process their metadata.
- **Dynamic Fields:** if you have fields that are dynamically populated. One example of this is if you are using scm / version control based version with tools like setuptooms_scm, then you might use the dynamic field. such as version (using scm) **dynamic = ["version"]**

### A few other notes

- The order of the sections of your pyproject.toml file doesn’t matter. What is important is that you have the correct subsections in each section. For example the build-system section should include your build requirements, but not your package classifiers which go in the project section of the pyproject toml.

## Activity: create your own pyproject.toml file

- Create your own file using the template above
- If you add it to your project, post a link to that pr / commit so others can see your file in the comments below.
