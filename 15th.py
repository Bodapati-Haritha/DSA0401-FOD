def calculate_likes_frequency(likes_list):
    likes_freq = {}
    for likes in likes_list:
        likes_freq[likes] = likes_freq.get(likes, 0) + 1
    return likes_freq
def display_likes_frequency_distribution(likes_freq):
    print("Likes\tFrequency")
    for likes, freq in likes_freq.items():
        print(f"{likes}\t{freq}")
if __name__ == "__main__":
    post_likes = [1000, 15000, 1200, 1200, 250000, 2000, 18890, 12300,23150,45100,45250]
    likes_frequency = calculate_likes_frequency(post_likes)
    display_likes_frequency_distribution(likes_frequency)
