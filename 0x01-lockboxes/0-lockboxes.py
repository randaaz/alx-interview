#!/usr/bin/python3

""" This module provides a function to determine
if all lockboxes can be opened. """


def canUnlockAll(boxes):
    """
    - Determines if all lockboxes can be opened.
    - boxes (list): A list of lists representing
    - lockboxes and their corresponding keys.
    - You can assume all keys will be positive integers
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, False otherwise.
    """
    canUnlockAll = False
    keys = {0: True}
    n_boxes = len(boxes)
    while(True):

        n_keys = len(keys)

        for i in range(len(boxes)):
            if boxes[i] and keys.get(i, False):
                for j in boxes[i]:
                    if j < n_boxes:
                        keys[j] = True
                    boxes[i] = None

        if not(len(keys) > n_keys):
            break

    if n_keys == len(boxes):
        canUnlockAll = True

    return canUnlockAll
