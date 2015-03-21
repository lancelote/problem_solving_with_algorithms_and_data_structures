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

    def set_empty_pin(self, n):
        if self.pin_a is None:
            self.set_pin_a(n)
        elif self.pin_b is None:
            self.set_pin_b(n)
        else:
            raise RuntimeError("There is no empty pin!")


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

    def set_empty_pin(self, n):
        if self.pin is None:
            self.set_pin(n)
        else:
            raise RuntimeError("There is no empty pin!")


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


class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin()
        if a == 0:
            return 1
        else:
            return 0


class XorGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 0 and b == 0:
            return 0
        elif a == 1 and b == 1:
            return 0
        else:
            return 1


class NandGate(AndGate):

    def __init__(self, n):
        AndGate.__init__(self, n)

    def perform_gate_logic(self):
        return int(not AndGate.perform_gate_logic(self))


class NorGate(OrGate):

    def __init__(self, n):
        OrGate.__init__(self, n)

    def perform_gate_logic(self):
        return int(not OrGate.perform_gate_logic(self))


class HalfAdder(XorGate, AndGate):

    # ToDo : restructure architecture to manage multi-output gates

    def __init__(self, n):
        XorGate.__init__(self, n)
        AndGate.__init__(self, n)
        self.xor_gate = XorGate(n)
        self.and_gate = AndGate(n)

    def set_pin_a(self, n):
        if n != 0 and n != 1:
            raise ValueError("Pin A should be 0 or 1")
        else:
            self.xor_gate.pin_a = n
            self.and_gate.pin_a = n

    def set_pin_b(self, n):
        if n != 0 and n != 1:
            raise ValueError("Pin B should be 0 or 1")
        else:
            self.xor_gate.pin_b = n
            self.and_gate.pin_b = n

    def return_gates(self):
        return self.xor_gate, self.and_gate


class FullAdder(XorGate, AndGate, OrGate):

    def __init__(self, n):
        XorGate.__init__(self, n)
        AndGate.__init__(self, n)
        OrGate.__init__(self, n)
        self.xor_gate_1 = XorGate(n)
        self.xor_gate_2 = XorGate(n)
        self.and_gate_1 = AndGate(n)
        self.and_gate_2 = AndGate(n)
        self.or_gate = OrGate(n)

    def set_pin_a(self, n):
        if n != 0 and n != 1:
            raise ValueError("Pin B should be 0 or 1")
        else:
            self.xor_gate_1.pin_a = n
            self.and_gate_2.pin_a = n

    def set_pin_b(self, n):
        if n != 0 and n != 1:
            raise ValueError("Pin B should be 0 or 1")
        else:
            self.xor_gate_1.pin_b = n
            self.and_gate_2.pin_b = n

    def set_pin_c(self, n):
        if n != 0 and n != 1:
            raise ValueError("Pin C should be 0 or 1")
        else:
            self.xor_gate_2.pin_b = n
            self.and_gate_1.pin_b = n

    def return_gates(self):
        self.xor_gate_2.pin_a = self.xor_gate_1.perform_gate_logic()
        self.and_gate_1.pin_a = self.xor_gate_2.pin_a
        self.or_gate.pin_a = self.and_gate_1.perform_gate_logic()
        self.or_gate.pin_b = self.and_gate_2.perform_gate_logic()
        return self.xor_gate_2, self.or_gate


class Connector():
    """
    Used as a connection between gates

    Nor gate:
    >>> g1 = OrGate("G1")
    >>> g1.set_pin_a(1)
    >>> g1.set_pin_b(0)
    >>> g2 = NotGate("G2")
    >>> c1 = Connector(g1, g2)
    >>> g2.get_output()
    0
    """

    def __init__(self, from_gate, to_gate):
        self.f_gate = from_gate
        self.t_gate = to_gate
        self.t_gate.set_empty_pin(self.f_gate.get_output())
