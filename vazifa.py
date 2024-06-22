from db import Database
import openpyxl

db = Database(dbname="fn21",user="postgres",password="*secret*")

path = 'users.xlsx'
wb = openpyxl.load_workbook(path)
sheet = wb.active


db.create_table()
for row in sheet.iter_rows(values_only=True):
    adding = db.add_users(row)
    if adding:
        print(f"{row[1]}, bazaga saqlandi!")
    else:
        print(f"{row[1]}, bazaga saqlanmadi..")
