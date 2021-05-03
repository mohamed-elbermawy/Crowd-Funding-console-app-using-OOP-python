from controller.normal_user_controller import NormalUserController

class AdminController(NormalUserController):
    def __init__(self,Helpers):
        self.helper = Helpers()

    def create_user(self,user):
        new_user = {}

        data = self.helper.loadData("db/user.json")

        new_user['frist_name']= user.fname
        new_user['last_name']= user.lname
        new_user['email']= user.email
        new_user['password']= user.password
        new_user['phone']= user.phone

        data.append(new_user)

        self.helper.saveData("db/user.json",data)
        print("Added")

    def delete_user(self,user_email):
        data = self.helper.loadData("db/user.json")
        for index, user in enumerate(data):
            if user['email'] == user_email:
                data.pop(index)
                self.helper.saveData("db/user.json",data)
                print(f"{user_email} Deleted")
                break
        else:
            print(f"{user_email} Doesn't exists")