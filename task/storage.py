import json
from pathlib import Path

def load_tasks(filepath):
        path = Path(filepath)

        try:
            text = path.read_text(encoding="utf-8")
            return json.loads(text)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

def save_tasks(tasks, filepath):
    path = Path(filepath)
    path.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )