# -*- coding: utf-8 -*-
"""
The FES is a variable-sized array where events are added and removed.
These events are sorted by the time of occurrence.

"""

import heapq
from event import Event

class FES:
    '''
    The future event set (FES) keeps track of the scheduled events. Events can
    be added or removed and events are sorted in a heap structure (by the time)
    of occurence.

    '''
    def __init__ (self) -> None:
        self.events = []

    def add(self, event: Event) -> None:
        '''
        Add new events (arrivals or departures) to the FES

        Parameters
        ----------
        event : Event
            The event argument is an event object that contains information
            on the type and time of the event (arrival/departure)

        Returns
        -------
        None
            The heappush function is used to sort the heap of events

        '''
        heapq.heappush(self.events, event)

    def next(self) -> Event:
        '''
        Returns
        -------
        Event
            Returns the next event (the event with the closest next arrival
                                     time).

        '''
        return heapq.heappop(self.events)
