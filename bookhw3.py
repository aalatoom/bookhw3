import string

def count_unique_words(Romeo_and_Juliet):
    # Reads a text file and counts unique words
    try:
        with open(Romeo_and_Juliet, "r", encoding="utf-8") as file:
            text = file.read().lower()  # Convert to lowercase
            text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
            words = set(text.split())  # Convert to a set to get unique words
            return len(words)
    except FileNotFoundError:
        print(f"Error: {Romeo_and_Juliet} not found.")
        return 0

# File names for the books (update with actual file paths)
book1 = "Romeo_and_Juliet"
book2 = "Alice's_Adventures_in_Wonderland"

# Count unique words
unique_words_book1 = count_unique_words(book1)
unique_words_book2 = count_unique_words(book2)

# Display results
print(f"Unique words in {book1}: {unique_words_book1}")
print(f"Unique words in {book2}: {unique_words_book2}")

# Compare unique word counts
if unique_words_book1 > unique_words_book2:
    print(f"{book1} has more unique words.")
elif unique_words_book1 < unique_words_book2:
    print(f"{book2} has more unique words.")
else:
    print("Both books have the same number of unique words.")