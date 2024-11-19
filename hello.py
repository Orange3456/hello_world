import sys
if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    print("You are expected to provide your name.")
    print("You need to type:")
    print(f"\t python {sys.argv[0]} your_name")
    sys.exit()
print(f"My name is {name}.")
print()

print("Hello world!")
print("\t This is my first git repository on github.")