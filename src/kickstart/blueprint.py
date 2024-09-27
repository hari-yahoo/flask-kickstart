

from kickstart.hatcher import Hatcher


class Blueprint(Hatcher):
    
    def __init__(self, project_name: str, app_folder:str, name: str):
        super().__init__(project_name)
        self.name = name
        self.appFolder = app_folder

    def generate(self):
        self.createPackage(self.appFolder +  '/' + self.name)
        self.generateFile('routes.tmpl', self.appFolder +  '/' + self.name, 'routes.py', name=self.name)
        