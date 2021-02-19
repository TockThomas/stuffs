# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for i in range(t):
    word = input()
    odd = ""
    even = ""
    for j in range(len(word)):
        if 0 != j % 2:
            odd = odd + word[j]
        elif 0 == j % 2:
            even = even + word[j]
    print(even + " " + odd)