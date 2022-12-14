from main import truncate_number

assert truncate_number(-5) == 0
assert truncate_number(-5.0) == 0.0
assert truncate_number(.5) == 0.5
assert truncate_number(0) == 0
assert truncate_number(0.0) == 0.0
assert truncate_number(0.001) == 0.001
assert truncate_number(0.1) == 0.1
assert truncate_number(0.28) == 0.28
assert truncate_number(0.32) == 0.32
assert truncate_number(0.345) == 0.345
assert truncate_number(0.49) == 0.49
assert truncate_number(0.50) == 0.5
assert truncate_number(0.999) == 0.999
assert truncate_number(1) == 0
assert truncate_number(1.0) == 0.0
assert truncate_number(1.5) == 0.5
assert truncate_number(1.54) == .54
assert truncate_number(1.99) == .99
assert truncate_number(1.99) == 0.99
assert truncate_number(1.9999) == 0.9999
assert truncate_number(10.0) == 0
assert truncate_number(10.0) == 0.0
assert truncate_number(2) == 0
assert truncate_number(2.0) == 0.0
assert truncate_number(28) == 0.0
assert truncate_number(5) == 0
assert truncate_number(5.0) == 0.0
assert truncate_number(5.5) == 0.5
assert truncate_number(7.5) == 0.5