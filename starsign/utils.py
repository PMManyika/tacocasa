import random


def get_random_gift():
    # List of possible gifts
    gifts = [
        "Discount Code: 10OFF",
        "Free eBook: 'The Stars Guide'",
        "Exclusive Astrology Wallpaper",
        "Personalized Horoscope Report",
        "Virtual Star Certificate",
        # Add more gifts as needed
    ]

    # Select and return a random gift
    return random.choice(gifts)
