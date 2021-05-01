class AdminController:
    def __init__(self,Helpers):
        self.helper = Helpers()

    def add_user(self,user):
    new_user = {}

    data = self.helper.loadData("db/user.json")

    new_user['frist_name']= user.fname
    new_user['last_name']= user.fname
    new_user['email']= user.email
    new_user['password']= user.password
    new_user['phone']= user.phone

    data.append(new_user)

    self.helper.saveData("db/user.json",data)
    print("Added")