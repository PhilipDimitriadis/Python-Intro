def compare_lists(list1: list, list2: list) -> None:
    """
    Compares two lists for identiny and for equality.

    Args: 
        list1 (list): The first list to compare.
        list2 (list): The second list to compare.

    Return:
        None
    """
    # Identiny Check -> list1 is list2
    print(f"{list1} is {list2}: {list1 is list2}")

    # Equality Check -> list1 == list2
    print(f"{list1} == {list2} : {list1 == list2}")

def main():
    my_list = [1, 2, 3]
    your_list = [1, 2, 3]

    # Compare lists
    compare_lists(my_list, your_list)

    print(id(my_list))
    print(id(your_list))

if __name__ == "__main__":
    main()