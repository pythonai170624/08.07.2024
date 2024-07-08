pi: float = 3.14159;
print(f"Pi: {pi}");
print(f"Pi: {pi:.2f}");

name1:str = "Alice";
age1: int = 30;
#            12345678911
name2:str = "Laura Croft";
age2: int = 27;
print(f"Name: {name1} {age1}")
print(f"Name: {name2} {age2}")
print(f"Name: {name1:<11} {age1:>4}")
print(f"Name: {name1:<11} {age1:^5}")
print(f"Name: {name2:<11} {age2}")
prc: float = 0.5;
print(f"percentage: {prc:%}");