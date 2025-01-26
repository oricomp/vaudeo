import cocotb
from cocotb.triggers import FallingEdge, Timer
from cocotb.clock import Clock


START = 0
STOP = 10
STEP = 1


async def reset(dut):
    """Resets the device and enables it"""
    dut.reset.value = 1
    await Timer(2, units="ns")
    dut.enable.value = 1
    dut.reset.value = 0


def assert_defaults(dut):
    """Asserts that the default parameters are the same"""
    assert dut.START.value == START
    assert dut.STOP.value == STOP
    assert dut.STEP.value == STEP


@cocotb.test()
async def counter_counts_test(dut):
    """Test that the counter properly counts"""
    assert_defaults(dut)
    await cocotb.start(Clock(dut.clk, 1, units="ns").start())
    await reset(dut)

    assert (STOP - START) // STEP >= 5, "Test will not work otherwise"
    await Timer(5, units="ns")
    assert dut.count.value == 5, "5 ticks after reset"


@cocotb.test()
async def counter_resets_test(dut):
    """Test that the counter properly resets"""
    assert_defaults(dut)
    await cocotb.start(Clock(dut.clk, 1, units="ns").start())
    await reset(dut)

    count = (STOP - START) // STEP // 2
    await Timer(count, units="ns")
    assert dut.count.value == count

    dut.reset.value = 1
    await Timer(5, units="ns")
    assert dut.count.value == 0, "Counter is in reset"


@cocotb.test()
async def counter_rolls_over_test(dut):
    """Test that the counter properly rolls over"""
    assert_defaults(dut)
    await cocotb.start(Clock(dut.clk, 1, units="ns").start())
    await reset(dut)

    count = (STOP - START) // STEP
    await Timer(count, units="ns")
    assert dut.count.value == count, "should be about to roll over"

    await Timer(1, units="ns")
    assert dut.count.value == START, "should have just rolled over"
    assert dut.rollover.value == 1, "should have just rolled over"


@cocotb.test()
async def counter_enable_test(dut):
    """Test that the counter properly handles enable"""
    assert_defaults(dut)
    await cocotb.start(Clock(dut.clk, 1, units="ns").start())
    await reset(dut)

    count = (STOP - START) // STEP // 2
    await Timer(count, units="ns")
    assert dut.count.value == count

    dut.enable.value = 0
    await Timer(10, units="ns")
    assert dut.count.value == count, "counter not enabled"

    dut.enable.value = 1
    await Timer(1, units="ns")
    assert dut.count.value == count + STEP, "should have increased once"
