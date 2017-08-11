'''

This is an implementation of tail
command in linux.

usage:

tailcommand.py file_name lines_to_read

'''

import sys
import linecache

if len(sys.argv) != 3:
  print "Usage tailcommand.py file_name lines_to_read"
  sys.exit(1)


# filename and number of lines requested
filename, lines = sys.argv[1:]
lines = int(lines)

# count the total number of lines
total_lines = len(open(filename).readlines())

# use linecache module to read the lines
for i in range(total_lines - lines + 1, total_lines+1):
    print linecache.getline(sys.argv[1],i)