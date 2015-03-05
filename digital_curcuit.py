class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None

    def perform_gate_logic(self):
        pass

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        return self.pin_a

    def get_pin_b(self):
        return self.pin_b

    def set_pin_a(self, n):
        if n != 0 and n != 1:
            raise ValueError("Pin A should be 0 or 1")
        else:
            self.pin_a = n

    def set_pin_b(self, n):
        if n != 0 and n != 1:
            raise ValueError("Pin B should be 0 or 1")
        else:
            self.pin_b = n


class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def get_pin(self):
        return self.pin

    def set_pin(self, n):
        if n != 0 and n != 1:
            raise ValueError("Pin should be 0 or 1")
        else:
            self.pin = n


class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 0 and b == 0:
            return 0
        else:
            return 1
