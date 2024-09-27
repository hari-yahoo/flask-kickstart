

from kickstart.blueprint import Blueprint
from kickstart.application import Application
from kickstart.hatcher import Hatcher


class Project(Hatcher):
    def __init__(self, project_name, author, description):
        super().__init__(project_name)
        self.author = author
        self.description = description
        self.application = Application(project_name)
        self.application.addBlueprint('main')

    def generate(self):
        print('Generating code for ' + self.projectName )
        folderName = self.projectName
      
        self.createFolder(folderName)
        self.generateFile('readme.tmpl', '/', 'README.md', projectName=self.projectName, description=self.description, author=self.author)
        #app = Application(self.projectName)
        self.application.generate()
    def setOutputFolder(self, folder):
        self._outputFolder = folder
        
    def addBlueprints(self, blueprints):
        for blueprint in blueprints:
            self.application.addBlueprint(blueprint)