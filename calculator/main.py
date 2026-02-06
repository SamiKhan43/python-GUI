import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton,
    QVBoxLayout, QGridLayout, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class CalculatorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(380, 600)
        self.current_value = "0"

        self.last_operator = None
        self.last_operand = None
        self.initUI()
        self.apply_styles()
    
    def initUI(self):
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(90)
        self.display.setFont(QFont('Segoe UI', 28, QFont.Light))
        self.display.setText("0")
        
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(25, 25, 25, 25)
        
        grid_layout = QGridLayout()
        grid_layout.setSpacing(15)
        
        buttons = [
            ['AC', '←', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '=']
        ]
        
        for row_idx, row in enumerate(buttons):
            for col_idx, text in enumerate(row):
                button = QPushButton(text)
                button.setFixedSize(70, 70)
                button.setFont(QFont('Segoe UI', 20, QFont.Normal))
                button.clicked.connect(lambda checked, t=text: self.on_button_click(t))
                button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                
                if text in ['/', '*', '-', '+']:
                    button.setObjectName("operator")
                elif text == '=':
                    button.setObjectName("equals")
                elif text in ['AC', '←', '%', '±']:
                    button.setObjectName("function")
                elif text == '0':
                    button.setObjectName("zero")
                else:
                    button.setObjectName("number")
                
                grid_layout.addWidget(button, row_idx, col_idx)
        
        main_layout.addWidget(self.display)
        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)
    
    def apply_styles(self):
        self.setStyleSheet("""
            QWidget { background-color: #121212; }

            QLineEdit {
                background-color: #1e1e1e;
                color: #ffffff;
                border: none;
                border-radius: 20px;
                padding: 20px;
                font-size: 32px;
                font-weight: bold;
            }

            QPushButton {
                background-color: #2a2a2a;
                color: #ffffff;
                border: none;
                border-radius: 35px;
                font-size: 22px;
                font-weight: bold;
            }

            QPushButton:hover { background-color: #3a3a3a; }
            QPushButton:pressed { background-color: #1f1f1f; }

            QPushButton#operator {
                background-color: #ff9500;
                color: #ffffff;
            }
            QPushButton#operator:hover { background-color: #ffb347; }
            QPushButton#operator:pressed { background-color: #cc7a00; }

            QPushButton#function {
                background-color: #555555;
                color: #ffffff;
            }
            QPushButton#function:hover { background-color: #666666; }
            QPushButton#function:pressed { background-color: #444444; }

            QPushButton#number {
                background-color: #2a2a2a;
                color: #ffffff;
            }
            QPushButton#number:hover { background-color: #3a3a3a; }
            QPushButton#number:pressed { background-color: #1f1f1f; }

            QPushButton#zero {
                background-color: #2a2a2a;
                color: #ffffff;
                border-radius: 35px;
            }
        """)
    
    def on_button_click(self, button_text):
        current = self.display.text()
        
        if button_text == "AC":
            self.display.setText("0")
            self.last_operator = None
            self.last_operand = None
        
        elif button_text == "←":
            if len(current) > 1:
                self.display.setText(current[:-1])
            else:
                self.display.setText("0")
        
        elif button_text == "±":
            if current != "0" and current != "Error":
                try:
                    if current.startswith("-"):
                        self.display.setText(current[1:])
                    else:
                        self.display.setText("-" + current)
                except:
                    pass
        
        elif button_text == "%":
            try:
                result = str(float(eval(current)) / 100)
                self.display.setText(result)
            except:
                self.display.setText("Error")
        
        elif button_text == "=":
            try:
                if self.last_operator is None:
                    result = str(eval(current))
                    for op in '+-*/':
                        if op in current:
                            parts = current.rsplit(op, 1)
                            if len(parts) == 2:
                                self.last_operator = op
                                self.last_operand = parts[1]
                            break
                else:
                    result = str(eval(current + self.last_operator + self.last_operand))
                
                self.display.setText(result)
            except:
                self.display.setText("Error")
        
        else:
            if button_text in "+-*/":
                self.last_operator = None
                self.last_operand = None
            
            if current == "0" or current == "Error":
                if button_text in "0123456789.":
                    self.display.setText(button_text)
                else:
                    self.display.setText(current + button_text)
            else:
                self.display.setText(current + button_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorUI()
    window.show()
    sys.exit(app.exec_())


