# extent_reports.py
class ExtentSparkReporter:
    def __init__(self, file_path):
        self.file_path = file_path

class ExtentReports:
    def __init__(self):
        self.reporter = None

    def attach_reporter(self, reporter):
        self.reporter = reporter

    def log(self, message):
        with open(self.reporter.file_path, 'a') as f:
            f.write(message + '\n')