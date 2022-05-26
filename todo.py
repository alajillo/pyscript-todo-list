from js import document, console
from pyodide import create_proxy


class TodoList:
    def __init__(self, parent_element):
        self.parent_element = parent_element
        self.current_id = 0
        self.__init__input()
        self.__init__button()
        self.__init__list()
        pass

    def __init__button(self):
        self.button_element = document.createElement("button")
        self.button_element.innerText = "add todo"
        self.parent_element.append(self.button_element)
        add_todo = create_proxy(self.add_todo)
        self.button_element.addEventListener("click", add_todo)
        pass

    def __init__input(self):
        self.input_element = document.createElement("input")
        self.parent_element.append(self.input_element)
        pass

    def __init__list(self):
        self.list_element = document.createElement("ul")
        self.parent_element.append(self.list_element)
        pass

    def add_todo(self, event):
        text = self.input_element.value
        new_item = Item(text, self.current_id)
        self.current_id = self.current_id + 1
        new_item.on_remove(self.remove_todo)
        self.list_element.append(new_item.item)
        pass

    def remove_todo(self, event):
        target_element = event.target.closest("li")
        self.list_element.removeChild(target_element)
        pass


class Item:
    def __init__(self, text, id):
        self.item = document.createElement("li")
        self.item.setAttribute("data-id", id)
        self.item.innerText = text
        self.remove_button = document.createElement("button")
        self.remove_button.innerText = "remove"
        self.item.append(self.remove_button)
        pass

    def on_remove(self, cb):
        on_remove_proxy = create_proxy(cb)
        self.remove_button.addEventListener("click", on_remove_proxy)
        pass


app = document.getElementById("app")

TodoList(app)
