from fpdf import FPDF
import pandas as pd
# getting the csv file for data
df = pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit='mm', format='A4')

for index, rows in df.iterrows():
    # getting the pdf set up
    pdf.add_page()
    pdf.set_font(family='Times', style="B", size=12)
    pdf.cell(w=0, h=12, txt=rows['Topic'], align='L', ln=1, border=1)

pdf.output('lined_notepad.pdf')
