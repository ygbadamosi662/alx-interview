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
    def unlock_boxes(unlocked_box, boxes, already_unlocked=None):
        """
        This function unlock boxes recursively if boxes is a list of box
        provide one unlocked box in the list as unlocked_box
        Returns a list of unlocked_boxes including unlocked_box

        Args:
            unlocked_box (list)
            boxes (list[list])
            already_unlockedlist[list]: default = None
        Returns:
            list[list]
        """
        if already_unlocked is None:
            already_unlocked = [unlocked_box]
        unlocked_here = []

        for val in unlocked_box:
            if (val < len(boxes)) and (boxes[val] not in already_unlocked):
                unlocked_here.append(boxes[val])
                already_unlocked.append(boxes[val])

        if unlocked_here == []:
            return already_unlocked

        for keys in unlocked_here:
            unlock_boxes(keys, boxes, already_unlocked)

        return already_unlocked

    if len(unlock_boxes(boxes[0], boxes)) == len(boxes):
        return True

    return False
