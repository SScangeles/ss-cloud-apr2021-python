
def isCrowded(party):
    if len(party) > 3:
        print("The party is crowded!")
    else:
        print("Party list is not crowded.")

def modList(party):
    while len(partyList) > 2:
            partyList.pop()

partyList = ['mina', 'jihyo', 'tzuyu', 'sana', 'momo', 'nayeon', 'chaeyoung', 'jeongyeon', 'dahyun']
isCrowded(partyList)
modList(partyList)
isCrowded(partyList)