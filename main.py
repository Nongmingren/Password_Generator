import random
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_letter = string.punctuation


def Generate_password():
    #############################################################################
    print("---------- Password Generator ---------")
    length_password = int(input("Length Password: "))
    use_lowercase = input("Lowercase (YES/NO): ")
    if use_lowercase.upper() == "YES":
        use_lowercase = True
    else:
        use_lowercase = False
    use_uppercase = input("UPPERCASE (YES/NO): ")
    if use_uppercase.upper() == "YES":
        use_uppercase = True
    else:
        use_uppercase = False
    use_digits = input("DIGITS (YES/NO): ")
    if use_digits.upper() == "YES":
        use_digits = True
        minimum_digits = int(input("\t- Minimum Digits: "))
    else:
        use_digits = False
        minimum_digits = 0
    use_special = input("Special (YES/NO): ")
    if use_special.upper() == "YES":
        use_special = True
        minimum_special = int(input("\t- Minimum special: "))
    else:
        use_special = False
        minimum_special = 0
    print(minimum_digits)
    print(minimum_special)
#######################################################################
    # print(f"lENGTH: {length_password}")
    # print(f"UPPERCASE: {use_uppercase}")
    # print(f"Lowercase: {use_lowercase}")
    # print(f"Digits: {use_digits}")
    # print(f"Special Letter: {use_special}")
    candidate_characters = {"use_lowercase": use_lowercase,
                            "use_uppercase": use_uppercase,
                            "use_digits": use_digits,
                            "use_special": use_special
                            }
    # print(f"candidate: {candidate_characters}")
    list_candidate = []
    for candidate, use in candidate_characters.items():
        if use:
            list_candidate.append(candidate)
    # print(f"after candidate: {list_candidate}")

    print("-"*40)
##################################################################
    list_password = []
    count_digits = 0
    count_special_letters = 0
    print("Generating...")
    for _ in range(length_password):

        if count_digits < minimum_digits:
            candidate = "use_digits"
        elif count_special_letters < minimum_special:
            candidate = "use_special"
        else:
            candidate = random.choice(list_candidate)
            #print(candidate)
        if candidate == "use_lowercase":
            character = random.choice(lowercase)
        elif candidate == "use_uppercase":
            character = random.choice(uppercase)
        elif candidate == "use_special":
            character = random.choice(special_letter)
            count_special_letters += 1
        elif candidate == "use_digits":
            count_digits += 1
            character = random.choice(digits)

            
        #print(f"candidate: {candidate} {character}")
        list_password.append(character)
    #print(list_password)
    password = "".join(list_password)
    print("Done")
    print(f"Digits: {count_digits}")
    print(f"Special Letter: {count_special_letters}")
    return password


if __name__ == '__main__':
    my_password = Generate_password()
    print(f"My Password: {my_password}")
#number_of_numbers = thislist.count(list_password)
