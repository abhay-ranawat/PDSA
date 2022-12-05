def odd_one(l):
    dict_l = {}

    def add_dict(x, typeX):
        if typeX in dict_l.keys():
            dict_l[typeX] += 1
        else:
            dict_l[typeX] = 1

    for x in l:
        if type(x) == int:
            add_dict(x, 'int')
        if type(x) == float:
            add_dict(x, 'float')
        if type(x) == bool:
            add_dict(x, 'bool')
        if type(x) == str:
            add_dict(x, 'str')

    for key, value in dict_l.items():
        if value == 1:
            return (key)
