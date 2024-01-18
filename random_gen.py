#secrets library generates less predictable and more secure passowrds than random
import secrets
import string

#pythin randome choice generator using the following types of characters: letters, digits and symbols

def generate_random_password():
    while True:
        #ask user for lenght and number of passwords and  which characters can make up the password  
        length = int(input("Enter a required password length: \n"))
        no_of_passwords = int (input("How many passwords do you want to generate: \n"))
        while True:
            LPD = input("Include letters, numbers and punctuation? yes/no ")
            if LPD[0].lower() == "y":
              charac= string.ascii_letters + string.punctuation + string.digits
              break

            LD = input("Include letters and numbers? yes/no ")
            if LD[0].lower() == "y":
              charac= string.digits + string.ascii_letters
              break
            LP = input("Include letters and punctuation? yes/no ")
            if LP[0].lower() == "y":
              charac= string.ascii_letters + string.punctuation
              break    
        
        #generate n number of secure passwords
        for n in range(no_of_passwords):
            password = "".join(secrets.choice(charac) for n in range(length))
            print(f"Generated Password No {n+1}: \n{password}")
        
        regenerate = input("Generate new password/s? yes/no ")
        if regenerate[0].lower() == "n":
            print("Generator stopped")
            break
        
generate_random_password()