<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

4-bit ALU with ADD, SUB, MUL, DIV, AND, OR, XOR, NOT, and ENC instructions. Addition (ADD) and subtraction (SUB) results in a 4-bit output. Multiplicatoin (MUL) results in an 8-bit output. Division (DIV) results in an 8-bit output, with the most significant four bits being the remainder and the least significant four bits being the quotient. AND, OR, XOR results in a 4-bit output. NOT results in a 4-bit output using only the first input. Encryption (ENC) results in a 8-bit output that is the XOR of 0xAB and the concatenation of the two inputs.

## How to test

ui_in[3:0] is input 1, and ui_in[3:0] is input 2. ui_out[8:0] is result, uio_in[3:0] is opcode, uio_out[6] is carry_out, and iuo_out[7] is overflow.

## External hardware

No external hardware needed
