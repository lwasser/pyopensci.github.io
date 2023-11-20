---
layout: single
permalink: /tutorials/about-python-packages.html
classes: wide
title: "What is a Python package?"
excerpt: "More here"
header:
  overlay_color: "#666"
  overlay_filter: 0.6
author_profile: false
---

# TODO - this might go directly into the packaging guide

then the first lesson can be lesson 0 - setup a dev envt

{% include packaging-toc %}

<div class="notice" markdown="1">
## Learning objectives

After reading this lesson you will:

- Understand what a Python package is
- Be able to list the 5 core components of a python package
- You will be able to explain the difference between generalizable code and code that supports a specific scientific application

</div>

## What is a Python package?

A Python package is a collection of related modules / code containing functions, classes and methods that are organized together in a directory. Packages allow you to group and structure your Python code, making it easier to manage and reuse code across different projects.

Ideally the code in a published Python package is generalizable. This means it can be applied in different settings.

An example of a package that has a generalized scope is matplotlib. It does one (big important) thing really well:

It creates visual plots of data.

Matplotlib is used by thousands of users for a host of different plotting applications. While few scientific packages will have the same broad application as tools like matplotlib or numpy, the
idea of code being used for something more than a single workflow still applies.

<figure>
    <a href="/images/python-packages/python-package-schematic.png"><img src="/images/python-packages/python-package-schematic.png" alt="ADD ALT"></a>
    <figcaption>Caption here</figcaption>
</figure>

A Python package can be installed into a Python environment. This allows you to access it from any code run with that specific Python environment activated.

## Why create a package?

There are numerous reasons why you might create a Python package:

- **Use your code across multiple projects:** At its most basic level, creating a package allows you to install your code into a Python environment. This allows you to then import functions and classes into any workflows both locally and in the cloud..
- **Share your code:** Sharing your code with others is often a common reason to create a package.If you publish a package on a public repository such as PyPI or conda, immediately your package can be installed on any machine using pip or conda with a single command.
- **Build community around your code:** Packages make it easier for multiple people to work on the same project (particularly when published on Github). A version platform such as git (the version control system used by GitHub), further makes it easier to track changes to the codebase over time. Tools such as issues and pull requests make it easier for outside users to contribute bug fixes and to establish review processes for accepting changes to the code base..
- **Organize your code:** Packages can be used to organize large code projects, dividing them into smaller, more manageable components. This structure can help with both maintaining the codebase and with making it easier to understand.

## What to consider before you create a package

Creating a python package that others use takes considerable time and effort. Before you begin, think about your goals including:

- Who you think will use your package
- Whether you have time to add things such as documentation and tests
- How long you might be able to maintain it

### The elements of a Python package

A package in any language is more than just code. If your package is public facing, meaning people besides yourself will use it, you will want to think about the various elements of a package that make it a useful community resource.

Most python packages live in an online version control platform such as GitHub or GitLab. These platforms support robust infrastructure including continuous integration and continuous deployment (CI/CD).

<figure>
    <a href="/images/python-packages/packaging-workflow.png"><img src="/images/python-packages/packaging-workflow.png" alt="ADD ALT"></a>
    <figcaption>Caption here</figcaption>
</figure>

The core elements of Python package include:

- **Code:** Generalized code that performs operations that you may need to complete multiple times
- **Documentation:** documentation with tutorials / examples that help users get started using your tool
  - Documentation also helps people to contribute to your package.
- **Tests:** that makes sure your code works as it should and makes it easier for you and others to contribute to, modify and update the code in the future
- **License:** An open source license …. - link to choose a license…
- **Infrastructure** that automates updates, publication workflows and runs test suites

If you intend for others to use and contribute to your code, consider who will maintain it over time. You will want a **contributing / development** guide to help new potential contributors get started with contributing to your package. And a **code of conduct** to ensure community interactions remain healthy both for you and your contributors / maintainer team

_Link to our EiC checklist for core components that pyOpenSci looks for… _

## Yay, your package has users! Now what?

As the community using your package grows, you may also find yourself managing users, contributors and others who want to interact with your package. It’s important to consider all this before you dive into development. Once you have a user base in the community, people will depend upon your code to work and will need direction regarding how to use it.

## Development guidelines

_TODO: I suspect nick murphy has something in this space that we can rif off of. Essentially I'm thinking here we have a SHORT section on development best practices and then link to another resource (be it on the pyos website or elsewhere). This would include things like:_

- _Defining the scope of your package and scope creep_
- _Keeping functions focused on doing a single thing well._
- _Broad generalizable get started guidelines and then we can link to more in depth resources in this space._

## Research compendia

Goal: The goal of this section is really to distinguish a public facing package from a more specific set of scripts and even a package that is intended to support a single workflow / paper/ etc. it likely needs a better heading as this term research compendia is a specific term that not everyone will know.

On the other hand, if your code is intended to be used for a specific purpose such as supporting an open reproducible science workflow and subsequent publication, it may have a more specific application. In this case you might create a package for your own use or your lab’s use. However this package may be less useful to others in the community other than when trying to reproduce your results. In this case having documentation and getting started guides is important. However you may not need as much robust infrastructure around your package given you don’t intend to maintain it after publication or for others to maintain it over time.

## What's next?

In future lessons we will talk more about the infrastructure around a published python package that makes it both easier to maintain, easier for others to contribute to and easier for other scientists to use. However, first we want to get you to your initial goal of publishing a python package.

In this next lesson you will learn how to create a basic installable Python package.
