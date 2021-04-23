
def isCrowded(party):
    partySize = len(party)
    if partySize > 5:
        print("There is a mob in the party!")
    elif partySize >= 3 and partySize <= 5:
        print("The party is crowded.")
    elif partySize >= 1 and partySize <= 2: 
        print("The party is not crowded.")
    else:
        print("The party is empty.")

def modList(party):
    while len(party) > 0:
            party.pop()

partyList = ['mina', 'jihyo', 'tzuyu', 'sana', 'momo', 'nayeon', 'chaeyoung', 'jeongyeon', 'dahyun']
isCrowded(partyList)