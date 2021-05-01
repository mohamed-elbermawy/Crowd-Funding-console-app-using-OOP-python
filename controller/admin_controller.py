
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

    