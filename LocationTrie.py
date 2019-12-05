import pygtrie


class LocationTrie:
    __trie = pygtrie.CharTrie()

    def __init__(self):
        self.__trie.enable_sorting()

    def add_location(self, location):
        self.__trie[location] = True

    def delete_location(self, location):
        self.__trie.pop(location)

    def get_location_list(self, prefix):
        return self.__trie.keys(prefix)
