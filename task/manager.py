from task.storage import load_tasks, save_tasks

class TaskManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.tasks = load_tasks(filepath)

    def _save(self):
        save_tasks(self.tasks, self.filepath)

    def list(self):
        if not self.tasks:
            print("\nタスクがありません")
            return
        print("\n---タスク一覧---\n")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
        print("\n--------------")


    def add(self, text):
        max_id = max((t.get("id", 0) for t in self.tasks), default=0)
        task = {
            "id": max_id + 1,
            "title": text,
            "done": False
        }
        self.tasks.append(task)
        self._save()
        print("\nタスクを追加しました。")

    def complete(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                self._save()
                return



    def delete(self, index):
        i = index -1
        if 0<= i < len(self.tasks):
            delete = self.tasks.pop(i)
            self._save()
            print(f"\n削除したタスクは{index}:{delete}です。")
        else:
            print("\n無効な番号です。")

    def clear(self):
        self.tasks.clear()
        self._save()
        print("\nタスクを全て削除しました。")
