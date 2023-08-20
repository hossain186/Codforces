def main():
    name = input()  # String.
    name = dict.fromkeys(name)  # Convert it to dictionary to remove duplicates.

    if len(name) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")


if __name__ == "__main__":
    main()
