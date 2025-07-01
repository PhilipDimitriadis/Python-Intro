import random

def get_user_guess():
    while True:
        try:
            return int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer")

def check_guess(secret, guess):
    if guess == secret:
        print("Bingo. Secret number: ", secret)
        return True
    elif abs(secret - guess) <= 5:
        print("Hot")
    else:
        print("Cold")
    return False

def main():
    secret_num = random.randint(1, 10)
    MAX_TRIES = 5
    tries = 0

    while tries < MAX_TRIES:
        guess = get_user_guess()
        
        if check_guess(secret=secret_num, guess=guess):
            break
        
        tries += 1

    if tries == MAX_TRIES:
        print("Maximum number of tries have been reached")

if __name__ == "__main__":
    main()