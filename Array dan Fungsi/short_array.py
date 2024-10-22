# set array
# Created by arsa
# 22-10-2024

print('\n')
print('='*30)
print('\tSet array')
print('='*30)

def data_array(arrayA, arrayB):
    return sorted(set(arrayA + arrayB))

data_a = [1,1,2,3,4,6,4,8,10,3,8,2,7,5,8,7,9,9,10]
data_b = [3,4,3,2,5,2,4,1,5,6,8,9,7,10,5,7,6,9,2,10]
c = data_array(data_a, data_b)
print(c)