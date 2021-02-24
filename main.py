# Python libraries
from fpdf import FPDF

# Local imports
from daily_counts import plot_daily_count_states, plot_daily_count_countries

WIDTH = 210
HEIGHT = 297

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello world')

plot_daily_count_states(
    ['New Hampshire', 'Massachusetts'], filename='test.png')
pdf.image('test.png', 5, 30, WIDTH/2-5)

plot_daily_count_countries(
    ['US', 'India'], filename='test2.png')
pdf.image('test2.png', WIDTH/2+5, 30, WIDTH/2-5)

pdf.output('test.pdf', 'F')
