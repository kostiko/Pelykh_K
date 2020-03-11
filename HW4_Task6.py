def correct_tail(body, tail):
     sub = body[len(body)-len(tail)]
     if sub == tail:
        #print ("T")
        return True
     else:
        #print ("F")
        return False
correct_tail("Giraffe", "d")
correct_tail("Meerkat", "t")
