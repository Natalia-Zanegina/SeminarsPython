import csv

def export_to_txt():
    with open('data_base.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    with open('base_export.txt', 'w') as file:
        for i in data:
            for j in i:
                file.write('{}; \n'.format(j))