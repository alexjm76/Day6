animal = "fruitbat"


def print_global():
    print("inside print_global:", animal)


print("at the top level:", animal)
print(globals())

g=1

def print_global():
    global g
    print(g)
    g=2
    print(g)

print(g)
print_global()
