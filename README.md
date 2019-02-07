# CDXJ Generator

A rudimentary Python 3 script to generate CDXJ TimeMaps for testing elsewhere. 

# Usage

To run:

    python3 cdxjGenerator.py [numberOfLines] > sample.cdxj

Nota bene, the resulting file should likely be sorted before used elsewhere. Do this via:

    sort sample.cdxj -o sample_sorted.cdxj

## Background
TimeMaps are lists that enumerate URIs of resources that encapsulate prior states of the given resource. ([RFC7089 - Memento](https://tools.ietf.org/html/rfc7089)). TimeMaps are often expressed in an extension of the Web Linking ([RFC5988](https://tools.ietf.org/html/rfc5988)) format. Additional, less common formats, like JSON and CDXJ TimeMaps can also express the same information in a less rigid format. [CDXJ](https://github.com/oduwsdl/ORS/wiki/CDXJ) is the most flexible of the three and is used by [InterPlanetary Wayback (ipwb)](https://github.com/oduwsdl/ipwb), which sparked the initial need for this software existing.
