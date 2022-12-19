class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def clientuser_certify(self):
        with open("clientusers.txt","r") as file:
            content = file.read()
            if self.email in content and self.password in content:
                print ("Welcome Client")
                return True
            else:
                print ("Email or password is incorrect")
                return False

    def freelanceruser_certify(self):
        with open("freelancerusers.txt","r") as file:
            content = file.read()
            if self.email in content and self.password in content:
                print ("Welcome Freelancer")
            else:
                print ("Email or password is incorrect")