class Notebook:
    todos = ["Clean my room", "Make my bed", "Go to school", "Do school homework"]

    @staticmethod
    def check_pos(pos):
        if len(Notebook.todos) == 0:
            raise Exception("No more todos!")
        elif pos >= len(Notebook.todos) or pos < 0:
            raise Exception("No such item number!")

    @staticmethod
    def add_todo(content):
        Notebook.todos.append(content)

    @staticmethod
    def remove_todo(pos):
        Notebook.check_pos(pos)

        Notebook.todos.pop(pos)

    @staticmethod
    def edit_todo(pos, content):
        Notebook.check_pos(pos)

        Notebook.todos[pos] = content

    @staticmethod
    def remove_all():
        Notebook.todos.clear()


Notebook.add_todo("Go to bed")
Notebook.remove_todo(0)
Notebook.edit_todo(0, "Get up from bed")
Notebook.remove_all()