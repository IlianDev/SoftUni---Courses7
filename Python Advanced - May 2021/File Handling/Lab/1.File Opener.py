try:
    open("File.txt")
    print("File found")
except FileNotFoundError:
    print("File not found")
