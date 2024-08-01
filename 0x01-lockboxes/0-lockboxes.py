def canUnlockAll(boxes):
    keys = set()
    for i, box in enumerate(boxes):
        if box == []:
            keys.add(0)
        for key in box:
            if key < len(boxes) and key != i:
                keys.add(key)

    return len(keys) == len(boxes)
