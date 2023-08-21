from dataclasses import dataclass

todos = []


@dataclass
class Item:
    title: str
    isCompleted: bool = False


def add(title):
    title = title.replace('b', 'bbb').replace('B', 'Bbb')
    todos.append(Item(title))


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted
