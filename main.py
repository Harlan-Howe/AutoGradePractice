# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class AGTester:

    def __init__(self, name):
        self.myName = name

    def __repr__(self):
        return f"Autotest with name {self.myName}"

    def __str__(self):
        return self.__repr__()

    def setName(self, name):
        self.myName = name

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tester = AGTester("Harlan")
    print(tester)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
