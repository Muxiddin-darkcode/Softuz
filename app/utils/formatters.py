import html
from datetime import datetime

def format_size(size_bytes: int) -> str:
    """Format bytes to human readable B, KB, MB, GB."""
    if not size_bytes or size_bytes < 0:
        return "0 B"
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if abs(size_bytes) < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"

def format_os(os_type: str) -> str:
    """Return formatted OS label with icon."""
    mapping = {
        "windows": "💻 Windows",
        "android": "📱 Android (APK)",
        "macos": "🍏 macOS",
        "linux": "🐧 Linux",
        "other": "🌐 Boshqa"
    }
    return mapping.get(os_type.lower(), f"💻 {os_type}")

def escape_text(text: str) -> str:
    """Escape text for HTML parse mode in Telegram."""
    if not text:
        return ""
    return html.escape(str(text))

def format_date(dt: datetime) -> str:
    """Format datetime to YYYY-MM-DD HH:MM."""
    if not dt:
        return "—"
    return dt.strftime("%Y-%m-%d %H:%M")
