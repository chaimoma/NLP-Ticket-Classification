from evidently.report import Report
import pandas as pd

def generate_report(reference, current):
    report = Report()
    report.run(reference_data=reference, current_data=current)
    report.save_html("report.html")
