import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.clock import Clock

@cocotb.test()
async def test_tt_um_ALU(dut):
    # Clock generation
    cocotb.start_soon(Clock(dut.clk, 10, units='ns').start())

    # Initialize Inputs
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.ena.value = 1
    dut.rst_n.value = 0
    ENC_KEY = 0xAB

    # Wait for global reset
    await Timer(50, units='ns')
    dut.rst_n.value = 1

    # Helper function to display results
    def display_result(op_name):
        print(f"{op_name}: result = {dut.uo_out.value}, uio_out = {dut.uio_out.value}")

    opcode = [i for i in range(9)]
    input_val = [i for i in range(16)]

    for opcode in range(9):
        dut.uio_in.value = opcode
        for val1 in range(16):
            dut.ui_in.value = val1 << 4
            for val2 in range(16):
                dut.ui_in.value &= 0xF0
                dut.ui_in.value |= val2
                await Timer(50, units='ns')
                match opcode:
                    case 0: # ADD
                        display_result("ADD")
                        assert dut.uo_out.value == val1 + val2
                    case 1: # SUB
                        display_result("SUB")
                        assert dut.uo_out.value == val1 - val2
                    case 2: # MUL
                        display_result("MUL")
                        assert dut.uo_out.value == val1 * val2
                    case 3: # DIV
                        display_result("DIV")
                        assert dut.uo_out.value == (val1 % val2) << 4 | (val1 // val2)
                    case 4: # AND
                        display_result("AND")
                        assert dut.uo_out.value == val1 & val2
                    case 5: # OR
                        display_result("OR")
                        assert dut.uo_out.value == val1 | val2
                    case 6: # XOR
                        display_result("XOR")
                        assert dut.uo_out.value == val1 & val2
                    case 7: # NOT
                        display_result("NOT")
                        assert dut.uo_out.value == ~val1
                    case 8: # ENC
                        display_result("ENC")
                        assert dut.uo_out.value == (val1 << 4 | val2) ^ ENC_KEY
