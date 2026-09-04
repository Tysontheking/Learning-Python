import argparse

parser = argparse.ArgumentParser(description="Simple Calculator")

parser.add_argument("option1", type=float, help="First Number")
parser.add_argument("option2", type=float, help="Second Number")
parser.add_argument("Opreactions", choices=["add","sub","mul","div"], help="Operation to perform")

args = parser.parse_args()
print(args)

if(args.Opreactions == "add"):
    print(f"Result is {args.option1 + args.option2}")
elif(args.Opreactions == "sub"):
    print(f"Result is {args.option1 - args.option2}")
elif(args.Opreactions == "mul"):
    print(f"Result is {args.option1 * args.option2}")
elif(args.Opreactions == "div"):
    print(f"Result is {args.option1 / args.option2}")
else:
    print("Error occured")