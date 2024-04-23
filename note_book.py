from fpdf import FPDF
import pandas as pd
# getting the csv file for data
df = pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for index, rows in df.iterrows():
    # getting the pdf set up # placed in forloop to get more pages # aka main parent
    # setting the header
    pdf.add_page()
    pdf.set_font(family='Times', style="B", size=24)
    pdf.cell(w=0, h=12, txt=rows['Topic'], align='L', ln=1)

    # setting page lines
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # setting the footer
    pdf.ln(265)
    pdf.set_font(family='Times', style="I", size=8)
    pdf.cell(w=0, h=10, txt=rows['Topic'], align='R')


    # setting the additional pages
    # -1 to take in consideration of the main add page
    for i in range(rows['Pages'] - 1):
        pdf.add_page()

    # setting page lines
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # setting the footer
    # added 12 to 265 to get 277
    pdf.ln(277)
    pdf.set_font(family='Times', style="I", size=8)
    pdf.cell(w=0, h=10, txt=rows['Topic'], align='R')

pdf.output('lined_notepad.pdf')
