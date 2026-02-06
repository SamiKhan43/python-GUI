# Calculator

A modern, sleek calculator application built with PyQt5 featuring a dark theme and intuitive interface.

## Features

- **Basic Arithmetic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Advanced Functions**:
  - Percentage calculation (%)
  - Sign toggle (±)
  - Backspace (←)
  - Clear all (AC)
- **Repeat Calculation**: Press = multiple times to repeat the last operation
- **Modern Dark UI**: Professional dark theme with orange operator buttons
- **Responsive Design**: Fixed 380x600 window size for optimal usability

## Screenshots

The calculator features:
- Dark background (#121212)
- Large, easy-to-read display
- Color-coded buttons:
  - Orange for operators (+, -, *, /)
  - Gray for functions (AC, ←, %, ±)
  - Dark gray for numbers
  - Hover and press effects for better UX

## Requirements

- Python 3.6+
- PyQt5

## Installation

1. Clone this repository or download the calculator file:
```bash
git clone <repository-url>
cd calculator
```

2. Install PyQt5:
```bash
pip install PyQt5
```

## Usage

Run the calculator:
```bash
python calculator.py
```

### Button Functions

| Button | Function |
|--------|----------|
| 0-9 | Number input |
| . | Decimal point |
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| = | Calculate result / Repeat last operation |
| AC | Clear all |
| ← | Backspace (delete last digit) |
| % | Convert to percentage (divide by 100) |
| ± | Toggle positive/negative |

### Tips

- **Repeat Calculations**: After calculating a result, press = again to repeat the last operation
  - Example: `5 + 3 = 8`, press = again → `8 + 3 = 11`
- **Chain Operations**: You can chain multiple operations together
  - Example: `5 + 3 * 2 =` will evaluate as `11` (left to right)
- **Error Handling**: Invalid operations will display "Error"

## Code Structure

```
calculator.py
├── CalculatorUI (QWidget)
│   ├── __init__(): Initialize calculator
│   ├── initUI(): Setup UI components
│   ├── apply_styles(): Apply dark theme styling
│   └── on_button_click(): Handle button interactions
```

### Key Components

- **Display**: Read-only QLineEdit showing current input/result
- **Button Grid**: 5x4 grid layout with all calculator buttons
- **Styling**: Custom CSS-like stylesheet for dark theme
- **State Management**: Tracks last operator and operand for repeat calculations

## Customization

### Change Theme Colors

Edit the `apply_styles()` method to customize colors:

```python
# Background color
QWidget { background-color: #121212; }

# Operator button color
QPushButton#operator { background-color: #ff9500; }

# Display color
QLineEdit { background-color: #1e1e1e; color: #ffffff; }
```

### Adjust Window Size

Modify in `__init__()`:
```python
self.setFixedSize(380, 600)  # Width, Height
```

### Change Button Size

Modify in `initUI()`:
```python
button.setFixedSize(70, 70)  # Width, Height
```

## Known Limitations

- Uses Python's `eval()` for calculations (evaluates expressions left to right)
- No keyboard input support (mouse/touch only)
- No calculation history
- Limited to basic arithmetic operations

## Future Enhancements

Possible improvements:
- [ ] Add keyboard support
- [ ] Implement calculation history
- [ ] Add scientific calculator mode
- [ ] Support for parentheses
- [ ] Memory functions (M+, M-, MR, MC)
- [ ] Theme customization options

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have suggestions, please open an issue in the repository.

---

**Made with ❤️ using PyQt5**