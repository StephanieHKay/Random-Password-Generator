#secrets library generates less predictable and more secure passowrds than random
import secrets
import string

#pythin randome choice generator using the following types of characters: letters, digits and symbols

def generate_random_password():
    while True:
        #ask user for lenght and number of passwords
        length = int(input("Enter a required password length: \n"))
        no_of_passwords = int (input("How many passwords do you want to generate: \n"))
        
        #which characters can make up the password
        charac= string.ascii_letters + string.punctuation + string.digits
        
        #generate n number of secure passwords
        for n in range(no_of_passwords):
            password = "".join(secrets.choice(charac) for n in range(length))
            print(f"Generated Password No {n+1}: \n{password}")
        
        regenerate = input("Generate new password/s? yes/no ")
        if regenerate[0].lower() == "n":
            print("Generator stopped")
            break
        
generate_random_password()