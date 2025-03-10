# a decision tree with interruptible branch evaluation
# that would be capable of optimizing a 2-operation program's result


import random

class Branch:
    def __init__(self, parent = None, opt = None, subopts = []):
        # each operation is a subtree, and has a metric

            # ok i'm thinking of having all children be a thing
            # but there is a situation where a node is unexpanded
            # let's still instantiate it though

        self._parent = parent
        self._opt = opt
        self._opts = subopts

        self._children = None 

        self._results = []

        # note: in a larger system, there could be more
        # - heuristics helping guide which option has most potential
            # - a quick-to-calculate guess as to the likely score
            # - bounds around a minimum or maximum score
        # - different kinds of score (speed, usefulness, reliability)
        # - changes in outer context stimulating need to re-evaluate options
        # - generally, shared or unique properties regarding different forms of evaluation, stimulating re-evaluation vs re-use of information
        # if properties are used the system can be generalized but represents an AI.

        # previous concept of "priority tree" likely has structure

        # we want to keep this simple to get somewhere

    def step(self):
        if self._children is None:
            self._children = [type(self)(opts=self._opts, parent=self, state=self._state) for 

