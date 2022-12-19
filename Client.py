class Client:
    def __init__(self,name,email,password,ID):
        self.name=name
        self.email=email
        self.password=password
        self.ID=ID

    def store_data (self):
        users_file = open("clientusers.txt", "a")
        users_file.write('\n' + 'Client' + self.name + '\n')
        users_file.write('\t' + self.name + '\n')
        users_file.write('\t' + self.email + '\n')
        users_file.write('\t' + self.password + '\n')
        users_file.write('\t' + self.ID + '\n')
        users_file.close()

class Posts:
    def __init__(self,title,post_id,discreption,skills):
        self.title = title
        self.post_id = post_id
        self.discreption = discreption
        self.skills = skills

    def add_post (self):
        posts_file = open("posts.txt", "a")
        posts_file.write(self.title + '\n')
        posts_file.write(self.post_id + '\n')
        posts_file.write(self.discreption + '\n')
        posts_file.write(self.skills + '\n')
        posts_file.close()
