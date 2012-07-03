#Source: http://docs.python.org/release/3.1.3/library/heapq.html
from itertools import *
from heapq import *

class PQueue:
    ''' 
    Priority queue to get the smallest element.
    '''

    def __init__(self):
        ''' Initialize a priority queue '''
        self._pq = []                         # the priority queue list
        self._counter = count(1)              # unique sequence count
        self._item_finder = {}                # mapping of item to entries
        self._INVALID = 0                     # mark an entry as deleted

    def add_item(self, priority, item, count=None):
        '''
        Add an item with a given priority to the priority queue. It item can be
        in the queue only once.

        @type   priority: number
        @param  priority: Priority of the item.

        @type   item: item
        @param  item: Item that should be added to the priority queue.
        '''
        if not item in self._item_finder:
            if count is None:
                count = next(self._counter)
            entry = [priority, count, item]
            self._item_finder[item] = entry
            heappush(self._pq, entry)

    def get_top_priority(self):
        '''
        Get the item on the top of the priority queue.

        @rtype: item
        @return: The item on the top of the priority queue.
        '''
        while True:
            priority, count, item = heappop(self._pq)
            del self._item_finder[item]
            if count is not self._INVALID:
                return item 

    @property
    def is_empty(self):
        '''
        Returns if the priority queue is empty

        @rtype: boolean
        @return: Truth-value for emptyness of the priority queue.
        '''
        return not self._pq
