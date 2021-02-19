# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
mydict = {}
for i in range(n):
    name, number = input().split()
    mydict[name] = number
while True:
    try:
        guess = input()
        if guess in mydict:
            print(guess + "=" + mydict[guess])
        else:
            print("Not found")
    except:
        break
