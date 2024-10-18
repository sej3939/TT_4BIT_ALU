<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

A Kogge-Stone adder is a type of adder that is designed for fast speeds. First, it calculates the propagate and generate signals. The propagate signal determines if a carry bit can propagate through to the next bit, and the generate signal bit determines if there is a carry bit. A combination of these two signals can calculate the carry signal which determines if there is a carry bit that will be added to a bit in the sum. The fast speeds come into play because the carry signal can be calculated in a logarithmic (log2) operation depending on the bit size of the largest input. Finally, the carry signal is combined with the propagate signal by an XOR operation, which combines the signal containing all the carry bits with the propagate signal, which is essentially the sum without any carrying operations. The final output is the sum, and the carry out can also be determined with the most significant bit in the carry signal. Although the Kogge-Stone adder is very fast due to its logarithmic process, it requires a lot of gates for its main signals along with intermediary signals that are used to calculate the carry signal. This makes it useful in cases where speed is paramount, but power and space have more lenient restraints.

## How to test

ui_in[3:0] is addend 1, and ui_in[3:0] is addend 2. ui_out[3:0] is sum, and ui_out[4] is carry_out.

## External hardware

No external hardware needed
