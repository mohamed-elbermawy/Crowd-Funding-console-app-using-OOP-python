from controller.super_admin_controller import SuperAdminController
from controller.normal_user_controller import NormalUserController
from controller.admin_controller import AdminController
from helpers.helpers import Helpers
from models.project import Project
from models.admin import Admin
from models.user import User


super_admin_controller = SuperAdminController(Helpers)
normal_user_controller = NormalUserController(Helpers)
admin_controller = AdminController(Helpers)
helper = Helpers()

# admin = Admin("taha","ashraf","a@gmail.com","123","123","000",1)
# user = User("mohamed","ashraf","a@gmail.com","123","123","000")
# project = Project("pro","pro",20000,"2020-2-30","2022-5-25","a@gmail.com")

# super_admin_controller.create_admin(admin)
# super_admin_controller.dactivate_admin("aa@gmail.com")
# super_admin_controller.activate_admin("a@gmail.com")
# super_admin_controller.delete_admin("a@gmail.com")
# super_admin_controller.create_user(user)
# super_admin_controller.delete_user("a@gmail.com")
# super_admin_controller.register(admin,"db/admin.json")
# print(super_admin_controller.login("b@gmail.com","123","db/admin.json"))

# admin_controller.create_user(user)
# admin_controller.delete_user("a@gmail.com")
# admin_controller.register(admin,"db/admin.json")
# print(admin_controller.login("b@gmail.com","123","db/admin.json"))

# normal_user_controller.add_project(project)
# normal_user_controller.delete_project("pro")
# normal_user_controller.register(user,"db/user.json")
# data = normal_user_controller.view_all_projects()
# print(data)
# print(normal_user_controller.login("a@gmail.com","123","db/user.json"))
# normal_user_controller.search_by_date("2020-2-30","a@gmail.com")

# print(helper.isemail_exsist(user.email,"db/user.json"))


