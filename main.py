from Client import Client
from Clientlogin import Login
from Freelancer import Freelancer


def add_post(filePath, post):
    posts_file = open(filePath, "a")
    for item in post:
       posts_file.write(item + '\n')
    posts_file.close()

def search_str(filePath, word):
    with open(filePath, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            print(content)
        else:
            print('post not found')


print ("Welcome to our Project\n")
while True:
    print("press 1 for Client\npress 2 for Freelancer\n press 3 to end")
    userchoice = int(input("Enter ur choice: "))
    if userchoice == 1:
        while True:
            print("press 1 for login\npress 2 for register\npress 3 to end")
            loginchoice = int(input("enter ur choice: "))
            if loginchoice == 1:
                clientlogin1 = Login(input("\nplease enter ur email: "), input("please enter ur password: "))
                clientlogin1.clientuser_certify()
                if clientlogin1.clientuser_certify() == False:
                    clientlogin1 = Login(input("\nplease enter ur email: "), input("please enter ur password: "))
                    clientlogin1.clientuser_certify()
                else:
                  break
            elif loginchoice == 2:
                client1 = Client(input("please enter ur name: "), input("please enter ur email: "),
                                 input("please enter ur password: "), input("please enter ur ID: "))
                client1.store_data()
            else:
              break

            while True:
                print("press 1 to add post\npress 2 to view porposals\npress 3 to end")
                postchoice = (int(input("Enter ur choice: ")))
                if postchoice == 1:
                    post1 = [input("Enter post title: "), input("Enter post ID: "),
                                  input("Enter post discreption: "), input("Enter 3 skills required with spaces: ")]
                    add_post("posts.txt", post1)
                elif postchoice == 2:
                    with open("porposals.txt", "r") as porposals_file:
                        porposalsFile = porposals_file.read()
                        print(porposalsFile)
                        try:
                            while True:
                                chosen_porposal = input("Choose porposal by enter freelancer id: ")
                                if chosen_porposal == porposal[0]:
                                    for field in porposal:
                                       print(field)
                                    print("Press 1 to accept porposal\nPress 2 to Reject")
                                    clientDecision = input("Enter your decision: ")
                                    if clientDecision == 1:
                                        porposal[3] = "Accepted"
                                        for field in porposal:
                                            print(field)
                                    elif clientDecision == 2:
                                        porposal[3] = "Rejected"
                                        for field in porposal:
                                            print(field)
                                    else:
                                        break
                                else:
                                    print("Wrong freelancer id")
                        except NameError:
                            print("No porposals submitted")
                else:
                    break
    elif userchoice == 2:
        while True:
            print("press 1 for login\npress 2 for register\npress 3 to end")
            freelancerloginchoice = int(input("enter ur choice: "))
            if freelancerloginchoice == 1:
                freelancerlogin1 = Login(input("\nplease enter ur email: "), input("please enter ur password: "))
                freelancerlogin1.freelanceruser_certify()
            elif freelancerloginchoice == 2:
                freelancerlogin1 = Freelancer(input("please enter ur name: "), input("please enter ur email: "),
                                 input("please enter ur password: "), input("please enter ur ID: "),
                                              input("please enter ur National ID: "))
                freelancerlogin1.store_data()
            else:
              break

            while True:
                print("press 1 to view posts\npress 2 to send porposals\npress 3 to view your porposal\npress 0 to end")
                postchoice = (int(input("Enter ur choice: ")))
                if postchoice == 1:
                    posts_file = open("posts.txt","r")
                    posts_file.read()
                    print (posts_file.read())
                    posts_file.close()
                    title = input("Enter post title to search for: ")
                    search_str("posts.txt", title)

                elif postchoice == 2:
                    porposal = [input("Enter ur ID: "), input("Enter ur postid: "), input("Enter ur skills: "), " "]
                    with open("freelancerusers.txt","r") as userFile:
                        freelancers = userFile.read()
                        if porposal[0] in freelancers:
                            with open("posts.txt","r") as postFiles:
                                posts_file = postFiles.read()
                                if porposal[1] in posts_file:
                                    porposals_file = open("porposals.txt", "a")
                                    for field in porposal:
                                       porposals_file.write(field + '\n')
                                    porposals_file.close()
                                    print("porposal submitted")
                                else:
                                    print("Wrong post id")
                        else:
                            print("No freelancer id found")

                elif postchoice == 3:
                    with open("freelancerusers.txt","r") as userFile:
                        freelancers = userFile.read()
                        if porposal[0] in freelancers:
                            for field in porposal:
                                print(field)
                else:
                   break
    else:
        break


