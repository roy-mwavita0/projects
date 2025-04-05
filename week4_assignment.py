def read_and_modify_file():
    filename = input("Enter the name of the file to read: ")

    try:
        # Try opening the original file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Create a new filename
        new_filename = f"modified_{filename}"

        # Write modified content to new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read or write to the file.")

# Run the program
read_and_modify_file()
