

def check_empty_dict(lst):

    lst1 = []
    for i in range(len(lst)):
        if lst[i]:
            lst1.append(None)
    if lst1:
        return False
    else:
        return True

def test(lst):
    print('checking list: ',lst)
    print(check_empty_dict(lst))
    

test([{}, {}])


test([{1:2}, {}, {}])

        