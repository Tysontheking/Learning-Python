filter1 = [12,23,20,45,67,89,90,100]

def filter_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
final_Filter = list(filter(filter_even, filter1))
Greater_20_filter = list(filter(lambda x: x>20, filter1))
start_with_1 = list(filter(lambda x: str(x).startswith('1'),filter1))

print(start_with_1)

print(final_Filter)
print(Greater_20_filter)