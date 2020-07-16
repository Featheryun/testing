def str_to_dict(s):
    a = s.split('，')
    b = list()
    c = list()
    for i in a:
        b.append(i.split('：')[0])
        c.append(i.split('：')[1])
    e = dict(zip(b, c))
    return e