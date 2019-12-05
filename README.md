# Backend RESTful APIs for Location Autocomplete

## Development environment
python 3.6
* Flask version 1.1.1

## Initialization
1. modify config/database.json
2. ```python init.py```

## Features
Specification
* Given a term it needs to return a sorted list of best matching locations
* Given a location it needs to add it to the dictionary if it does not exist
* Given a location it needs to delete it from the dictionary if it exists
* Implement caching to quickly return the same response for a term seen previously
* Implement rate limit to avoid excessive queries
* Implement authentication mechanism to add/delete APIs
* Scripts to run this server in production

## Assumption and Tradeoff
I decided to not store the locations in Database nor filesystem, because there is "Runtime Efficiency" in the criteria
 but not "data persistence", so I assumed that it doesn't matter that the data will be gone if system restarts and the 
 performance is more important.