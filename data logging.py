filepath='C:/Users/RANJANA/Desktop/sample.txt'
file=open(filepath,'a')
name=[]
degree=[]
for i in range(5):
    h=str(input('ur name'))
    j=str(input('ur degree'))
    name.append(h)
    degree.append(j)
    data=file.write(h)
    d1=file.write(j)
print('only 5 candidates are allowed thank you')
print(data)
print(d1)
file.close()
