# Open the input file
with open('dumplog-input-file.txt', 'r') as infile:
  # Open the output file
  with open('dumplog-output-file.txt', 'w') as outfile:
    # Iterate through each line of the input file
    for line in infile:
      # Check if the line starts with 'S'
      if line.startswith('S'):
        # If it does, write the line to the output file
        outfile.write(line)
