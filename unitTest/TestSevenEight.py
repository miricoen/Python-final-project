import unittest
from unittest.mock import patch
from classes.SevenEight import SevenEight

class TestSevenEight(unittest.TestCase):

    @patch('builtins.print')
    def test_print_python_version(self, mock_print):
        SevenEight.print_python_version()
        mock_print.assert_called_once()

    def test_process_parameters(self):
        result_dict = SevenEight.process_parameters(('a', 1), ('b', 2), 'invalid', ('c',))
        self.assertIsInstance(result_dict, dict)
        self.assertEqual(result_dict, {'a': 1, 'b': 2})

    def test_remove_first_10_percent(self):
        usernames = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7', 'user8', 'user9', 'user10']
        modified_usernames = SevenEight.remove_first_10_percent(usernames)
        self.assertEqual(len(modified_usernames), 9)

    def test_read_usernames_from_even_rows(self):
        with patch('builtins.open') as mock_open:
            mock_file = mock_open.return_value
            mock_file.__enter__.return_value.__iter__.return_value = ['1\n', '2\n', '3\n', '4\n', '5\n']
            usernames = list(SevenEight.read_usernames_from_even_rows('test.txt'))
            self.assertEqual(usernames, ['2', '4'])

    @patch('builtins.print')
    def test_read_emails(self, mock_print):
        with patch('builtins.open') as mock_open:
            mock_file = mock_open.return_value
            mock_file.__enter__.return_value.__iter__.return_value = ['example1@gmail.com\n', 'example2\n']
            SevenEight.read_emails('test.txt')
            mock_print.assert_called_once_with("Valid email address: example1@gmail.com")

    def test_read_gmail(self):
        with patch('builtins.open') as mock_open:
            mock_file = mock_open.return_value
            mock_file.__enter__.return_value.__iter__.return_value = ['example1@gmail.com\n', 'example2@yahoo.com\n']
            gmail_emails = SevenEight.read_gmail('test.txt')
            self.assertEqual(gmail_emails, ['example1@gmail.com'])

    @patch('builtins.print')
    def test_check_username_in_email(self, mock_print):
        with patch('builtins.open') as mock_open_emails, patch('builtins.open') as mock_open_names:
            mock_open_emails.return_value.__iter__.return_value = ['example1@gmail.com\n', 'example2@yahoo.com\n']
            mock_open_names.return_value.__iter__.return_value = ['User1\n', 'User2\n']
            SevenEight.check_username_in_email('emails.txt', 'names.txt')
            mock_print.assert_any_call("Email 'example1@gmail.com' contains the username 'User1'.")
            mock_print.assert_any_call("Email 'example2@yahoo.com' does not contain the username 'User2'.")

    def test_check_and_modify_name(self):
        with patch('builtins.open') as mock_open:
            mock_open.return_value.__enter__.return_value.read.return_value = 'User1\nUser2\n'
            SevenEight.check_and_modify_name('User1', 'names.txt')  # Assuming 'User1' is in the file
            # No direct assertion possible as this function prints output

    def test_read_user_names(self):
        with patch('builtins.open') as mock_open:
            mock_open.return_value.__enter__.return_value.__iter__.return_value = ['User1\n', 'User2\n']
            names = SevenEight.read_user_names('test.txt')
            self.assertEqual(names, ['User1', 'User2'])

    def test_calculate_earnings(self):
        total_earnings = SevenEight.calculate_earnings([24, 32, 88])
        self.assertEqual(total_earnings, 650)

    if __name__ == '__main__':
        unittest.main()

