import csv
import json


class Home10:

    def __init__(self, json_file: str, csv_file: str):
        self.json_file = json_file
        self.csv_file = csv_file

    def csv_convert_func(self) -> None:
        with (
            open(self.json_file, 'r', encoding='utf-8') as f_json,
            open(self.csv_file, 'w', newline='', encoding='utf-8') as f_csv
        ):
            file_ = json.load(f_json)
            print(file_)

            list_ = [[level_, id_, name_] for level_, i_u in file_.items()
                     for id_, name_ in i_u.items()]
            print(list_)
            writer = csv.writer(f_csv, dialect='excel')
            writer.writerows(list_)


if __name__ == '__main__':
    a = Home10('task32.json', 'task33.csv')
    a.csv_convert_func()
