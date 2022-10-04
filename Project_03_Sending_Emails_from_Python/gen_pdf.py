"""This script contains functions used in the main script cars.py"""
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib import colors

def create_list(in_dict):
#This function creates a list from the dictionary input in order to add it to the pdf.
    out_list = []
    for element in in_dict:
        temp_list = []
        temp_list.append(element['id'])
        concat_string = "{} {} ({})".format(element['car']['car_make'], element['car']['car_model'], element['car']['car_year'])
        temp_list.append(concat_string)
        temp_list.append(element['price'])
        temp_list.append(element['total_sales'])
        out_list.append(temp_list)

    return out_list


def generate_pdf(body, in_list):
#This function generates the pdf with the summary and the table containing more detailed information.
    report = SimpleDocTemplate("report.pdf")
    
    styles = getSampleStyleSheet()
    
    report_title = Paragraph("Sales Summary for the last month", styles["h1"])
    report_body_1 = Paragraph(body[0] , styles["Normal"])
    report_body_2 = Paragraph(body[1] , styles["Normal"])
    report_body_3 = Paragraph(body[2] , styles["Normal"])
    table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
    report_table = Table(data=in_list, style=table_style, hAlign="LEFT")
    
    report.build([report_title, report_body_1, report_body_2, report_body_3, report_table])
