def login_system():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    max_attempts = 3
    
    while max_attempts > 0 :
        retype_password = input("Re-type your password: ")
        
        if retype_password == password:
            print("Login successful!")
            return True 
        else:
            max_attempts -= 1
            print(f"Incorrect password. {max_attempts} attempts left.")
            
        if max_attempts == 0:
            print("Maximum attempts reached. Login failed.")
            return False  

login_system()
