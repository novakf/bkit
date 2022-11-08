def field(items, *args):
    assert len(args) > 0

    for item in items:
        d = {arg: item.get(arg) for arg in args if item.get(arg)}
        
        if len(d) == 0: 
            continue
        if len(args) == 1: 
            yield d[args[0]]
        else: 
            yield d
'''
goods = [
   {'title': 'Ковер', 'price': 2000, 'color': 'green'},
   {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

gen1 = field(goods, 'title')
gen2 = field(goods, 'title', 'price')

for i in gen1:
    print(i)    #должен выдавать 'Ковер', 'Диван для отдыха'
for i in gen2:
    print(i)    #должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}
'''