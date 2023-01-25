import sys

def find_duplicates(file_name):
    # Create an empty dictionary
    lines_seen = {}
    duplicates = []

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

    # Print the list of duplicates
    for duplicate in duplicates:
        print(duplicate)

# Main function
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_name>")
        sys.exit()
    file_name = sys.argv[1]
    find_duplicates(file_name)
