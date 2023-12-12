import string
import secrets
import random

# [Brute Force Method] Generate a random hexadecimal.
def generate_random_alphnum():
    # Define choice as an option between 16 charcters. Allow for a repeat of previosly selected characters.
    # Define a tuple as the choices of hexadecimal characters. We want to target speed.
    hex_chars = ("0", "1", "2", "3", "4", "5", "6", "8", "9", "A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f")

    # Iterate through 6 positions of a list to generate the hexadecimal string.
    random_hexadecimal_string = []
    for x in range(6):
        random_choice = random.choice(hex_chars)
        random_hexadecimal_string.append(random_choice)
    
    # Join the elements within the list to form hexadecimal string.
    seperator =''
    hex_string = seperator.join(random_hexadecimal_string)

    return hex_string


# [Method 2] Leveraging Python Built ins
def generate_url_string():
     # String Length
     N = 7
     # leveraging python's secrets module to populate choices.
     url_string = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(N))
     return url_string


def main():
    for i in range(3):
        # Brute Force Method
        # rand_string = generate_random_alphnum()
        # Using python built ins
        rand_string = generate_url_string()
        print(f"Heres a random hexadeximal {rand_string}")

    print(f"[+] randhex has finished execution.")
    return

if __name__ == "__main__":
        main()