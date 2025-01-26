/******************************************************************************/
/*                                                                            */
/* Utility for a simple up counter                                            */
/*                                                                            */
/******************************************************************************/

`timescale 1ns/1ns

module counter #(parameter  START = 0, // counter will start here
                 parameter  STOP = 10, // counter will rollover when count is
                                       // greater than this
                 parameter  STEP = 1,  // how much count should increase each
                                       // clock cycle
                 localparam BITS = $clog2(STOP - START))

                (input                  clk,       // clk for counter to run on
                 input                  reset,     // will reset count to START
                 input                  enable,    // will only count when enable high
                 output reg  [BITS-1:0] count,     // current value of counter
                 output reg             rollover); // high if just rolled over

    wire [BITS-1:0] count_n;
    wire            rollover_n;

    assign rollover_n = count + STEP > STOP;
    assign count_n = rollover_n ? START : count + STEP;

    always @(posedge clk)
        if (reset) begin
            count <= START;
            rollover <= 0;
        end
        else if (enable) begin
            count <= count_n;
            rollover <= rollover_n;
        end

endmodule // counter
