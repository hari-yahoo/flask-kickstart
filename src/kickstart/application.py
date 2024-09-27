import os

from kickstart.blueprint import Blueprint
from kickstart.hatcher import Hatcher

class Application(Hatcher):
    def __init__(self, project_name):
        self.projectName = project_name
        self.blueprints = []

    def addBlueprint(self, name):
        self.blueprints.append(Blueprint(self.projectName,'app', name))

    def generate(self):
        self.createPackage('app')
        self.makeFolder('/app/static')
        self.makeFolder('/app/templates')
        self.generateFile('base.tmpl', '/app/templates', 'base.html', projectName=self.projectName)
        self.generateFile('index.tmpl', '/app/templates', 'index.html', projectName=self.projectName)
        

        # bp = Blueprint(self.projectName, 'app', 'api')
        # bp.generate()
        for bp in self.blueprints:
            bp.generate()