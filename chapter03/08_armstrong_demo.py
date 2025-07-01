def is_armstrong_number(num):   # 153
    digits = str(num)
    power = len(digits)
    total = 0

    # '1', '5', '3'
    for digit in digits:
        total += int(digit) ** power 

    return num == total

def main():
    try:
        num = int(input("Please insert an int: "))
    except ValueError:
        print("Invalid input")
        return

    if is_armstrong_number(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} isn't an Armstrong number")

    #num = (
    #    f"{num} is an Armstrong number" if is_armstrong_number(num) else
    #    f"{num} isn't an Armstrong number" if is_armstrong_number(num) else
    #    "Invalid input"
    #)
    #print(num)

if __name__ == "__main__":
    main()