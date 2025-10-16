"""
SmartWeather Pro - Modern Weather Application
"""
import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor
from PySide6.QtCore import Qt
from gui.main_window import MainWindow


def create_fallback_icon():
    """Create a simple fallback icon if custom icon is not found"""
    pixmap = QPixmap(32, 32)
    pixmap.fill(Qt.transparent)

    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)

    # Simple weather icon design
    painter.setBrush(QColor(66, 135, 245))
    painter.setPen(Qt.NoPen)
    painter.drawRoundedRect(0, 0, 32, 32, 6, 6)

    painter.setBrush(QColor(255, 255, 255))
    painter.drawEllipse(6, 8, 8, 8)
    painter.drawEllipse(12, 5, 10, 10)
    painter.drawEllipse(20, 8, 6, 6)

    painter.end()
    return QIcon(pixmap)


def get_application_icon():
    """Get the application icon from the specified path"""
    # Possible paths for the icon
    possible_paths = [
        # Main icon path where user placed it
        "gui/icons/weather_icon.ico",
        # Alternative paths
        "./gui/icons/weather_icon.ico",
        "weather_icon.ico",
        "./weather_icon.ico",
        "assets/icons/weather_icon.ico",
        "./assets/icons/weather_icon.ico",
    ]

    # Check each path
    for icon_path in possible_paths:
        if os.path.exists(icon_path):
            try:
                app_icon = QIcon(icon_path)
                # Check if the icon is valid
                if not app_icon.isNull():
                    print(f"✅ Application icon loaded from: {icon_path}")
                    return app_icon
                else:
                    print(f"⚠️ Icon at {icon_path} is not valid")
            except Exception as e:
                print(f"⚠️ Error loading icon from {icon_path}: {e}")

    # If no icon found, use fallback icon
    print("🔷 Using fallback icon")
    return create_fallback_icon()


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("SmartWeather Pro")
    app.setApplicationVersion("2.0")

    # Set application icon
    app_icon = get_application_icon()
    app.setWindowIcon(app_icon)

    API_KEY = "97b9cc3c6fdb4548be2152202251410"

    if not API_KEY:
        print("❌ Please set a valid WeatherAPI key")
        return 1

    window = MainWindow(API_KEY)

    # Set icon for main window
    window.setWindowIcon(app_icon)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
