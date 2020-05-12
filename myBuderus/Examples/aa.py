a = 0x07 ^ 0x00
a = a ^ 0x65
a = a ^ 0x65

# NACHT 15 => 30 -> 0x1C
# NACHT 15 => 30 -> 0x1E
# NACHT 16 => 32 -> 0x20
# NACHT 17 => 34 -> 0x22
a = a ^ 0x65

# TAG - 17 => 34 -> 0x22
# TAG - 18 => 36 -> 0x24
# TAG - 19 => 38 -> 0x26
# TAG - 20 => 40 -> 0x28
a = a ^ 0x28

# N/D/A 00/01/02  65
a = a ^ 0x65

a = a ^ 0x65
a = a ^ 0x10
a = a ^ 0x03
print (hex(a))



