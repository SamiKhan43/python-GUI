import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QPushButton
                            ,QVBoxLayout,QHBoxLayout)
from PyQt5.QtCore import QTime,QTimer,Qt

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00:00:00",self)
        self.start_button = QPushButton("start",self)
        self.stop_button = QPushButton("Stop",self)
        self.reset_button = QPushButton("Reset",self)
        self.timer = QTimer(self)
        self.initUI()
        
        
    def initUI(self):
        self.setWindowTitle("STOPWATCH")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)

        self.setStyleSheet(""" 
            QWidget{
                background-color:#121212;
                font:Helvetica; 
            }
            QPushButton{
                background-color: #1F1F1F;
                color: white;
                border-radius: 10px;
                padding: 8px;
                font-size: 16px;
            }
            QLabel{
                color: #00E5FF;
                font-size: 60px;
                letter-spacing: 3px;
                font-weight: bold;
                
            }
            QPushButton:hover {
                background-color: #2A2A2A;
            }

            QPushButton:pressed {
                background-color: #00E5FF;
                color: black;
            }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)
        self.start_button.setDisabled(True)

    def stop(self):
        self.timer.stop()
        self.start_button.setDisabled(False)

    def reset(self):
        self.timer.stop()
        self.start_button.setDisabled(False)
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))
    
    def format_time(self,time):
        hours=time.hour()
        minutes=time.minute()
        seconds=time.second()
        milliseconds=time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())
    