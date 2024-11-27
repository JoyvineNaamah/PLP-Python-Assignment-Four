try:
    with open("myData.txt", "r") as file:
        data = file.read()
        print("File read successfully.")
except FileNotFoundError:
    print("Error: File not found. Please check the filename.")
except IOError:
    print("Error: Unable to read the file.")
    