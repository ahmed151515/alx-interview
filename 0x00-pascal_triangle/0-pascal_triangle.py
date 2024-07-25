#!/usr/bin/python3

def pascal_triangle(n):
    if n < 1:
        return []
    res = [[1]]

    for i in range(1, n):
        cur = [1]
        for j in range(1, len(res[i - 1])):
            num = res[i-1][j - 1] + res[i-1][j]
            cur.append(num)
        cur.append(1)

        res.append(cur)

    return res
