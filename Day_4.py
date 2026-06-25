n = 10 
for i in range(n):
    print("Hello world", i + 1)
#O(1)


n = 10 
for i in range(n):
    for j in range (n):
        print(i, j)

    for j in range (n):
        print(i, k)
#O(n^2)

