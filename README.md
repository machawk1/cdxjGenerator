# CDXJ Generator

A rudimentary Python 3 script to generate CDXJ TimeMaps for testing elsewhere. 

## Usage

To run, call the script:

    python cdxjGenerator.py [number of lines] [URI-R]
    
For example:

    python cdxjGenerator.py 12
    
...will generate CDXJ output (to stdout by default) consisting of entries for 12 random URIs. Alternatively:

    python cdxjGenerator.py 25000 memento.us
    
...will generate 25,000 entries for the URI-R `memento.us`. This output can be written to a file like:

    python cdxjGenerator.py 25000 memento.us > sample.cdxj

The resulting file will likely need to be sorted before used elsewhere. Do this via:

    LC_ALL=C sort sample.cdxj > sample_sorted.cdxj

This can also be performed in a single command, instead of writing to the temporary, unsorted `sample.cdxj` like:

    python cdxjGenerator.py 25000 memento.us | LC_ALL=C sort > sample_sorted.cdxj

## Background
TimeMaps are lists that enumerate URIs of resources that encapsulate prior states of the given resource. ([RFC7089 - Memento](https://tools.ietf.org/html/rfc7089)). TimeMaps are often expressed in an extension of the Web Linking ([RFC5988](https://tools.ietf.org/html/rfc5988)) format. Additional, less common formats, like JSON and CDXJ TimeMaps can also express the same information in a less rigid format. [CDXJ](https://github.com/oduwsdl/ORS/wiki/CDXJ) is the most flexible of the three and is used by [InterPlanetary Wayback (ipwb)](https://github.com/oduwsdl/ipwb), which sparked the initial need for this software existing.

## A Note
This tool uses the Faker module to generate valid dates. Some Python environments don't like this. Generate a fresh one using `python3 -m venv test_venv` rather than the typical syntax to remedy the issue.
