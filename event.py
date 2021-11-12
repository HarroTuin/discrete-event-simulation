# -*- coding: utf-8 -*-
"""

Event class:
    An event occurs whenever the state of the system (e.g. the queue length)
    changes. The Event class creates a new event for the Future Event Set.
    Note that the Event class contains a function __lt__. This is a standard
    Python function used to compare objects to another (’lt’ stands for “less
    than”), to determine the order in which they should be sorted.

"""

class Event:
    '''
    The Event class is used to create new events for the simulation
    '''
    ARRIVAL = 0 # constant for arrival type
    DEPARTURE = 1 # constant for departure type

    def __init__(self, type_ : int, time: float) -> None:
        '''
        Parameters
        ----------
        type_ : int
            Type of arrival (arrival or departure), underscore is used because
            type is a reserved namespace
        time : float
            The time the event is taking place.

        Returns
        -------
        None

        '''
        self.type = type_
        self.time = time

    def __lt__(self, other):
        return self.time < other.time
