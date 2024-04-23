from fpdf import FPDF
import pandas as pd
# getting the csv file for data
df = pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit='mm', format='A4')

for index, rows in df.iterrows():
    # getting the pdf set up # placed in forloop to get more pages # aka main parent
    # setting the header
    pdf.add_page()
    pdf.set_font(family='Times', style="B", size=24)
    pdf.cell(w=0, h=24, txt=rows['Topic'], align='L', ln=1)
    pdf.line(10, 28, 200, 28)

    # setting the additional pages
    # -1 to take in consideration of the main add page
    for i in range(rows['Pages'] - 1):
        pdf.add_page()

pdf.output('lined_notepad.pdf')
