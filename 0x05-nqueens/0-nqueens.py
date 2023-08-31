#!/usr/bin/python3
"""
    Defines class NQueens
"""
import sys


# Handle conditions
try:
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        exit(1)

    n = int(args[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

except ValueError:
    print("N must be a number")
    exit(1)


class NQueens:
    """
        Solve NQueens:
        This returns the number of queens that can be present
        in a nxn chess board with them attacking one another.
    """
    def __init__(self, n):
        """ initialize the varaible """
        self.num = n
        self.solution = []
        self.state = []

    def is_valid_state(self, state, n):
        """
            check if the state is up to the

        Args:
            state (List): various level queen is present
            n (int): the nxn board

        Returns:
            bool: _description_
        """
        return len(state) == n

    def get_candidates(self, state, n):
        """
            Get the next level to continue with

        Args:
            state (List): various level queen is present.
            n (int): the nxn board

        Returns:
            Union[Set, Type] : the available position
        """
        if not state:
            """ if no queen is added yet return a range """
            return range(n)

        position = len(state)  # the position to insert the queen
        candidates = set(range(n))  # columns
        for row, col in enumerate(state):
            candidates.discard(col[1])  # remove col
            # remove diagonals
            n_level = position - row
            candidates.discard(col[1] + n_level)  # discard left diagonal
            candidates.discard(col[1] - n_level)  # discard right diagonal

        return candidates

    def search(self, solution, state):
        """
            search and add the state to solution if the conditions are met
        Args:
            solution (List): list or lists of valid entries
            state (List): various level queen is present.
        """
        if self.is_valid_state(self.state, self.num):
            self.solution.append(self.state.copy())
            return

        for candidate in self.get_candidates(self.state, self.num):
            index = len(self.state)
            self.state.append([index, candidate])
            self.search(self.solution, self.state)
            # remove the recently added data for backtracking
            self.state.pop()

    def result(self):
        """ return the solution"""
        self.search(self.solution, self.state)
        return self.solution


if __name__ == "__main__":
    queens = NQueens(n)
    for result in queens.result():
        print(result)
