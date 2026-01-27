from pathlib import Path
from datetime import datetime


def main() -> None:
    """Write the current local time to outtime.txt."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Path("outtime.txt").write_text(f"{now}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
