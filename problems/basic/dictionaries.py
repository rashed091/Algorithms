from collections import defaultdict
from collections import OrderedDict


pairs = {('a', 1), ('b', 2), ('c', 3)}

d1 = {}

for key, value in pairs:
    if key not in d1:
        d1[key] = []
    d1[key].append(value)
print(d1)


d2 = defaultdict(list)

for key, value in pairs:
    d2[key].append(value)

d2['a'].append(5)

print(d2)


d3 = OrderedDict(pairs)

for key in d3.keys():
    print(key, d3[key])