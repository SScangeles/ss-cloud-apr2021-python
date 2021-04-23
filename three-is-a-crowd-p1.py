
def isCrowded(party):
    if len(party) > 3:
        print("The party is crowded!")

def modList(party):
    while len(party) > 2:
            party.pop()

partyList = ['mina', 'jihyo', 'tzuyu', 'sana', 'momo', 'nayeon', 'chaeyoung', 'jeongyeon', 'dahyun']
isCrowded(partyList)
modList(partyList)
isCrowded(partyList)