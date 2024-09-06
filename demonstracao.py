class Student:
    _name = None
    _matricula = None
    _ramo = None

    def __init__(self, name, matricula, ramo):
        self._name = name
        self._matricula = matricula
        self._ramo = ramo
    
    def _saida(self):
        print("Matrícula: ", self._matricula)
        print("Ramo: ", self._ramo)


class Info:

    def __init__(self, name, matricula, ramo):
        self._student = Student(name, matricula, ramo)

    def display_details(self):
        print("Nome: ", self._student._name)
        self._student._saida()
    
obj = Info("Beatriz", "2004529", "Tecnologia")
obj.display_details()