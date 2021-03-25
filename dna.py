n1 = input()
n2 = input()
n3 = input()

if len(n1) <= len(n2) and len(n1) <= len(n3):
    print(f"{n1} {len(n1)}")
elif len(n2) < len(n3):
    print(f"{n2} {len(n2)}")
else:
    print(f"{n3} {len(n3)}")