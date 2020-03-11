def make_move(sticks):
    if sticks==21:
        return 1
    return sticks-4*(sticks//4)

print(make_move(5))