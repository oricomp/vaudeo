import cocotb
from cocotb.triggers import FallingEdge, Timer
from cocotb.clock import Clock


@cocotb.test()
async def counter_test(dut):
    dut.enable.value = 1
    dut.reset.value = 0
    await cocotb.start(Clock(dut.clk, 1, units="ns").start())

    await Timer(5, units="ns")

    dut._log.info("counter value: %s", dut.count.value)
    assert True
