def compare_integers(a: int, b: int) -> bool:
    if (a == b):
        print("The numbers are equal")
    elif a > b:
        print("The first is greater than the second number")
    else:
        print("The second number is greater than the second number")


def main():
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Now enter the second number: "))
    except:
        print("Invalid input. Please provide integers")
        return

    compare_integers(a, b)

    # 1. simple example (ternary operator)
    if a > 0:
        print("positive")
    else:
        print("non-positive")

    result = "positive" if a > 0 else "non-positive"
    print(result)

    # 2. extended example (ternary operator)
    result = (
        "The numbers are equal" if a == b else
        "The first is greater than the second number" if a > b else
        "The second number is greater than the second number"
    )
    print(result)

if __name__ == "__main__":
    main()