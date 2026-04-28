#INVERTED PYRAMID

def inverted_pyramid(n):
    for i in range(n):
        print(""*i,end="")

        print("*"*(2*n-2*i-1))

    inverted_pyramid(5)