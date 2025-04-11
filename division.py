class Division:
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    @property
    def calcular_division(self):
        if isinstance(self.operand1, (int, float)) or not (isinstance(self.operand2, (int, float))):
            pass
        # Validar que ambos operandos sean numéricos
        else:
            return "Error: Ambos operandos deben ser numéricos"

        # Validar división entre cero
        if self.operand2 == 0:
            return "Error: No se puede dividir entre cero"

        # Realizar la división
        return self.operand1 / self.operand2
