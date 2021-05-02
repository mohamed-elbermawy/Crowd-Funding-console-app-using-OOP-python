class NormalUserController:
    def __init__(self,Helpers):
        self.helper = Helpers()

    def add_project(self,project):
        new_project = {}

        data = self.helper.loadData("db/project.json")

        new_project['title']= project.title   
        new_project['details']= project.details
        new_project['total_target']= project.total_target
        new_project['start_time']= project.start_time
        new_project['end_time']= project.end_time
        new_project['auther']= project.auther

        data.append(new_project)

        self.helper.saveData("db/project.json",data)
        print("Added")
    
    def delete_project(self,project_title):
        data = self.helper.loadData("db/project.json")
        for index, project in enumerate(data):
            if project['title'] == project_title:
                data.pop(index)
                self.helper.saveData("db/project.json",data)
                print(f"{project_title} Deleted")
                break
        else:
            print(f"{project_title} Doesn't exists")