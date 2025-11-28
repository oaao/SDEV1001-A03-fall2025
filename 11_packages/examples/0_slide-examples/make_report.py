from yattag import Doc

from report_config import get_config


def build_report(data):
	doc, tag, text = Doc().tagtext()
	cfg = get_config()

	with tag("html"):
		with tag("body"):
			with tag("h1"):
				text(cfg["title"])
			with tag("p"):
				text(f'- by {cfg["author"]}')

	return doc.getvalue()


if __name__ == "__main__":
	sample_data = [
		"1. create your venv",
		"2. step into your venv",
		"3. install packages from requirements.txt",
		"4. run the program!"
	]
	print(build_report(sample_data))
