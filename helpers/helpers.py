import json
import re


class Helpers:
    def __init__(self):
        pass
    
    def loadData(self,file):
        try:
            db = open(file,'r')
            data_string = db.read()
            db.close()
            data = json.loads(data_string)
            return data
        except Exception:
            return []
        
    def saveData(self,file,data):
        try:
            db = open(file,'w')
            db.write(json.dumps(data))
            db.close()
        except Exception:
            print(f"{file} Doesn't exists")

    def isfirst_name(self , first_name):
        if first_name is None or first_name.isdigit():
            return False

        return True

    def islast_name(self , last_name):
        if last_name is None or last_name.isdigit():
            return False
            
        return True

    def isemail(self,email):
        email_regix = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if email is None or not re.match(email_regix,email):
            return False

        return True

    def ispassword (self, password , con_password):
        if password is None or con_password is None:
            return False
        if password != con_password:
            return False
        
        return True

    def isphone(self,phone):
        phone_regex = '^01[0125][0-9]{8}'
        if phone is None or not re.match(phone_regex,phone):
            return False

        return True