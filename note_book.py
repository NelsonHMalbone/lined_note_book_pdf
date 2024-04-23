from fpdf import FPDF
import pandas as pd
# getting the csv file for data
df = pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit='mm', format='A4')

for index, rows in df.iterrows():
    # getting the pdf set up # placed in forloop to get more pages # aka main parent
    pdf.add_page()
    pdf.set_font(family='Times', style="B", size=24)
    pdf.cell(w=0, h=24, txt=rows['Topic'], align='L', ln=1)
    pdf.line(10, 28, 200, 28)


pdf.output('lined_notepad.pdf')
