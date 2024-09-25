Personal Project - INVERSE ACRONYM
============================
A simple project to make inverse acronyms


Table Of Contents
----------------------------
+ [General info](#general-info)
+ [Technologies](#technologies)
+ [Setup](#setup)

## General info
This project lets the user pull category lists from wikitionary and use them to search for inverse acronyms
For example:
- searching for *bv* in *English_idioms* categoty would return:
- 1 - bird's-eye view
- 2 - broken vessel

## Technologies
* Python version: 3.12


## Setup
You need at least python 3.12 installed.
+ Install poetry
```
$ pip install poetry
```
+ Run ```poetry install``` inside root folder
```
$ poetry install 
```
+ And finally to run
```
$ poetry run python3 inverse-acronym/main.py
```
