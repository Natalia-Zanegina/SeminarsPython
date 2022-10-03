import csv
import sqlite3
import json
import collections

def t_csv():
    base = sqlite3.connect('data_base.db')
    cur = base.cursor()
    cur.execute("SELECT * FROM data")

    header = ['last_name', 'name', 'tel', 'description']
    with open('data_base.csv', 'w', encoding='UTF8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",", lineterminator="\r")
        csv_writer.writerow(header)
        csv_writer.writerows(cur)
    base.close()

def t_txt():
    base = sqlite3.connect('data_base.db')
    cur = base.cursor()
    cur.execute("SELECT * FROM data")
    with open('data_base.txt', 'w') as file:
        for i in cur:
            for j in i:
                file.write('{}; \n'.format(j))
    base.close()

# def t_json():
#     base = sqlite3.connect('data_base.db')
#     cur = base.cursor()
#     cur.execute("SELECT * FROM data")
#     rows = cur.fetchall()
#     rowarray_list = []
#     for row in rows:
#         t = (row[0], row[1], row[2], row[3])
#         rowarray_list.append(t)
#     print(rowarray_list)

#     j = json.dump(rowarray_list)

#     with open('data_base.json', 'w') as json_file:
#         json_file.write(j)

#     objects_list = []
#     for row in rows:
#         d = collections.OrderedDict()
#         d['last_name'] = row[0]
#         d['name'] = row[1]
#         d['tel'] = row[2]
#         d['description'] = row[3]
#         objects_list.append(d)

#     j = json.dump(objects_list)
#     with open('data_base.json', 'w') as json_file:
#         json_file.write(j)

#     base.close()


    