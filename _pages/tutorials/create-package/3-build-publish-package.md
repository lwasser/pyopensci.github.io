---
layout: single
permalink: /python-package-tutorial/build-publish-pypi.html
classes: wide
title: "Build your Python package"
excerpt: "More here"
header:
  overlay_color: "#666"
  overlay_filter: 0.6
author_profile: false
---

{% include packaging-toc %}

# TODO: add either step in the make installable package lesson or a new lesson that just has the user create a license, readme file, contributing & CODE_of_CONDUCt.md file.

<div class="notice" markdown="1">
## Learning Objectives

In this lesson you will learn:

1. sdf

</div>

# What is building (link to guide)

# What tools do you need to build ?

- use pip to install locally - when you use pip it actually does create a wheel...
- we are using pypa build which will create the proper distribution archives that pypi requires
- we are using hatchling which is a build-backend (other backends include... setuptools, pdm-build, flit.core, meson-python etc... )
- you will use twine to publish your package on PyPI

## Building a distribution

```python
# build your distro using pypa's build tool
`python -m build`
```

look at the output

extras
wheel is just a .zip file - you can unzip it and look inside (in guide covered??)

sdist is the flat files - you can unzip the tar.gz to see those...

- specify what doesn't go in sdist???

## Publish to pypi (could be it's own lesson)

- first time will need to be manual - will need a unique name
- setup user account on test pypi
- build distribution locally
- use twine to publish to pypi ...

In this lesson you will learn how to publish to test-pypi. the steps for publishing to pypi will be the same but we will demonstrate test-pypi first.

In doing this you will see how the metadata in your pyproject toml helps pypi understand ...

and helps users find your package.

it might be nice to setup

https://test.pypi.org/manage/account/publishing/ it seems easier than secrets and such.

then w e can use pdm publish

https://test.pypi.org/manage/account/publishing/

https://docs.pypi.org/trusted-publishers/adding-a-publisher/
