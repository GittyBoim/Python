import openpyxl as xl

wb = xl.load_workbook('winner.xlsx')
sheet = wb['sheet1']

sheet['A1'] = "שם"
sheet['B1'] = "הצלחה"
sheet['C1'] = "כשלון"
sheet['D1'] = "סהכ נקודות"
wb.save('winner.xlsx')

#המשתנה מחזיק את מספר השורה של המשתמש הנוכחי
current_user = None

#פונקציה שיוצרת את חשבון המשתמש בקובץ
def typeName(userName):
    global current_user
    current_user = None
    column = sheet['A']
    for cell in column:
        if cell.value == userName:
            current_user = cell.row
    if not current_user:
        current_user = sheet.max_row+1
        sheet[f'A{current_user}'] = userName
        sheet[f'B{current_user}'] = 0
        sheet[f'C{current_user}'] = 0
        sheet[f'D{current_user}'] = 0
    wb.save('winner.xlsx')

#הפונקציה מעדכנת את הנקודות של המשתמש מקבלת True אם הצליח וFakse אחרת
def update(flag):
    if flag:
        sheet[f'B{current_user}'].value += 1
    else:
        sheet[f'C{current_user}'].value += 1
    wb.save('winner.xlsx')


#הפונקציה סוכמת את הנקודות השליליות והחיוביות ומציבה בעמודה המתאימה בקובץ
def sumPoints():
    sheet[f'D{current_user}'].value += (
                (50 * sheet[f'B{current_user}'].value) - (30 * sheet[f'C{current_user}'].value))
    wb.save('winner.xlsx')
