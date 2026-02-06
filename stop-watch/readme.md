# PyQt5 Stopwatch Application

A sleek, modern stopwatch application built with PyQt5 featuring a dark theme and precise millisecond timing.

## Features

- **Precise Timing**: Tracks time down to centiseconds (10ms intervals)
- **Modern UI**: Dark theme with cyan accents and smooth animations
- **Simple Controls**: Start, Stop, and Reset buttons
- **Time Format**: Displays time as HH:MM:SS:CS (Hours:Minutes:Seconds:Centiseconds)
- **Responsive Design**: Button states update based on stopwatch status

## Requirements

- Python 3.x
- PyQt5

## Installation

1. **Install Python** (if not already installed)
   - Download from [python.org](https://www.python.org/downloads/)
   - Ensure Python is added to your system PATH

2. **Install PyQt5**
   ```bash
   pip install PyQt5
   ```

## Usage

1. **Run the application**
   ```bash
   python stopwatch.py
   ```

2. **Controls**
   - **Start**: Begin timing (button becomes disabled while running)
   - **Stop**: Pause the timer
   - **Reset**: Stop the timer and reset to 00:00:00:00

## Code Structure

### Main Components

- **StopWatch Class**: Main widget inheriting from QWidget
  - `time`: QTime object storing elapsed time
  - `time_label`: QLabel displaying formatted time
  - `timer`: QTimer triggering updates every 10ms
  - Start, Stop, Reset buttons for control

### Key Methods

- `initUI()`: Sets up the user interface, layout, and styling
- `start()`: Starts the timer and disables the start button
- `stop()`: Pauses the timer and re-enables the start button
- `reset()`: Stops the timer and resets time to zero
- `format_time()`: Formats QTime object to HH:MM:SS:CS string
- `update_display()`: Updates the display every 10ms

## Styling

The application features a modern dark theme with:
- **Background**: Dark gray (#121212)
- **Buttons**: Lighter gray (#1F1F1F) with hover effects
- **Time Display**: Bright cyan (#00E5FF) for high visibility
- **Interactive Feedback**: Button color changes on hover and press

## Screenshot Description

The stopwatch displays:
- Large cyan time display at the top
- Three horizontally aligned buttons at the bottom
- Clean, minimalist design with rounded corners

## Customization

### Change Colors
Edit the `setStyleSheet()` section in `initUI()`:
```python
QLabel{
    color: #00E5FF;  # Change time display color
}
QPushButton{
    background-color: #1F1F1F;  # Change button color
}
```

### Adjust Timer Precision
Modify the interval in the `start()` method:
```python
self.timer.start(10)  # 10ms = centisecond precision
```

### Change Font
Update the QLabel styling:
```python
QLabel{
    font-size: 60px;  # Adjust size
}
```

## Troubleshooting

### PyQt5 Import Error
```
ModuleNotFoundError: No module named 'PyQt5'
```
**Solution**: Install PyQt5 using `pip install PyQt5`

### Window Doesn't Appear
**Solution**: Ensure you're running the script with a display environment (not headless)

## License

This project is open source and available for educational and personal use.

## Author

Created as a demonstration of PyQt5 GUI programming with QTimer and QTime functionality.

## Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Lap timing functionality
- Save/load times
- Different themes
- Sound notifications
- Keyboard shortcuts

---

**Enjoy timing with precision!** ⏱️