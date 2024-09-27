from kickstart.project import Project
import json

def main():
    
    with open('settings.json') as user_file:
        file_contents = user_file.read()

    settings = json.loads(file_contents)

    proj = Project(settings["project"]["name"],
                    settings["project"]["author"],
                    settings["project"]["description"] )
    
    proj.setOutputFolder( settings["outputFolder"])
    proj.addBlueprints( settings["project"]["blueprints"] )
    proj.generate()

