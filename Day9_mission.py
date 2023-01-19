#9.1
def good():
    return ["Harry", "Ron", "hermione"]

#9.2
cnts = 0

def get_odds():
    for i in range(10):
        if i % 2 == 1:
            yield i

odds = get_odds()
for j in odds:
    cnts += 1
    if cnts ==3:
        print(j)
