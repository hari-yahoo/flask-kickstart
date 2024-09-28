

from kickstart.hatcher import Hatcher


class Blueprint(Hatcher):
    
    def __init__(self, folder: str, name: str):
        super().__init__(folder + '/' + name)
        self.name = name
      

    def generate(self):
        self.createPackage(self.folder)
        self.generateFile('routes.tmpl', self.folder, 'routes.py', name=self.name)
        