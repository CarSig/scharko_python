
# To handle files in Python, you can use the built-in open() function, which allows you to open files in different modes (such as read mode, write mode, or append mode) and perform various operations on them. Here's how you can read the contents of a file named "example.txt" located in the same folder as your Python script:


# Open the file in read mode
# with open("example.txt", "r") as file:
#     # Read the contents of the file
#     contents = file.read()
#     # Print the contents to the console
#     print(contents)


# We use the open() function to open the file named "example.txt" in read mode ("r").
# We use the with statement to ensure that the file is properly closed after reading its contents. This is a recommended practice as it automatically closes the file when the block of code inside it exits.
# We use the read() method to read the entire contents of the file into a string variable named contents.
# Finally, we print the contents of the file to the console.
# You can also use other modes with the open() function depending on the operation you want to perform:

# "w": Write mode (creates a new file or overwrites an existing file).
# "a": Append mode (appends data to the end of the file).
# "r+": Read and write mode (allows you to read and write to the file).
# "b": Binary mode (for working with binary files).

def file_handling():
    # Opening a file
    file = open("example.txt", "r")
    # Reading a file
    content = file.read()
    # Writing to a file
    text = input("Enter some text: ")
    file = open("example.txt", "w")
    file.write(text)
    # Closing a file
    file.close()

file_handling()    