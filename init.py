from LocationTrie import LocationTrie
from flask_limiter import Limiter
from flask_caching import Cache
from flask_limiter.util import get_remote_address
import json


def init(app):
    trie = LocationTrie()
    with open('location-cnt.txt') as locations:
        for line in locations:
            location = line[line.find(' ') + 1: -1]
            trie.add_location(location)

    with open('config/config.json') as config_file:
        config = json.load(config_file)

    cache = Cache(config={'CACHE_TYPE': config['CACHE_TYPE']})
    cache.init_app(app)

    limiter = Limiter(app, get_remote_address, default_limits=["10000 per day", "1000 per hour"])

    keys = set(config['authorized_keys'])

    return trie, cache, limiter, keys
