#  No Duplicate Items ========================================================>>>>>>>>>>>>>>>>
a = set('fsjhdfhalhdf')
print(a) # {'h', 'l', 'a', 'j', 'f', 'd', 's'} unordered, unindexed.

b = set('abracadabra')

print(a - b)  # {'s', 'l', 'j', 'h', 'f'}                                   # letters in a but not in b
print(a | b)  # {'a', 's', 'c', 'j', 'l', 'r', 'd', 'h', 'b', 'f'}          # letters in either a or b
print(a & b)  # {'a', 'd'}                                                  # letters in both a and b
print(a ^ b)  # {'s', 'c', 'j', 'b', 'h', 'f', 'r', 'l'}                    # letters in a or b but not both
