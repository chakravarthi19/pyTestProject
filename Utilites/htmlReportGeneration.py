import pytest
import datetime


def generate_report_filename():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    return f"test_report_{timestamp}.html"


if __name__ == "__main__":
    report_filename = generate_report_filename()
    pytest.main([f"--html=reports/{report_filename}"])
