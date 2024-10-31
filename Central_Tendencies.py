import pandas as pd

mean,median,mode=0,0,0
d={}

data = pd.read_csv('Data\Central_Tendencies.csv')

values = data['Values'].tolist()

print(values)
values.sort()
if len(values) % 2 == 0:
    median = (values[len(values)//2]+values[len(values)//2+1])//2
else:
    median = values[len(values)//2]

for val in values:
    mean += val
mean = mean/(len(values))

for val in values:
    if val not in d.keys():
        d[val]=1
    else:
        d[val]+=1

temp=0

for key,value in d.items():
    if value>temp:
        temp=value
        mode=key


print("Central Tendencies: ")
print(f"Mean: {mean}")
print(f"Median: {median}")
print("Mode:" , end=" " )
for key,value in d.items():
    if value == temp:
        print(key, end=", ")
print()

