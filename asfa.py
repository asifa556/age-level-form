def calculate_rank(age):
    if age < 18:
        return "Beginner"
    elif 18 <= age <= 30:
        return "Intermediate"
    else:
        return "Advanced"

def main():
    while True:
        try:
            age = int(input("enter your age (type 'exit' to end): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if age < 0:
            print("Invalid age. Please enter a valid age.")
            continue

        if age == 0:
            print("Goodbye!")
            break

        user_rank = calculate_rank(age)
        print(f"according to your age you are at  {user_rank} level.")

if __name__ == "__main__":
    main()
