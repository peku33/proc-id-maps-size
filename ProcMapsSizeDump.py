###################################################
#
# Scans /proc/id/maps file and adds two columns
# - Size in bytes
# - Size in human readable form (B, KB, MB, GB)
# Then passes it to output
#
# Usage: python ProcMapsSizeDump.py < /proc/id/maps
#
###################################################

# Function converting large number to human-readable
# 1024 -> 1.00Kb
# 1024 * 1024 -> 1.00Mb
# etc
def human_format(number):
    formats = ['b', 'Kb', 'Mb', 'Gb']
    exponent = 0

    while(number >= 1024):
        exponent += 1;
        number /= 1024

    return "%.2f%s" % (number, formats[exponent])

# Iterate over standard input until we got EOF, then break
while(True):

    try:
        map_line = input()
    except EOFError:
        break
	
	# Skip empty lines
    if(map_line == ''):
        continue
		
	# Split line by spaces
    map_line_entries = map_line.split()
	
	# First token contains memory range aaaaaaa-bbbbbbbbb, extract a (start), b (end)
    map_line_size_entries = map_line_entries[0].split("-")
	
	# Convert Hex to Dec
    map_line_size_start = int(map_line_size_entries[0], 16)
    map_line_size_end = int(map_line_size_entries[1], 16)
	
	# Calculate size
    map_line_size = map_line_size_end - map_line_size_start
	# Make it human readable
    map_line_size_str = human_format(map_line_size)
	
	# Insert results to original maps entry
    map_line_entries.insert(1, str(map_line_size).rjust(16, ' '))
    map_line_entries.insert(2, map_line_size_str.rjust(16, ' '))
	
	# Make it string again
    map_line = " ".join(map_line_entries)
	
	# Out
    print(map_line)
