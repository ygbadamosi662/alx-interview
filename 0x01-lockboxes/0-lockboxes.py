#!/usr/bin/python3
"""
    Defines the canUnlockAll function
"""
import sys


def canUnlockAll(boxes):
    """
        Represents canUnlockAll for boxes

        Args:
            boxes (_type_): list
        Returns:
            boolean
    """
    sys.setrecursionlimit(1000000)  # SET RECURSION LIMIT NUMBER.
    lock_status = [False] * len(boxes)

    def unlock_boxes(boxes, index):
        """
        This function unlock boxes recursively if boxes is a list of box

        Args:
            boxes (list[list])
            index (integer)
        Returns:
            list[boolean]
        """
        try:
            if not lock_status[index]:
                lock_status[index] = True
            else:
                return

            keys = boxes[index]
            if not keys:
                return

            for key in keys:
                unlock_boxes(boxes, key)
        except IndexError:
            return

    unlock_boxes(boxes, 0)
    return all(lock_status)
