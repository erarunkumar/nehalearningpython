
students = dict()
for i in range(2):
    student = input("enter the name of student ")
    marks = []
    for a in range(5):
        n = int(input("enter mark in subject " + str(a + 1) + " :- "))
        marks.append(n)

    students[student] = marks
print("created dic of students", students)

total = sum(marks)
avg = total / 5
print("the total marks", total)
print("percentage marks are ", avg)
print("now you can open excel worksheet 'book1' to check all data of student")

import xlsxwriter

workbook = xlsxwriter.Workbook('C:\\Users\\neha\\Documents\\book2.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('F1', 'marksheet of student')
bold = workbook.add_format({'bold': 1})
worksheet.set_column('A:A', 13)
worksheet.set_column('B:B', 10)
worksheet.set_column('C:C', 12)
worksheet.set_column('D:D', 11)
worksheet.set_column('E:E', 13)
worksheet.set_column('F:F', 14)
worksheet.set_column('G:G', 10)
worksheet.set_column('H:H', 12)

worksheet.write('A1', 'Student Name', bold)
worksheet.write('B1', 'hindi marks', bold)
worksheet.write('C1', 'English marks', bold)
worksheet.write('D1', 'math marks', bold)
worksheet.write('E1', 'science marks', bold)
worksheet.write('F1', 'drawing marks', bold)
worksheet.write('G1', 'total marks', bold)
worksheet.write('H1', 'percentage %', bold)

data = (['arun', 78, 76, 90, 69, 67],
        ['neha', 89, 78, 90, 89, 78],
        ['gaurav', 76, 56, 67, 98, 78],
        ['ritu', 65, 87, 65, 90, 67],
        ['rashi', 50, 78, 89, 67, 78],
        ['khushboo', 30, 40, 36, 47, 67],
        ['jyoti', 67, 65, 87, 67, 54],
        ['suraj', 34, 89, 65, 74, 98],
        ['yuraj', 56, 78, 54, 65, 10],
        ['nimki', 67, 76, 54, 53, 72]
        )
row = 1
col = 0

for name, hindi_marks, English_marks, math_marks, science_marks, drawing_marks in (data):
    worksheet.write_string(row, col, name)

    worksheet.write_number(row, col + 1, hindi_marks)
    worksheet.write_number(row, col + 2, English_marks)
    worksheet.write_number(row, col + 3, math_marks)
    worksheet.write_number(row, col + 4, science_marks)
    worksheet.write_number(row, col + 5, drawing_marks)
    row += 1

    worksheet.write('G2', '=sum(B2:F2)')
    worksheet.write('G3', '=sum(B3:F3)')
    worksheet.write('G4', '=sum(B4:F4)')
    worksheet.write('G5', '=sum(B5:F5)')
    worksheet.write('G6', '=sum(B6:F6)')
    worksheet.write('G7', '=sum(B7:F7)')
    worksheet.write('G8', '=sum(B8:F8)')
    worksheet.write('G9', '=sum(B9:F9)')
    worksheet.write('G10', '=sum(B10:F10)')
    worksheet.write('G11', '=sum(B11:F11)')

    worksheet.write('H2', '=(G2/500)*100')
    worksheet.write('H3', '=(G3/500)*100')
    worksheet.write('H4', '=(G4/500)*100')
    worksheet.write('H5', '=(G5/500)*100')
    worksheet.write('H6', '=(G6/500)*100')
    worksheet.write('H7', '=(G7/500)*100')
    worksheet.write('H8', '=(G8/500)*100')
    worksheet.write('H9', '=(G9/500)*100')
    worksheet.write('H10', '=(G10/500)*100')
    worksheet.write('H11', '=(G11/500)*100')

workbook.close()


