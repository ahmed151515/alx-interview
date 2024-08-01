"""_summary_
"""


def canUnlockAll(boxes):
    """_summary_

    Args:
        boxes (_type_): _description_

    Returns:
        _type_: _description_
    """
    keys = set()
    for i, box in enumerate(boxes):
        if box == []:
            keys.add(0)
        for key in box:
            if key < len(boxes) and key != i:
                keys.add(key)

    return len(keys) == len(boxes)
