# Importação da biblioteca para uso de métodos abstratos
from abc import ABC, abstractmethod

class Department:
# Instanciando nome e código dos departamentos
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    ''' Utilizando a o parâmetro Abstracte Base Classes para tornar
    a classe Employee abstrata e impedir, dessa forma, que ela
    seja instanciada diretamente e, consequentemente, protegendo-a'''
    
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

# Classe abstrata, métodos abstratos também
    @abstractmethod
    def calc_bonus(self):
        pass

    @abstractmethod
    def get_hours(self):
        pass


class Manager(Employee):
# Uso de 'dunder' nas variáveis para torná-las atributos privados
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)


    def calc_bonus(self):
        return self.salary * 0.15

    def get_hours(self):
        return 8

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, department):
        self.__departament.name = department


class Seller(Employee):

    '''Utilizando a classe Employee como parâmetro da
    Classe Seller, objetivando tornar Seller filha de Employee,
    para que a mesma herde os atributos de Employee'''

    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0
    
    def calc_bonus(self):
        return self.get_sales() * 0.15
    
    def get_sales(self):
        return self.__sales

    def put_sales(self, sale):
        self.__sales += sale

    def get_hours(self):
        return 8
    
    def set_department(self, department):
        self.__departament.name = department

    def get_departament(self):
        return self.__departament.name
