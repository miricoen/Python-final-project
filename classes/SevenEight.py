import sys


class SevenEight:
    @staticmethod
    def print_python_version():
        python_version = sys.version
        print(f"Python Version: {python_version}")
    @staticmethod
    def process_parameters(*args):
        result_dict = {}
        for arg in args:
            if isinstance(arg, tuple):
                if len(arg) == 2:
                    result_dict[arg[0]] = arg[1]
                else:
                    print(f"Error: Tuple {arg} should contain exactly two elements.")
            else:
                print(arg)

        return result_dict
    @staticmethod
    def read_usernames(filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    yield line.strip()  # Strip whitespace and newline characters
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    @staticmethod
    def remove_first_10_percent(usernames):
        num_users_to_remove = len(usernames) // 10
        modified_usernames = usernames[num_users_to_remove:]
        return modified_usernames

    @staticmethod
    def read_usernames_from_even_rows(filename):
        try:
            with open(filename, 'r') as file:
                for i, line in enumerate(file, 1):
                    if i % 2 == 0:  # Check if the row number is even
                        yield line.strip()
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def read_emails(filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    email = line.strip()
                    if '@' not in email or '.' not in email:
                        print(f"Invalid email address found: {email}")
                    else:
                        print(f"Valid email address: {email}")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def read_gmail(filename):
        gmail_emails = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    email = line.strip()
                    if '@gmail.com' in email:
                        gmail_emails.append(email)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return gmail_emails

    @staticmethod
    def check_username_in_email(emails_file, names_file):
        email_username_dict = {}
        try:
            with open(emails_file, 'r') as emails, open(names_file, 'r') as names:
                for email, name in zip(emails, names):
                    email = email.strip()
                    name = name.strip()
                    if email not in email_username_dict:
                        email_username_dict[email] = name
                    else:
                        print(f"Duplicate email address found: {email}")

            for email, username in email_username_dict.items():
                if username.lower() in email.lower():
                    print(f"Email '{email}' contains the username '{username}'.")
                else:
                    print(f"Email '{email}' does not contain the username '{username}'.")

        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def check_and_modify_name(user_name, names_file):
        try:
            # Read names from the file into a list
            with open(names_file, 'r') as file:
                names_list = file.read().splitlines()

            # Check if the user's name is in the list
            if user_name in names_list:
                print(f"{user_name} is in the list of names.")
            else:
                print(f"{user_name} is not in the list of names.")

            # Try changing the name by replacing 'A' with different formats
            modified_names = []
            for format in ['a', 'A', chr(65), chr(97)]:
                modified_name = user_name.replace('A', format)
                modified_names.append(modified_name)

            # Check if modified names are in the list
            for modified_name in modified_names:
                if modified_name in names_list:
                    print(f"Modified name '{modified_name}' is in the list of names.")
                else:
                    print(f"Modified name '{modified_name}' is not in the list of names.")

        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def read_user_names(filename):
        try:
            # Open the file and read its contents
            with open(filename, 'r') as file:
                # Read lines from the file and strip any leading or trailing whitespace
                names = [line.strip() for line in file]
            return names
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return []

    @staticmethod
    def calculate_earnings(teams):
        total_earnings = 0
        for team in teams:
            if team % 8 == 0:
                total_earnings += 200
            else:
                additional_users = team % 8
                total_earnings += 200 + (additional_users * 50)
        return total_earnings

def main():
    # Test print_python_version
    SevenEight.print_python_version()

    # Test process_parameters
    result_dict = SevenEight.process_parameters(('a', 1), ('b', 2), 'invalid', ('c',))
    print("Processed Parameters:", result_dict)

    # Test remove_first_10_percent
    usernames = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7', 'user8', 'user9', 'user10']
    modified_usernames = SevenEight.remove_first_10_percent(usernames)
    print("Modified Usernames:", modified_usernames)

    # Test read_usernames_from_even_rows
    even_usernames = list(SevenEight.read_usernames_from_even_rows('test.txt'))
    print("Even Usernames:", even_usernames)

    # Test read_emails
    SevenEight.read_emails('emails.txt')

    # Test read_gmail
    gmail_emails = SevenEight.read_gmail('emails.txt')
    print("Gmail Emails:", gmail_emails)

    # Test check_username_in_email
    SevenEight.check_username_in_email('emails.txt', 'names.txt')

    # Test check_and_modify_name
    SevenEight.check_and_modify_name('User1', 'names.txt')

    # Test read_user_names
    names = SevenEight.read_user_names('names.txt')
    print("User Names:", names)

    # Test calculate_earnings
    total_earnings = SevenEight.calculate_earnings([24, 32, 88])
    print("Total Earnings:", total_earnings)


if __name__ == "__main__":
    main()
