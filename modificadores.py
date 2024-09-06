# Em python o modificador de acesso Private é diferente, utiliza-se dois underscores ('__')
# Por exemplo:

class Pessoa:
    def __init__(self, idade):
        self.__idade = idade
# Nesse exemplo, para definir uma idade com o atributo privado:
    def get_idade(self):
        return self.__idade
    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self.__idade = nova_idade
        else:
            print("idade inválida")

p = Pessoa(25)
print(p.get_idade())
p.set_idade(30)
print(p.get_idade())

# O modificador de acesso para tornar um atributo protegido é ('_'). Por exemplo:
class Peopletwo:
    def __init__(self, idade):
        self._idade = idade

p = (Peopletwo(25))
print(p._idade)

# Podemos acessar diretamente o atributo sem utilizar getter e setter.
p._idade = 30
print(p._idade)

# Para ser público não precisa adicionar nada a classe.

# No python nenhum atributo é realmente privado, enquanto no Java os modificadores
# de acesso definem a visibilidade de membros de uma classe.
 