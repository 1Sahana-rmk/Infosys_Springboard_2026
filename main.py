# Infosys_Springboard_2026
# main.py

from sentiment_dictionary import word_scores
from file_handler import read_reviews, write_results


def calculate_score(sentence):
    sentence = sentence.lower()
    words = sentence.split()

    score = 0

    for word in words:
        if word in word_scores:
            score += word_scores[word]

    return score


def process_reviews():
    reviews = read_reviews("reviews.txt")
    results = []

    for review in reviews:
        score = calculate_score(review)
        result_line = f"{review.strip()} --> Score: {score}"
        results.append(result_line)

    write_results("output.txt", results)


if __name__ == "__main__":
    process_reviews()
    print("Processing Complete. Check output.txt")
