from diary import find_entries, is_valid_date, save_entry


def main():
    file_name = "diary.txt"

    while True:
        print(f"\nCurrent diary file: {file_name}")
        print("1. Choose a diary file")
        print("2. Add an entry")
        print("3. View entries by date")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            new_file = input(
                "Enter a file name, such as diary2.txt: "
            ).strip()

            if new_file:
                file_name = new_file
                print(f"Selected file: {file_name}")
            else:
                print("The file name cannot be empty.")

        elif choice == "2":
            date_text = input("Enter the date (YYYY-MM-DD): ").strip()

            if not is_valid_date(date_text):
                print("Invalid date. Example: 2026-10-07")
                continue

            entry_text = input("Write your entry on one line: ").strip()

            if not entry_text:
                print("The entry cannot be empty.")
                continue

            try:
                save_entry(file_name, date_text, entry_text)
                print("Entry saved.")
            except OSError as error:
                print(f"Could not save the entry: {error}")

        elif choice == "3":
            date_text = input("Enter the date (YYYY-MM-DD): ").strip()

            if not is_valid_date(date_text):
                print("Invalid date. Example: 2026-10-07")
                continue

            try:
                entries = find_entries(file_name, date_text)
            except OSError as error:
                print(f"Could not read the file: {error}")
                continue

            if entries:
                print(f"Entries for {date_text}:")
                for entry in entries:
                    print(f"- {entry}")
            else:
                print("No entries found for this date in the current file.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Please choose a number from 1 to 4.")


if __name__ == "__main__":
    main()
