

# Write a function that counts the number of lines in a txt file

def countlines(filename: str) -> int:
    """
    Counts the number of lines in a file
    this includes any spaces
    """
    with open(filename, "r") as f:
        text = f.read().splitlines()
    return len(text)

print(countlines("Day_19-Modules/obama_speech.txt"))