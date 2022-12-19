class Freelancer:

    def __init__(self, fname, femail, fpassword, fID, national_id): #f refers to freelancer
        self.fname = fname
        self.femail = femail
        self.fpassword = fpassword
        self.fID = fID
        self.national_id = national_id

    def store_data(self):
        users_file = open("freelancerusers.txt", "a")
        users_file.write('\n' + 'Freelancer' + self.fname + '\n')
        users_file.write('\t' + self.fname + '\n')
        users_file.write('\t' + self.femail + '\n')
        users_file.write('\t' +self.fpassword + '\n')
        users_file.write('\t' +self.fID + '\n')
        users_file.write('\t' + self.national_id + '\n')
        users_file.close()
