# Python libraries
from fpdf import FPDF

# Local imports
from daily_counts import plot_daily_count_states, plot_daily_count_countries
from time_series_analysis import plot_states, plot_countries
from helper import Mode

WIDTH = 210
HEIGHT = 297


def create_report(filename='tutorial.pdf'):
    pdf = FPDF()
    ''''First page'''
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Hello world')

    '''Second Page'''
    states = ['New Hampshire', 'Massachusetts']
    plot_daily_count_states(states, filename='test.png')
    pdf.image('test.png', 5, 30, WIDTH/2-5)

    plot_daily_count_states(states, mode=Mode.DEATHS, filename='test2.png')
    pdf.image('test2.png', WIDTH/2+5, 30, WIDTH/2-5)

    plot_states(states, filename='test3.png')
    pdf.image('test3.png', 5, 110, WIDTH/2-5)

    plot_states(states, mode=Mode.DEATHS, filename='test4.png')
    pdf.image('test4.png', WIDTH/2+5, 110, WIDTH/2-5)

    pdf.output(filename, 'F')


if __name__ == '__main__':
    create_report('test.pdf')
