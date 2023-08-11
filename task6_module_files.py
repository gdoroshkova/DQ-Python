import os
import sys
from OOP_task import UserInteraction
from function_task3 import case_normalization


class ImportPublications:
    def __init__(self, file_path="task6_records.txt"):
        self.file_path = file_path
        self.records = []
        self.user_interaction = UserInteraction()

    def download_records(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                content = file.read()
                separator = '**********\n'
                self.records = content.split(separator)

    def upload_records(self):
        for record in self.records:
            if record:
                rows = record.split('\n')
                text = case_normalization(rows[1].replace('text: ', ''))

                if record.startswith('News'):
                    city = rows[2].replace('city: ', '')
                    self.user_interaction.add_publication("News", text=text, city=city)
                elif record.startswith('Private Ad'):
                    expiration_date = rows[2].replace('expiration_date: ', '')
                    self.user_interaction.add_publication("Advertising", text=text, expiration_date=expiration_date)
                elif record.startswith('Motivation'):
                    audience = rows[2].replace('audience: ', '')
                    self.user_interaction.add_publication("Motivation", text=text, audience=audience)
        self.user_interaction.save_publication()

    def remove_file(self):
        os.remove(self.file_path)


import_publications = ImportPublications()
try:
    import_publications.download_records()
    import_publications.upload_records()
    # import_publications.remove_file()
except:
    print("Error!")



