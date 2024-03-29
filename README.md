# Backend APIs for Location Autocomplete

## Development environment
* python 3.6
* pip3
* Flask version 1.1.1

## Initialization
### By script (not recommended)
1. modify config/config.json
2. ```python run.py```

### By Docker (recommended)
1. ```docker build -t location-autocomplete .```
2. ```docker run -p YourPort:5000 location-autocomplete```

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

## Sample request
* post /add/ {"location": "beiiiii", "key":"123456"}
* post /delete/ {"location": "beiiiii", "key":"123456"}
* get /query/?term=bei
