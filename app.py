from models.admin import Admin
from controller.admin_controller import SuperAdminController
from helpers.helpers import Helpers

# admin = Admin("taha","ashraf","a@gmail.com","123","123","000",1,0,1)
admin_controller = SuperAdminController(Helpers)
# admin_controller.add_admin(admin)
# admin_controller.dactivate_admin("aa@gmail.com")
# admin_controller.activate_admin("a@gmail.com")
admin_controller.delete_admin("a@gmail.com")
