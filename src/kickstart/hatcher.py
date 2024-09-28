import os
import errno
from jinja2 import FileSystemLoader, Environment, PackageLoader, select_autoescape

#templateLoader = FileSystemLoader(searchpath="./kickstart/templates")
templateLoader = PackageLoader("kickstart")
ENV = Environment(
    loader= templateLoader,
    autoescape=select_autoescape()
)


class Hatcher:
    def __init__(self, project_name):
        print(project_name)
        self.projectName = project_name
        print(self.projectName)
    
    def createFolder(self, folderName, mode=755):
       
        try:
            
            os.makedirs(folderName, mode, True)
        except OSError as e:
            if e.errno != errno.EEXIST or not os.path.isdir(folderName):
                raise

    def _buildPath(self, path):
        fullpath = self.projectName +'/' + path
        return os.sep.join (fullpath.split('/'))
    
    def makeFolder(self, folder, mode=755):
        
        path = self._buildPath(folder)

        try:
            os.makedirs(path, mode, True)
        except OSError as e:
            if e.errno!= errno.EEXIST or not os.path.isdir(path):
                raise

    def createPackage(self, name):
        folder = os.path.join(self.projectName, name)
        self.createFolder(folder)
        with open(os.path.join(folder, '__init__.py'), 'a') as f:
            f.write("")

        with open(os.path.join(folder, 'routes.py'), 'a') as f:
            f.write("")

    def generateFile(self, template_jnj, output_folder, output_file, **variables):
        file_path = self._buildPath(output_folder + '/' +output_file)
        template = ENV.get_template(template_jnj)
        output   = template.render(variables)
        with open(file_path, 'w') as f:
            f.write(output)