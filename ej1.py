from enum import Enum

class EstadoHospitalario(Enum):
    PLANTA = 1
    UCI = 2
    ALTA = 3

class Persona:
    _list_dnis = []

    def __init__(self, dni: str, nombre: str, estado_hospitalario: EstadoHospitalario, edad: int):
        if not isinstance(dni, str) or len(dni) != 9 or not dni.isdigit():
            raise ValueError("DNI debe ser un string de 9 dígitos")
        if dni in Persona._list_dnis:
            raise ValueError("DNI ya existe")
        if not isinstance(nombre, str) or not nombre.isalpha():
            raise ValueError("Nombre debe ser un string")
        if not isinstance(estado_hospitalario, EstadoHospitalario):
            raise ValueError("Estado hospitalario debe ser un valor de Enum")
        if not isinstance(edad, int) or edad < 0 or edad > Persona.max_edad:
            raise ValueError(f"Edad debe ser un valor entre 0 y {Persona.max_edad}")
        self._dni = dni
        self._nombre = nombre
        self._estado_hospitalario = estado_hospitalario
        self._edad = edad
        self._num_dosis = 0
        self._carga_viral = 100 - self._edad
        Persona._list_dnis.append(self._dni)

    @property
    def dni(self):
        return self._dni

    @property
    def nombre(self):
        return self._nombre

    @property
    def estado_hospitalario(self):
        return self._estado_hospitalario

    @property
    def edad(self):
        return self._edad

    @property
    def max_edad(self):
        return 100

    @property
    def list_dnis(self):
        return Persona._list_dnis

    @property
    def max_dosis(self):
        return 3

    @property
    def carga_viral(self):
        return self._carga_viral

    def set_carga_viral(self, carga_viral):
        self._carga_viral = carga_viral

    def __del__(self):
        Persona._list_dnis.remove(self._dni)

    def __str__(self):
        return f"DNI: {self._dni}\nNombre: {self._nombre}\nEdad: {self._edad}\nEstado: {self._estado_hospitalario.name}\nCarga Viral: {self._carga_viral}\nDosis: {self._num_dosis}"

    def vacunado(self):
        if self._estado_hospitalario == EstadoHospitalario.ALTA and self._num_dosis < Persona.max_dosis:
            self._num_dosis += 1
            self._carga_viral += 25
            return 1
        else:
            return -1

    def infectado(self, impacto_covid):
        if self._estado_hospitalario == EstadoHospitalario.ALTA:
            self._carga_viral -= impacto_covid * self._estado_hospitalario.value
            if self._carga_viral < 0:
                self._estado_hospitalario = EstadoHospitalario.UCI
                return -1
            else:
                return self._carga_viral
        else:
            return -1
