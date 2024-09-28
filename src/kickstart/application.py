import os

from kickstart.blueprint import Blueprint
from kickstart.hatcher import Hatcher

class Application(Hatcher):
    def __init__(self, folder):
        super().__init__( folder + '/app')
        self.blueprints = []

    def addBlueprint(self, name):
        self.blueprints.append(Blueprint(self.folder, name))

    def generate(self):
        print(self.folder)
        self.createPackage(self.folder)
        self.makeFolder(self.folder + '/static')
        self.makeFolder(self.folder + '/templates')
        self.generateFile('base.tmpl', self.folder + '/templates', 'base.html', projectName="projectName")
        self.generateFile('index.tmpl', self.folder + '/templates', 'index.html', projectName="projectName")
       
        for bp in self.blueprints:
            bp.generate()
     