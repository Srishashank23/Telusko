# Dictionary
# 1
data = {1: 'Abhi' ,2: 'Shivam' ,3: 'Naveen' ,4: 'Dev'}
print(data)
print(data[4])
print(data.get(1))
print(data.get(5,'Not Found'))

# 2
names = ['Abhi', 'Naveen', 'Shivam', 'Dev']
number = [2, 4, 6, 8]
data = dict(zip(number,names))
print(data)
print(data[2])
data[18] = 'Ved'
print(data)
del data[4]
print(data)