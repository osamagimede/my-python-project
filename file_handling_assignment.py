def create_file():
    try:
        # Create a new text file named "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("Hello, this is line 1.\n")
            file.write("My name is Gloria Osamagimede Samuel\n")
            file.write("Python file handling is fun!\n")
    except Exception as e:
        print("Error:", e)
    finally:
        print("File creation process completed.")

def read_and_display():
    try:
        # Open "my_file.txt" in read mode ('r')
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            print("Contents of my_file.txt:")
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to access the file.")
    except Exception as e:
        print("Error:", e)
    finally:
        print("File reading process completed.")

def append_to_file():
    try:
        # Open "my_file.txt" in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the existing content
            file.write("Appending line 1.\n")
            file.write("Thanks to PLP academy for the Oppourtunity\n")
            file.write("Python file handling is awesome!\n")
    except Exception as e:
        print("Error:", e)
    finally:
        print("File appending process completed.")

if __name__ == "__main__":
    # Task 1: Create a new file with some initial content
    create_file()

    # Task 2: Read and display the contents of the file
    read_and_display()

    # Task 3: Append additional content to the file
    append_to_file()
