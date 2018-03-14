import random

from dongers import dongers
from emotions import emotions


def handle_message(message):

    needed_donger = message.split()[-1]
    random_donger = random.choice(dongers[needed_donger])
    if message.split()[1] != 'stats':
        emotions[needed_donger] += 1
    if message.split()[1] == 'stats':
        return emotions[needed_donger]
    else:
        return random_donger


if __name__ == "__main__":

    nickname = input("Enter your nickname: ")

    while True:
        msg = input("Your message: ")
        ans = handle_message(msg)

        print(ans)
