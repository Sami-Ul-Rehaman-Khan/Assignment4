try:
    f = open('sample.txt','r')
    print("Line 1: ",f.readline())
    print("Line 2: ",f.readline())
except FileNotFoundError:
    print("The File 'sample.txt' not found")
