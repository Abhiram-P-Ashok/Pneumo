'''from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys


class WebAppViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.webview = QWebEngineView()
        self.webview.setUrl(QUrl('https://pneumo.pythonanywhere.com'))

        self.setCentralWidget(self.webview)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Web App Viewer')
        self.setWindowIcon(QIcon('Icons8-Ios7-Healthcare-Lungs.ico'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WebAppViewer()
    window.show()
    sys.exit(app.exec_())'''

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
import subprocess
import os

# Import pywin32
try:
    from win32com.client import Dispatch
except ImportError:
    print("pywin32 module is required. Install it using 'pip install pywin32'.")


class WebApp(QMainWindow):
    def __init__(self):
        super(WebApp, self).__init__()

        # Execute your app.py script
        self.execute_app_script()

        # Create a web browser widget
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://pneumo.pythonanywhere.com")) 

        # Set the web browser widget as the central widget
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Set application icon
        icon_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Icons8-Ios7-Healthcare-Lungs.ico')  

    def execute_app_script(self):
        # Replace 'app.py' with the actual name of your Flask app script
        script_path = os.path.abspath('C:\\Users\\PC\\OneDrive\\Desktop\\pneumonia_detection\\project\\Pneumo\\app.py')

        # Execute the app.py script
        subprocess.Popen(['python', script_path], shell=True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName("Pneumo")
    window = WebApp()
    app.exec_()
