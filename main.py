from fpdf import FPDF

var = 'report using typed literals'
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, f'Hello world, this the first PDF {var}!')
pdf.output('test.pdf', 'F')
