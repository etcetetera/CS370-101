# Introduction

## What is this repository?

This is a docker-based dev environment for CS370-101: Intro to Artificial Intelligence. It currently supports NVIDIA GPUs but with slight modifications it can target for x86 CPUs and Apple silicon chips. 

It currently includes the following tools:

* an empty library called `artagents` that includes code / logic imported across assignments and projects.
* a `project` directory for project source code. The documentation for the project is stored separately in the `docs` directory. 
* a `docs` directory that contains the source code of a [quarto](https://quarto.org/) based publishing system with markdown (qmd) and `ipynb` notebooks content. The docs folder is used to publish project work. 
* an empty CLI tool that should be based on `typer`, optionally used to implement a CLI for projects or assignments. 
* a `tests` directory containing `pytest` based tests for the `artagents` library and all other code.