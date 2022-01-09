import re


def rearange_name(name):
	result = re.search(r"^([\w .]*), ([\w .]*)$", name)
	if result is None:
		return ""
	return f"full name: {result[2]} {result[1]}"
