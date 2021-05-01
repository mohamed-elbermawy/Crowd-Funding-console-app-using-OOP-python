
class SuperAdminController:
    def __init__(self,Helpers):
        self.helper = Helpers()

    def add_admin(self,admin):
        new_admin = {}

        data = self.helper.loadData("db/admin.json")

        new_admin['frist_name']= admin.fname
        new_admin['last_name']= admin.fname
        new_admin['email']= admin.email
        new_admin['password']= admin.password
        new_admin['phone']= admin.phone
        new_admin['is_staff']=admin.is_staff
        new_admin['is_superuser'] = admin.is_superuser
        new_admin['is_admin_user'] = admin.is_admin_user

        data.append(new_admin)

        self.helper.saveData("db/admin.json",data)
        print("Added")

    def dactivate_admin(self,admin_email):
        data = self.helper.loadData("db/admin.json")
        for admin in data:
            if admin['email'] == admin_email:
                admin['is_staff'] = 0
                self.helper.saveData("db/admin.json",data)
                print(f"{admin_email} Dactivated")
                break
        else:
            print(f"{admin_email} Doesn't exists")

    def activate_admin(self,admin_email):
        data = self.helper.loadData("db/admin.json")
        for admin in data:
            if admin['email'] == admin_email:
                admin['is_staff'] = 1
                self.helper.saveData("db/admin.json",data)
                print(f"{admin_email} Activated")
                break
        else:
            print(f"{admin_email} Doesn't exists")

    def delete_admin(self,admin_email):
        data = self.helper.loadData("db/admin.json")
        for index, admin in enumerate(data):
            if admin['email'] == admin_email:
                data.pop(index)
                self.helper.saveData("db/admin.json",data)
                print(f"{admin_email} Deleted")
                break
        else:
            print(f"{admin_email} Doesn't exists")

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