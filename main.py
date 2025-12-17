from task.manager  import TaskManager

def show_menu():
    print("\nメニュー")
    print("1. タスク一覧")
    print("2. タスク追加")
    print("3. タスク完了")
    print("4. タスク削除")
    print("5. タスク全削除")
    print("0. 終了")

def handle_choice(choice, manager):
    if choice == "1":
        manager.list()
    elif choice == "2":
        text = input("追加するタスクを入力してください:")
        manager.add(text)
        manager.list()
    elif choice == "3":
        index = input("完了するタスク番号を入力してください。")
        # 表示対象（今は全タスク、将来は未完了のみ）
        visible = [t for t in manager.tasks] #if not t["done"]]

        if index.isdigit():
            i = int(index) - 1
            if 0 <= i < len(visible):
                task_id = visible[i]["id"]
                manager.complete(task_id)
                manager.list()
            else:
                print("その番号のタスクはありません。")
        else:
            print("番号を入力してください。")
    elif choice == "4":
        index = input("削除するタスクIDを入力してください。（例:1 3 5):")

        try:
            indexes = [int(i) for i in index.split()]
            for i in sorted(indexes, reverse=True):
                manager.delete(i)
            manager.list()
        except ValueError:
            print("番号を正しく入力してください。")

    elif choice == "5":
        yn = input("本当に削除しますか？y/n")
        if yn.lower() == "y":
            manager.clear()

        else:
            print("キャンセルしました。")
        manager.list()

    else:
        print("無効な番号です。")


def main():
    manager = TaskManager("tasks.json")

    while True:
        show_menu()
        choice = input("数字を入力してください：")
        if choice == "0":
            break
        handle_choice(choice, manager)


if __name__ == "__main__":
    main()
