import abc


# Abstract class for Subject which is being observed for changes
class Subject(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_observer(self, observer):
        pass

    @abc.abstractmethod
    def remove_observer(self, observer):
        pass

    @abc.abstractmethod
    def do_notify(self):
        pass


# Abstract class for Observer which is observing the subject
class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_update(self, name):
        pass


class ImplementSub(Subject):
    def __init__(self, name):
        self.observers = []
        self.name = name

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def do_notify(self):
        for observer in self.observers:
            observer.do_update(self.name)

    def set_name(self, name):
        print("Sending name as : %s" % name)
        self.name = name
        self.do_notify()


class Observer1(Observer):
    def do_update(self, name):
        print("Observer 1 just found out name of customer 1 is %s" % name)


class Observer2(Observer):
    def do_update(self, name):
        print("Observer 2 just found out name of customer 2 is %s" % name)


if __name__ == '__main__':
    obj = ImplementSub(33)

    ob1 = Observer1()
    ob2 = Observer2()
    obj.add_observer(ob1)
    obj.add_observer(ob2)

    obj.set_name("Mansi")
    obj.remove_observer(ob1)
    obj.set_name("Ann")
