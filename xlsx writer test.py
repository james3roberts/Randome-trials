import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet('Sheet1')

worksheet.write('A1', 'Got it')

workbook.close()
