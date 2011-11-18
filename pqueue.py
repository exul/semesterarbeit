'''
Source: http://docs.python.org/release/3.1.3/library/heapq.html
'''

from itertools import *
from heapq import *

class PQueue:
    ''' 
    Priority queue to get the smallest element.
    '''
    def __init__(self):
        self._pq = []                         # the priority queue list
        self._counter = count(1)              # unique sequence count
        self._item_finder = {}                # mapping of item to entries
        self._INVALID = 0                     # mark an entry as deleted

    def add_item(self, priority, item, count=None):
        if not item in self._item_finder:
            if count is None:
                count = next(self._counter)
            entry = [priority, count, item]
            self._item_finder[item] = entry
            heappush(self._pq, entry)

    def get_top_priority(self):
        while True:
            priority, count, item = heappop(self._pq)
            del self._item_finder[item]
            if count is not self._INVALID:
                return item 

    @property
    def is_empty(self):
        return not self._pq
