import datetime
from _pytest.config import create_terminal_writer


def pytest_html_report_title(report):
    return "My Test Report"


def pytest_configure(config):
    config.option.htmlpath = generate_report_filename()


def generate_report_filename():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    return f"reports/test_report_{timestamp}.html"


def pytest_terminal_summary(terminal_reporter, exitstatus):
    terminal_writer = create_terminal_writer(terminal_reporter.config)
    terminal_writer.line("Custom HTML report:", bold=True)
    terminal_writer.sep("=", bold=True)
    report_path = generate_report_filename()
    terminal_writer.line(report_path)
    terminal_writer.sep("=", bold=True)

