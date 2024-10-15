def removeItem(tpl: tuple[int], value: int):
    if value in tpl:
        tplIsList = list(tpl)
        tplIsList.remove(value)
        return tuple(tplIsList)
    return tpl

test1 = tuple({1, 2, 3})
test2 = tuple({1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2})
test3 = tuple({2, 4, 6, 6, 4, 2})

res1 = removeItem(test1, 1)
print(res1, type(res1))

res2 = removeItem(test2, 3)
print(res2, type(res2))

res3 = removeItem(test3, 9)
print(res3, type(res3))