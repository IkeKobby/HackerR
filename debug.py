def reverse_number(number):
    return number if len(number) == 0  else reverse_number(number[1:]) + number[0]

def is_palindrome(number: int):
    return int(reverse_number(str(number))) == number

if __name__ == "__main__":
    print(reverse_number("xyz"))