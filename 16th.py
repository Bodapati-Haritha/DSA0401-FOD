import string
from collections import Counter
def process_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    return text
def calculate_word_frequency(reviews):
    word_frequency = Counter()

    for review in reviews:
        processed_review = process_text(review)
        words = processed_review.split()
        word_frequency.update(words)
    return word_frequency
if __name__ == "__main__":
    customer_reviews = [
        "Loved the product",
        "Not satisfied with the quality.",
        "Poor Quality",
        "Amazing ambience"
    ]
    word_frequency = calculate_word_frequency(customer_reviews)
    print("Word Frequency Distribution:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")
