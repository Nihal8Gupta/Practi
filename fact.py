#WAP to print factorial
def demo(i):
    if i==0:
        return 1
    return i*demo(i-1)
print(demo(1))