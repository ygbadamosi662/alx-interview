#!/usr/bin/python3
"""
    Defines the canUnlockAll function
"""


def canUnlockAll(boxes):
    """
        Represents canUnlockAll for boxes

        Args:
            boxes (_type_): list
        Returns:
            boolean
    """
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
        if (not lock_status[index]) and (index < len(boxes)):
            lock_status[index] = True
        else:
            return

        keys = boxes[index]

        if not keys:
            return

        for key in keys:
            unlock_boxes(boxes, key)

    unlock_boxes(boxes, 0)
    return all(lock_status)
