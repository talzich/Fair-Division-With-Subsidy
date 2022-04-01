"""
This file defines an agent class.

An agent has an ID, valuation function
"""
import itertools


class Agent:
    newid = itertools.count().next

    def __init__(self, value_func: callable):
        self.id = Agent.newid()
