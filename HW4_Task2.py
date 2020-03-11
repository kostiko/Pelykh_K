def enough(cap, on, wait):
    if wait<=(cap-on):
        print('He can fit all {} passengers'.format(wait-(cap-on)))
        return 0
    else:
        print("""He can't fit {} out of {} waiting'""".format(wait-(cap-on),wait))
        return wait-(cap-on)
enough(100,60,50)


