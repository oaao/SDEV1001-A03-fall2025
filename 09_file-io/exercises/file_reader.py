def read_file(filename):

	lines = []

	with open(filename, 'r') as f:
		for line in f:
			stripped = line.strip()
			if stripped:  # evaluates false if empty string ""
				lines.append(stripped)

	for n, contents in enumerate(lines, start=1):
		print(f"Line {n}: {contents}")
	print(f"Total of {len(lines)} non-empty lines in: {filename}.")

	return lines
