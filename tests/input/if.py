def test(msgtype, flags):
    if flags == 1:
        msgtype = 1
    elif flags == 2:
        msgtype = 2
    elif flags == 3:
        msgtype = 3
    return msgtype

def test2():
    item = None
    if item is None:
        item = 'item is none'
    if item is not None:
        item = 'item is not none'
    if item == 1:
        item ='item equals 1'
    if not ( item == 1 or item == 2):
        item = 'item not equals 1 or 2'
