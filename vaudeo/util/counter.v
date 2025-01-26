/******************************************************************************/
/*                                                                            */
/* Utility for a simple counter                                               */
/*                                                                            */
/******************************************************************************/

`timescale 1ns/1ns

module counter #(parameter  START = 0,
                 parameter  STOP = 10,
                 parameter  STEP = 1,
                 localparam BITS = STEP > 0 ? $clog2(STOP - START)
                                            : $clog2(START - STOP))

                (input                  clk,       // clk for counter to run on
                 input                  reset,     // will reset count to START
                 input                  enable,    // will only count when enable high
                 output reg  [BITS-1:0] count,     // current value of counter
                 output wire            rollover); // high if next clk will cause rollover

    wire [BITS-1:0] count_n;

    assign rollover = count + STEP > STOP;
    assign count_n = rollover ? START : count + STEP;

    always @(posedge clk) begin
        if (reset) count <= START;
        else if (enable) count <= count_n;
    end

endmodule // counter
