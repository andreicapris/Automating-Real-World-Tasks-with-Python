#!/usr/bin/env python3 

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import getSampleStyleSheet

def generate_report(filename, title, body):
    report = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles["h1"])
    report_body = Paragraph(body, styles["Normal"])

    report.build([report_title, report_body])
