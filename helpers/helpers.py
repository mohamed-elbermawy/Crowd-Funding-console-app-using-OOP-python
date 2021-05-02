import json
import re
import datetime


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

    def isString(self , item):
        if item and not item.isdigit():
            return True

        return False

    def isNumber(self , item):
        if item and item.isdigit():
            return True

        return False

    def isemail(self,email):
        email_regix = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if email and re.match(email_regix,email):
            return True

        return False

    def ispassword (self, password , con_password):
        if password is None or con_password is None:
            return False
        if password != con_password:
            return False
        
        return True

    def isphone(self,phone):
        phone_regex = '^01[0125][0-9]{8}'
        if phone and re.match(phone_regex,phone):
            return True

        return False
    
    def isemail_exsist(self,email,file):
        data = self.loadData(file)

        for item in data:
            if item['email'] == email:
                return True

        return False

    def isDate(self , date):
        try:
            if date and datetime.datetime.strptime(date, '%Y-%m-%d'):
                return True
            return False  
        except ValueError:
            return False