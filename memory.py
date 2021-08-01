import sys

bit_processor = 1

memory = (2 ** bit_processor) # memory 1 address length equal to 1 bytes
print(str(memory) + " bytes")

memory_bits = memory * 8
print(str(memory_bits) + ' bits')

max_value = (2 ** memory_bits) - 1
print(str(max_value) + ' decimal')

memory_used = (len(bin(max_value)) - 2) / 8
print(str(memory_used) + ' bytes')

# variabel = max_value
# print(str(int(sys.getsizeof(variabel))) + " bytes")