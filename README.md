# Quotefuck - a ludicrous programming language

Quotefuck is an esoteric programming language derived from Brainfuck. It shares the same instruction set, but with a different syntax, using only quote-like characters (“”‘’"'`´).

The language was created to show the slight but important differences of the different quote-like characters. The characters are pair-wise well suited for logical syntax but are hard to type on a standard keyboard. They can be hard to distinguish when printed in a small font, such as in a text editor, and when used together they produce an unreadable garbled mess.

## Background

Historical reasons has caused some confusion in the usage of quotation character on computers. Mechanical typewriters used only straight quotation marks to save space. The ASCII standard did not contain an acute accent (´) and early X Window System fonts showed apostrophe (') and grave accent (\`) as mutually symmetric single quotation marks. This lead to the combination of these characters to be used to \`quote text' and this syntax is still used in some contexts. Another example of odd syntax is the use of grave accent for command substitution in bash scripts and for code syntax in Markdown.

## Instructions

The instruction set is fairly straight forward with mutually symmetric characters being used for pointer and value operations and for loops. The straight quotation mark and apostrophe are used for I/O.

| Instruction | Character name | Unicode number | Description | Brainfuck equivalent |
|-------------|----------------|----------------|-------------|----------------------|
| “ | Left double quotation mark | U+201C | Decrement pointer | < |
| ” | Right double quotation mark | U+201D | Increment pointer | > |
| ‘ | Left Single Quotation Mark | U+2018 | Decrement value at pointer | - |
| ’ | Right Single Quotation Mark | U+2019 | Increment value at pointer | + |
| " | Quotation Mark | U+0022 | Print character | . |
| ' | Apostrophe | U+0027 | Input character | , |
| ` | Grave Accent | U+0060 | Start loop | [ |
| ´ | Acute Accent | U+00B4 | End loop | ] |

## Example

Using the instruction set above, the classical Hello world program becomes as simple as

    ’’’’’’’’`”’’’’`”’’”’’’”’’’”’““““‘´”’”’”‘””’`“´“‘´””"”‘‘‘"’’’’’’’""’’’"””"“‘"“"’’’"‘‘‘‘‘‘"‘‘‘‘‘‘‘‘"””’"”’’"

Running this program yields the output

    # ./qf.py hello.qf
    Hello World!

## Additional features

This interpreter can also import Brainfuck code and convert it to Quotefuck. A source file containing the Brainfuck addition program (`[->+<]`) can be converted to Quotefuck with the command

    # ./qf.py --bf --print_code add.bf
    `‘”’“´

## Implementation details

This interpreter is using a list of integers as data memory and does not do any overflow checks. This means that it follows the standard Python rules and is not compatible with the standard Brainfuck implementation. The data pointer can become negative and then wraps around to point at the end of the memory.

The default memory size is 256 bytes but it can be changed using the `--memory-size` flag.

Each memory cell is a standard int and can become very large (2^31 or 2^63) before it wraps around.

## Syntax highlighting

Why would you want syntax highlighting for a language that was designed to be unreadable?

## References

* https://www.cl.cam.ac.uk/~mgk25/ucs/quotes.html
