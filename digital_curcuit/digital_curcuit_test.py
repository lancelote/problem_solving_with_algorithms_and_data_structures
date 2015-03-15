import unittest
from digital_curcuit.digital_curcuit import LogicGate, Connector
from digital_curcuit.digital_curcuit import BinaryGate, UnaryGate
from digital_curcuit.digital_curcuit import AndGate, OrGate, NotGate
from digital_curcuit.digital_curcuit import NandGate, NorGate


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

    def test_set_empty_pin_works_correct(self):
        self.test_binary_gate.set_empty_pin(0)
        self.assertEqual(self.test_binary_gate.get_pin_a(), 0)
        self.test_binary_gate.set_empty_pin(1)
        self.assertEqual(self.test_binary_gate.get_pin_b(), 1)

    def test_set_empty_pin_raises_runtimeerror_if_no_empty_pin(self):
        self.test_binary_gate.set_empty_pin(0)
        self.test_binary_gate.set_empty_pin(1)
        self.assertRaises(RuntimeError, self.test_binary_gate.set_empty_pin, 1)


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

    def test_set_empty_pin_works_correct(self):
        self.test_unary_gate.set_empty_pin(0)
        self.assertEqual(self.test_unary_gate.get_pin(), 0)

    def test_set_empty_pin_raises_runtimeerror_if_no_empty_pin(self):
        self.test_unary_gate.set_empty_pin(0)
        self.assertRaises(RuntimeError, self.test_unary_gate.set_empty_pin, 1)


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


class NotGateTest(unittest.TestCase):

    def setUp(self):
        self.test_not_gate = NotGate("Label")

    def test_perform_gate_logic_returns_correct_result(self):
        self.test_not_gate.set_pin(0)
        self.assertEqual(self.test_not_gate.perform_gate_logic(), 1)
        self.test_not_gate.set_pin(1)
        self.assertEqual(self.test_not_gate.perform_gate_logic(), 0)


class NandGateTest(unittest.TestCase):

    def setUp(self):
        self.test_nand_gate = NandGate("Label")

    def test_perform_gate_logic_returns_correct_result(self):
        self.test_nand_gate.set_pin_a(0)
        self.test_nand_gate.set_pin_b(0)
        self.assertEqual(self.test_nand_gate.perform_gate_logic(), 1)
        self.test_nand_gate.set_pin_a(1)
        self.assertEqual(self.test_nand_gate.perform_gate_logic(), 1)
        self.test_nand_gate.set_pin_b(1)
        self.assertEqual(self.test_nand_gate.perform_gate_logic(), 0)
        self.test_nand_gate.set_pin_a(0)
        self.assertEqual(self.test_nand_gate.perform_gate_logic(), 1)


class NorGateTest(unittest.TestCase):

    def setUp(self):
        self.test_nor_gate = NorGate("Label")

    def test_perform_gate_logic_returns_correct_result(self):
        self.test_nor_gate.set_pin_a(0)
        self.test_nor_gate.set_pin_b(0)
        self.assertEqual(self.test_nor_gate.perform_gate_logic(), 1)
        self.test_nor_gate.set_pin_a(1)
        self.assertEqual(self.test_nor_gate.perform_gate_logic(), 0)
        self.test_nor_gate.set_pin_b(1)
        self.assertEqual(self.test_nor_gate.perform_gate_logic(), 0)
        self.test_nor_gate.set_pin_a(0)
        self.assertEqual(self.test_nor_gate.perform_gate_logic(), 0)


class ConnectorTest(unittest.TestCase):

    def test_init_works_correct(self):
        # NorGate
        g1 = OrGate("G1")
        g1.set_pin_a(1)
        g1.set_pin_b(0)
        g2 = NotGate("G2")
        c1 = Connector(g1, g2)
        self.assertEqual(g2.get_output(), 0)

        # NandGate
        g3 = AndGate("G3")
        g3.set_pin_a(1)
        g3.set_pin_b(0)
        g4 = NotGate("G4")
        c2 = Connector(g3, g4)
        self.assertEqual(g4.get_output(), 1)