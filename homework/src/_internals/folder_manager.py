import os


class FolderManager:
    def __init__(self, input_path):
        self.input_path = input_path

    def get_txt_files(self):
        return [
            os.path.join(self.input_path, filename)
            for filename in os.listdir(self.input_path)
            if filename.endswith(".txt")
        ]
