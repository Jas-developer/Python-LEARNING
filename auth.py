class Authentication:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
    
    def __str__(self):
        password = "jameson"
        username = "bayot"
        
        if self.username == username and password == self.password:
            return f"You are now logined {self.username} and your email is {self.email}"
        else:
            return "Invalid credintials"
        



person = Authentication("bayot","bayot@gmail.com","jameson")
print(person)