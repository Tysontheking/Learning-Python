def sum_all(*args):
    total = 0
    for i in args:
        total += i
    return total
        

num = sum_all(12,2,3)
# print(num)

def print_details(**kwargs):
    for item in kwargs.keys():
        print(f" {item} : {kwargs[item]}")

print_details(name="Alice", age=25, city="Delhi")