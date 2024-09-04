def AND(a,b):
    if a == 1 and b == 1:
        return True
    else:
        return False
    
print(AND(1,1))

def OR(a,b):
    if a == 1 or b == 1:
        return True
    else:
        return False
    
print(OR(1,1))


def NOT(a):
    return not a

print(NOT(1))