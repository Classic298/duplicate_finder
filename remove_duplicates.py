"""This script takes a file name as a command-line argument and uses a dictionary to keep track of
the lines that have been seen. If a line is already in the dictionary, it is added to a list of
duplicates. Finally, the script prints out the list of duplicates, opens the file for writing, and
writes the non-duplicate lines to the file, effectively deleting the duplicate lines."""
import sys

def find_duplicates(file_name):
    # Create an empty dictionary
    lines_seen = {}
    duplicates = []
    new_lines = []

    # Open the file
    with open(file_name, "r") as f:
        # Iterate over each line
        for line in f:
            # Strip leading and trailing white space
            line = line.strip()
            # If the line is already in the dictionary, add it to the list of duplicates
            if line in lines_seen:
                duplicates.append(line)
            else:
                # Add the line to the dictionary
                lines_seen[line] = 1
                new_lines.append(line)

    # Print the list of duplicates
    for duplicate in duplicates:
        print(f"Duplicate: {duplicate}")

    #Open the file for writing
    with open(file_name, "w") as f:
        for line in new_lines:
            f.write(line + '\n')
    print(f"Duplicates removed and written back to {file_name}")

# Main function
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_name>")
        sys.exit()
    file_name = sys.argv[1]
    find_duplicates(file_name)
