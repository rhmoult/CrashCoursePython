million = list([i for i in range(1, 1000001)])

print(f"The first three items in the list are: {million[:3]}")
print(f"Three items in the middle of the list are: {million[499_998:500_001]}")
print(f"The last three items in the list are: {million[-3:]}")