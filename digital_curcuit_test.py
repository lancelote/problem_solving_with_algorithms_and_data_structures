import unittest
from digital_curcuit import LogicGate, BinaryGate, UnaryGate, AndGate, OrGate


class LogicGateTest(unittest.TestCase):

    def setUp(self):
        self.test_logic_gate = LogicGate("Label")

    def test_init_creates_correct_object(self):
        self.assertEqual(self.test_logic_gate.label, "Label")
        self.assertIsNone(self.test_logic_gate.output)

    def test_get_label_returns_correct_result(self):
        self.assertEqual(self.test_logic_gate.get_label(), "Label")

    def test_get_output_returns_correct_result(self):
        self.assertIsNone(self.test_logic_gate.get_output())


class BinaryGateTest(unittest.TestCase):

    def setUp(self):
        self.test_binary_gate = BinaryGate("Label")

    def test_init_creates_correct_object(self):
        self.assertIsNone(self.test_binary_gate.pin_a)
        self.assertIsNone(self.test_binary_gate.pin_b)

    def test_set_pin_a_works_correct(self):
        self.test_binary_gate.set_pin_a(0)
        self.assertEqual(self.test_binary_gate.pin_a, 0)
        self.test_binary_gate.set_pin_a(1)
        self.assertEqual(self.test_binary_gate.pin_a, 1)

    def test_set_pin_b_works_correct(self):
        self.test_binary_gate.set_pin_b(0)
        self.assertEqual(self.test_binary_gate.pin_b, 0)
        self.test_binary_gate.set_pin_b(1)
        self.assertEqual(self.test_binary_gate.pin_b, 1)

    def test_set_pin_a_raises_valuerror_if_not_0_or_1(self):
        self.assertRaises(ValueError, self.test_binary_gate.set_pin_a, "Hello")

    def test_set_pin_b_raises_valuerror_if_not_0_or_1(self):
        self.assertRaises(ValueError, self.test_binary_gate.set_pin_b, "Hello")

    def test_get_pin_a_returns_correct_result(self):
        self.assertIsNone(self.test_binary_gate.get_pin_a())
        self.test_binary_gate.set_pin_a(0)
        self.assertEqual(self.test_binary_gate.get_pin_a(), 0)
        self.test_binary_gate.set_pin_a(1)
        self.assertEqual(self.test_binary_gate.get_pin_a(), 1)

    def test_get_pin_b_returns_correct_result(self):
        self.assertIsNone(self.test_binary_gate.get_pin_b())
        self.test_binary_gate.set_pin_b(0)
        self.assertEqual(self.test_binary_gate.get_pin_b(), 0)
        self.test_binary_gate.set_pin_b(1)
        self.assertEqual(self.test_binary_gate.get_pin_b(), 1)


class UnaryGateTest(unittest.TestCase):

    def setUp(self):
        self.test_unary_gate = UnaryGate("Label")

    def test_init_creates_correct_object(self):
        self.assertIsNone(self.test_unary_gate.pin)

    def test_set_pin_works_correct(self):
        self.test_unary_gate.set_pin(0)
        self.assertEqual(self.test_unary_gate.pin, 0)
        self.test_unary_gate.set_pin(1)
        self.assertEqual(self.test_unary_gate.pin, 1)

    def test_set_pin_raises_valuerror_if_not_0_or_1(self):
        self.assertRaises(ValueError, self.test_unary_gate.set_pin, "Hello")

    def test_get_pin_returns_correct_result(self):
        self.assertIsNone(self.test_unary_gate.get_pin())
        self.test_unary_gate.set_pin(0)
        self.assertEqual(self.test_unary_gate.get_pin(), 0)
        self.test_unary_gate.set_pin(1)
        self.assertEqual(self.test_unary_gate.get_pin(), 1)


class AndGateTest(unittest.TestCase):

    def setUp(self):
        self.test_and_gate = AndGate("Label")

    def test_perform_gate_logic_returns_correct_result(self):
        self.test_and_gate.set_pin_a(0)
        self.test_and_gate.set_pin_b(0)
        self.assertEqual(self.test_and_gate.perform_gate_logic(), 0)
        self.test_and_gate.set_pin_a(1)
        self.assertEqual(self.test_and_gate.perform_gate_logic(), 0)
        self.test_and_gate.set_pin_a(0)
        self.test_and_gate.set_pin_b(1)
        self.assertEqual(self.test_and_gate.perform_gate_logic(), 0)
        self.test_and_gate.set_pin_a(1)
        self.assertEqual(self.test_and_gate.perform_gate_logic(), 1)


class OrGateTest(unittest.TestCase):

    def setUp(self):
        self.test_or_gate = OrGate("Label")

    def test_perform_gate_logic_returns_correct_result(self):
        self.test_or_gate.set_pin_a(0)
        self.test_or_gate.set_pin_b(0)
        self.assertEqual(self.test_or_gate.perform_gate_logic(), 0)
        self.test_or_gate.set_pin_a(1)
        self.assertEqual(self.test_or_gate.perform_gate_logic(), 1)
        self.test_or_gate.set_pin_a(0)
        self.test_or_gate.set_pin_b(1)
        self.assertEqual(self.test_or_gate.perform_gate_logic(), 1)
        self.test_or_gate.set_pin_a(1)
        self.assertEqual(self.test_or_gate.perform_gate_logic(), 1)