import yaml

yaml_file = open("settings.yaml", 'r')

class Settings_Loader():

    def __init__(self):
        self.settings_content = yaml.safe_load(yaml_file)
    
    def display_settings(self):
        for key, value in self.settings_content.items():
            print(f"{key}: {value}")