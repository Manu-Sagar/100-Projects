from abc import ABC, abstractmethod

class Task(ABC):
    def __init__(self, task_id, title):
        self.__task_id=task_id
        self.__title=title
        self.__completed=False

    #Encapsulation-Getter
    @property
    def task_id(self):
        return self.__task_id

    @property
    def title(self):
        return self.__title

    @property
    def completed(self):
        return self.__completed

    #Encapsulation-controlled modification
    def complete(self):
        self.__completed=True

    #Abstraction
    @abstractmethod
    def display(self):
        pass

class PersonalTask(Task):
    #Inheritance
    def display(self):
        if self.completed:
            status="Completed"
        else:
            status="Pending"
        print(self.task_id,self.title,"- Personal -",status)

class WorkTask(Task):
    #Inheritance
    def display(self):
        if self.completed:
            status="Completed"
        else:
            status="Pending"
        print(self.task_id,self.title,"- Work -",status)