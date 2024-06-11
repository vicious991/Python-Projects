from cryptography.fernet import Fernet
def load_key():
    file = open ("key.key","rb")
    key = file.read
    file.close()
    return key

master_pwd = input("what is the master password ? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

'''
def write_key():
    key = Fernet.generate_key()                # run it only oe time to generate the key
    with open("key.key","wb") as key_file:
        key_file.write(key)'''


def view():
    with open ('password.txt','r') as f:
        for line in f.readlines():
            data = print(line.rstrip())
            user , passw = data.split("|")
            print("User:",user , ", Passowrd:",fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open ('password.txt','a') as f:
        f.write(name+ "|"+fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("would you like to add a new password or view existing one (view,add),press q to quit?").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print ("invalid input")
        continue


'''This code snippet is a simple password manager program that allows users to add new passwords or view existing ones. Let's break down the functionality step by step:

1. The `load_key()` function reads a key from a file named "key.key" in binary mode and returns the key. It is using the `cryptography` library's `Fernet` module for encryption and decryption.

2. The user is prompted to enter a master password, which is then encoded and combined with the key obtained from `load_key()` to create a new key for the `Fernet` encryption.

3. The `view()` function reads from a file named "password.txt" and decrypts each line using the `Fernet` key. It then prints out the username and decrypted password for each entry.

4. The `add()` function prompts the user to enter an account name and password. It then encrypts the password using the `Fernet` key and appends the account name and encrypted password to the "password.txt" file.

5. The main loop allows the user to choose between adding a new password or viewing existing passwords. Entering 'q' quits the program. If an invalid input is provided, the user is prompted again.

Overall, this code demonstrates a basic implementation of a password manager using file I/O and encryption techniques. The use of functions helps in organizing the code and separating different functionalities for better readability and maintainability.
'''