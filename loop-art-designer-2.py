print("-----FLOYD's-TRIANGLE-----")
num = 1
rows = 7
for i in range(1,7):
    for j in range(i):
        print(f"{num} ", end="")
        num += 1
    print()
