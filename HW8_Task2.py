def sorter(textbooks):
    return sorted(textbooks,key=str.casefold)

print(sorter(['Algebra', 'History', 'Geometry', 'English']))