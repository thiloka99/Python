def count_substring(string, substring):
    count = 0
    sub_len = len(substring)
    
    # Iterate through the string
    for i in range(len(string) - sub_len + 1):
        # Check if the substring matches the current slice of the string
        if string[i:i+sub_len] == substring:
            count += 1
    
    return count


if __name__ == '__main__':
    string = input()  # Read the original string
    substring = input()  # Read the substring
    result = count_substring(string, substring)  # Call the count_substring function
    print(result)  # Print the number of occurrences
