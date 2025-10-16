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
    # مسیرهای ممکن برای آیکون
    possible_paths = [
        # مسیر اصلی آیکون که کاربر قرار داده
        "gui/icons/weather_icon.ico",
        # مسیرهای جایگزین
        "./gui/icons/weather_icon.ico",
        "weather_icon.ico",
        "./weather_icon.ico",
        "assets/icons/weather_icon.ico",
        "./assets/icons/weather_icon.ico",
    ]

    # بررسی هر مسیر
    for icon_path in possible_paths:
        if os.path.exists(icon_path):
            try:
                app_icon = QIcon(icon_path)
                # بررسی می‌کنیم که آیکون معتبر باشد
                if not app_icon.isNull():
                    print(f"✅ آیکون برنامه از مسیر زیر بارگذاری شد: {icon_path}")
                    return app_icon
                else:
                    print(f"⚠️  آیکون در مسیر {icon_path} معتبر نیست")
            except Exception as e:
                print(f"⚠️  خطا در بارگذاری آیکون از {icon_path}: {e}")

    # اگر هیچ آیکونی پیدا نشد، از آیکون پیش‌فرض استفاده کن
    print("🔷 از آیکون پیش‌فرض استفاده می‌شود")
    return create_fallback_icon()


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("SmartWeather Pro")
    app.setApplicationVersion("2.0")

    # تنظیم آیکون برنامه
    app_icon = get_application_icon()
    app.setWindowIcon(app_icon)

    API_KEY = "97b9cc3c6fdb4548be2152202251410"

    if not API_KEY:
        print("❌ Please set a valid WeatherAPI key")
        return 1

    window = MainWindow(API_KEY)

    # تنظیم آیکون برای پنجره اصلی
    window.setWindowIcon(app_icon)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()