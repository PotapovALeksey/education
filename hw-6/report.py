from datetime import datetime

line_template = '{:-<15}{:->8} \n'
format_template = '{:<15}|{:>7} \n'

report_dictionary = {}
start_time = None

def add_report_operation(name):
    global start_time

    if start_time == None:
        start_time = datetime.now()

    if name in report_dictionary:
        report_dictionary[name] = report_dictionary[name] + 1
    else:
        report_dictionary[name] = 1

def get_report():
    report = format_template.format('Operation', 'Count') + line_template.format('', '')

    for key, value in report_dictionary.items():
        report += format_template.format(key, value)

    return start_time, report
