# -*- coding: utf-8 -*-
"""
Discrete-event simulator that can be used as a basis for most types of
discrete-event simulations. This version is an example that simulates a G/G/c
queuing system. The code is based on the lecture notes of the Stochastic
Simulation course from the Eindhoven University of Technology.

"""

from scipy import stats
from distribution import Distribution
from event import Event
from fes import FES
from simulation_results import SimResults


class Simulation:
    '''
    Simulates a GGc queuing system
    '''
    def __init__(self, arr_dist: object, serv_dist: object, nr_servers: int) -> None:
        '''
        Parameters
        ----------
        arr_dist : object
            Object of the Distribution class that contains that can be used to
            derive the distribution of the arrivals.
        serv_dist : object
            Object of the Distribution class that contains that can be used to
            derive the distribution of the serving time.
        nr_servers : int
            The number of servers that can process the arrivals.

        Returns
        -------
        None.

        '''
        self.arr_dist = arr_dist
        self.serv_dist = serv_dist
        self.nr_servers = nr_servers

    def simulate(self, sim_time: int) -> object:
        '''
        Parameters
        ----------
        sim_time : int
            total run time of the simulation.

        Returns
        -------
        object
            results object from the SimResults() class that can be used to
            extract meaningful results from the simulation such as queue lenght.

        '''
        queue = 0 # current number of customers
        time = 0 # current time
        #truck = Truck()
        results = SimResults()
        fes = FES()
        first_event = Event(Event.ARRIVAL, self.arr_dist.rvs())
        fes.add(first_event)
        while time < sim_time:
            print(queue)
            event = fes.next() # jump to next event
            time = event.time # update the time
            print(time)
            results.register_queue_length(time, queue) # register the queue length
            if event.type == Event.ARRIVAL : # if event is an arrival :
                queue += 1 # increase queue length
                if queue <= self.nr_servers : # there is an available server
                    dep = Event(Event.DEPARTURE, time + self.serv_dist.rvs())
                    fes.add(dep)
                arr = Event(Event.ARRIVAL, time + self.arr_dist.rvs())
                fes.add(arr) # schedule next arrival
            elif event.type == Event.DEPARTURE : # event is departure
                queue -= 1 # decrease queue length
                if queue >= self.nr_servers : # someone is waiting for service
                    dep = Event(Event.DEPARTURE, time + self.serv_dist.rvs())
                    fes.add(dep)
        return results

def main(sim_time: int) -> object:
    '''

    Parameters
    ----------
    sim_time : int
        total run time of the simulation.

    Returns
    -------
    object
        results object from the SimResults() class that can be used to
        extract meaningful results from the simulation such as queue lenght.

    '''

    arr_dist = Distribution(stats.expon(scale = 1/5.0)) # we expect 5 arrival p/h
    serv_dist = Distribution(stats.expon(scale = 1/1.0)) # we can process 1 arrival p/h per server

    # Intialize simulator
    sim = Simulation(arr_dist, serv_dist, nr_servers = 3)

    # Simulate for "sim_time" timesteps
    results = sim.simulate(sim_time = sim_time)

    return results

if __name__ == "__main__":
    SIM_TIME = 100
    res = main(sim_time = SIM_TIME)
