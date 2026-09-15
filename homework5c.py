import sys
from pathlib import Path


def parse_log_line(line: str) -> dict:
    parts = line.strip().split(" ", 3)

    if len(parts) != 4:
        raise ValueError(f"Invalid log line format: {line.strip()}")

    date, time, level, message = parts

    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message,
    }


def load_logs(file_path: str) -> list:
    logs = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                try:
                    logs.append(parse_log_line(line))
                except ValueError as error:
                    print(f"Skipped invalid line: {error}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

    except OSError as error:
        print(f"Error reading file: {error}")
        return []

    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()

    return list(
        filter(
            lambda log: log["level"] == level,
            logs,
        )
    )


def count_logs_by_level(logs: list) -> dict:
    counts = {}

    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1

    return counts


def display_log_counts(counts: dict) -> None:
    print("Рівень логування | Кількість")
    print("-----------------|----------")

    for level in ["INFO", "DEBUG", "ERROR", "WARNING"]:
        print(f"{level:<16} | {counts.get(level, 0)}")


def display_logs(logs: list, level: str) -> None:
    filtered_logs = filter_logs_by_level(logs, level)

    if not filtered_logs:
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        print("Записів не знайдено.")
        return

    print(f"\nДеталі логів для рівня '{level.upper()}':")

    for log in filtered_logs:
        print(
            f"{log['date']} {log['time']} - {log['message']}"
        )


def main():
    if len(sys.argv) < 2:
        print("Usage: python homework5c.py <log_file> [level]")
        return

    file_path = sys.argv[1]

    if not Path(file_path).exists():
        print(f"File not found: {file_path}")
        return

    logs = load_logs(file_path)

    if not logs:
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) >= 3:
        level = sys.argv[2]
        display_logs(logs, level)


if __name__ == "__main__":
    main()