data =[]

print("Enter 5 numbers:")

for i in range(5):
    data.append(int(input()))

max_val =max(data)
min_val =min(data)
data_range = f"{min_val}-{max_val}"
sum_val = sum(data)

print("Max :",max_val)
print("Min :",min_val)
print("Range :",data_range)
print("Sum is :",sum_val)
