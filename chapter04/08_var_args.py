def my_add(*args: int) -> int:
    return sum(args)

def my_avg(*args: int) -> float:
    return sum(args) / len(args) if args else 0

    # if not args:
    #     return 0
    # else:
    #     return sum(args) / len(args)

def main():
    ages = [27, 18, 35, 22, 32, 27]

    print(my_add(*ages))
    print(my_avg(*ages))

if __name__ == "__main__":
    main()