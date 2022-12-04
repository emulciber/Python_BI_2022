# Homework № 2: Files and functions

This script contains functions to filters reads in FASTQ files.

To run the program, you need to call function `main()` with following arguments:
* input_fastq - (required arg) path to input fastq file.
* output\_file\_prefix - path and prefix to output files.
* gc_bounds - filters reads on GC content. Argument takes two percentage values in in parentheses (example `(0, 100)`) or one percentage value as upper bound.
* length_bounds - filter reads on length. Argument takes two values in in parentheses (example `(0, 2**32)`) or one value as upper bound.
* quality_treshold - filter reads on mean value of read quality. Argument takes one Q-value.
* save_filtered - bool argument. If True, filtered reads will saved to a separate file.
