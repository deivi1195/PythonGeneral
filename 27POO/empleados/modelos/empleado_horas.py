from modelos.empleado import Empleado

class EmpleadoHoras(Empleado):
    def __init__(self, documento, nombre_completo, correo_electronico, especialidad, numero_horas, valor_horas):
        super().__init__(documento, nombre_completo, correo_electronico, especialidad)
        
        self.numero_horas = numero_horas
        self.valor_horas = valor_horas
        
    def calcular_salario(self):
        total = super().calcular_salario() + self.numero_horas * self.valor_horas

        return total




