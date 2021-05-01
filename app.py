from controller.admin_controller import SuperAdminController
from models.admin import Admin
from models.user import User
from helpers.helpers import Helpers

super_admin_controller = SuperAdminController(Helpers)

# admin = Admin("taha","ashraf","a@gmail.com","123","123","000",1,0,1)
user = User("mohamed","ashraf","a@gmail.com","123","123","000")

# super_admin_controller.add_admin(admin)
# super_admin_controller.dactivate_admin("aa@gmail.com")
# super_admin_controller.activate_admin("a@gmail.com")
# super_admin_controller.delete_admin("a@gmail.com")
super_admin_controller.add_user(user)
