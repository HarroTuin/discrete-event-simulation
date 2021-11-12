# -*- coding: utf-8 -*-
"""
The SimResults class is used to keep track of the results.
In this simulation we are interested in the mean queue length and the queue
length probabilities.

"""
import numpy as np

class SimResults:

    MAX_QL = 10000

    def __init__(self):
        self.sum_ql = 0
        self.old_time = 0
        self.queue_length_histogram = np.zeros(self.MAX_QL+1)

    def register_queue_length(self, time, ql):
        self.sum_ql += ql*(time - self.old_time)
        self.queue_length_histogram[min(ql, self.MAX_QL)] += (time - self.old_time)
        self.old_time = time

    def get_mean_queue_length(self):
        return self.sum_ql/self.old_time

    def get_queue_length_probabilities(self):
        return [x/self.old_time for x in self.queue_length_histogram]
