import csv
import os
import re
from PyPDF2 import PdfFileReader

def extract_date(page):
    text = page.extractText()
    date = re.findall("\d\d\.\d\d\.\d{4}", text)
    return date

def read_pdf(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        ticket_id = path[-10:-4]
        number_pages = pdf.getNumPages()
        date_list = []
        if number_pages == 1:
            date_list = extract_date(pdf.getPage(0))[:1]
        elif number_pages == 2:
            # zweiseitig bei Hin- und Rückfahrt
            date_list = extract_date(pdf.getPage(0))[:2]
        elif number_pages == 3:
            # dreiseitig bei Fahradticket
            date_list = extract_date(pdf.getPage(0))[:1]
        elif number_pages == 4:
            # vierseitig bei Hin- und Rückfahrt + CityTicket
            date_list_part_1 = extract_date(pdf.getPage(0))[:1]
            date_list_part_2 = extract_date(pdf.getPage(2))[:1]
            date_list = date_list_part_1 + date_list_part_2

        for el in date_list:
            return ticket_id, date_list

rows = [read_pdf(pdf) for pdf in os.listdir('.') if pdf[-3:] == 'pdf']
csvout = csv.writer(open('bahnfahrten.csv', 'w', newline=''), delimiter=';')
# add header
csvout.writerow(["ticket_id", "date"])
for row in rows:
    if len(row[1]) == 2:
        for date in row[1]:
            csvout.writerow([row[0], date])
    else:
        csvout.writerow([row[0], row[1][0]])
