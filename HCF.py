n = int(input("Enter the number of numbers: "))
number_list = []
for _ in range(n):
    a = int(input())
    number_list.append(a)


number_list.sort(reverse=True)
total_set = set()
a = 1
while a <= number_list[0]:
    total_set.add(a)
    a += 1
factor_set = set()

for nums in number_list:
    factor_set = set()
    i = 1
    while i<= nums:
        if nums%i == 0:
            factor_set.add(i)
        i += 1
    total_set = total_set.intersection(factor_set)

new_factor_set = sorted(total_set, reverse=True)
total_set_list = list(new_factor_set)

print(total_set_list[0])