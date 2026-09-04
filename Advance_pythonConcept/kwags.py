def dic1(**kwargs):
    for item in kwargs.keys():
        print(f" {item} and value is {kwargs[item]}")
    
dic1(name='sachin', country='India')