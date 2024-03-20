"""
PYSOUNDS
funcs:
fanfare -- plays simple fanfare
about -- returns information about your release
main:
starts fanfare with default values
"""
def about():
    """
    Returns information about your release and other projects by LK
    """
    return {"Version":(1, 0, 1), "Author":"Leander Kafemann", date:"19.3.2024", recommend:("Büro by LK", "pyimager by LK", "pycols by LK", "naturalsize by LK"), feedbackTo: "leander@kafemann.berlin"}

import winsound, time

def fanfare(freq: int = 1000):
	"""
	Starts classical da-da-da-dim fanfare with given freq..
	"""
	for i in range(3):
		winsound.Beep(freq, 250)
		time.sleep(0.05)
	winsound.Beep(int(freq*1.35), 800)

if __name__ == "__main__":
	fanfare()