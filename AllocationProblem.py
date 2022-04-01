"""
This file defines an allocation problem class. Objects of this class will be the main input for our algorithm.

An allocation problem is a triplet made of
N - The set of agents in the allocation
M - The set of goods to be allocated
V - Vector of |N| valuations v_i such that v_i is the valuation function of agent i
"""


def validate_arguments(agents, goods, valuations):
    if type(agents) is not type(tuple) or type(goods) is not type(set) or type(valuations) is not type(tuple):
        raise TypeError("An allocation problem must consist of a tuple, a set and a tuple, respectively")
    if len(agents) != len(valuations):
        raise ValueError("Valuations vector size must be the same size as number of agents")
    if len(agents) == 0 or len(goods) == 0:
        raise ValueError("An allocation problem has at least one agent and at least one good")


class AllocationProblem:
    def __init__(self, agents: tuple, goods: set, valuations: tuple):
        validate_arguments(agents, goods, valuations)
        self.agents = agents
        self.goods = goods
        self.valuations = valuations

    def get_agents(self) -> tuple:
        return self.agents

    def get_goods(self) -> set:
        return self.goods

    def get_valuations(self) -> tuple:
        return self.valuations


__author__ = "Tal Zichlinsky and Alon Eshed"
