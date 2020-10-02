"""This file contains my solutions to Leetcode problem 929: Unique Email Addresses."""


# No built-ins
# time complexity: O(nm), where 'n' is the number of emails and 'm' is the length
# of the longest email
# space complexity: O(nm)

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        number_of_emails = len(emails)
        current_email = 0
        while current_email < number_of_emails:
            filtered_email_characters = []
            character_index = 0
            email = emails[current_email]
            email_length = len(email)
            while character_index < email_length and email[character_index] not in ("+", "@"):
                if email[character_index] != ".":
                    filtered_email_characters.append(email[character_index])
                character_index += 1
            while character_index < email_length and email[character_index] != "@":
                character_index += 1
            if character_index < email_length:
                filtered_email_characters.extend(email[character_index:])
            unique_emails.add(tuple(filtered_email_characters))
            current_email += 1
        return len(unique_emails)
        

# Solution with built-ins. Same complexities.
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        number_of_emails = len(emails)
        current_email = 0
        for index in range(number_of_emails):
            local_name, domain_name = emails[index].split("@")
            local_name_without_plus_sign = local_name.split("+")[0]
            unique_emails.add(local_name_without_plus_sign.replace(".", "") + "@" + domain_name)
        return len(unique_emails)
        
        