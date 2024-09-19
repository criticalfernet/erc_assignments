my_list=[
     {"first":"1"},
     {"second": "3"},
     {"third": "9"},
     {"four": "5"},
     {"five":"5"},
     {"six":"9"},
     {"seven":"6"}
    ]

def find_val(dict_list):
    values = set([])
    for dict_obj in dict_list:
        val = int(list(dict_obj.values())[0])
        values.add(val)
    print(list(values))

find_val(my_list)
