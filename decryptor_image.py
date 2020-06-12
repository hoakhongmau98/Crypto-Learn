#!/usr/bin/env python3
import png

f = png.Reader(filename='png/lemur.png')
lemur = f.read()

f = png.Reader(filename='png/flag.png')
flag = f.read()

# the 2nd index in the result tuples is a list of rows
# see pypng docs
flag_lemur = zip(flag[2], lemur[2])

combined_rows = []

for (flag_row, lemur_row) in flag_lemur:
    zipped_row = zip(flag_row, lemur_row)
    combined_rows.append([x ^ y for (x, y) in zipped_row])

with open('lemur_xor_flag.png', 'wb') as f:
    # lemur[0] and lemur[1] are the original width and height
    w = png.Writer(lemur[0], lemur[1], bitdepth=8, greyscale=False)
    w.write(f, combined_rows)