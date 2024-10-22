"""
PYSOUNDS
funcs:
fanfare -- plays simple fanfare basing on frequency
fanfare_note -- plays simple fanfare basing on note
about -- returns information about your release
main:
starts fanfare with default values
"""
def about():
    """
    Returns information about your release and other projects by LK
    """
    return {"Version":(1, 1, 1), "Author":"Leander Kafemann", "date":"22.10.2024", "recommend":("Büro by LK", "pyimager by LK", "naturalsize by LK"), "feedbackTo": "leander@kafemann.berlin"}

import winsound, time

starting = 261.63 #Hz
n_dict = {"c": 1, "cis": 1.06, "d": 1.12, "dis": 1.19, "e": 1.26, "f": 1.33, "fis": 1.41, "g": 1.5, "gis": 1.59, "a": 1.68, "ais": 1.78, "h": 1.89} #note: hz at oct 1
"""
starting -- starting freq of c 1
n_dict -- translating dictionary from note to multiplicator of starting
"""

def fanfare(freq: int = 1000):
	"""
	Starts classical da-da-da-dim fanfare with given freq..
	'Distance' between notes is NOT evaluated individually,
	but the most accurate starting at 1000 Hz.
	"""
	for _ in range(3):
		winsound.Beep(freq, 250)
		time.sleep(0.05)
	winsound.Beep(int(freq*1.35), 800)
	
def fanfare_note(start: str = "g", end: str = "c", oct_: int = 1):
	"""
	Starts classical da-da-da-dim fanfare in given octave
	with given start (dadada) and end (dim) notes.
	Requires you to give valid notes.
	"""
	for _ in range(3):
		winsound.Beep(int(n_dict[start]*oct_*starting), 250)
		time.sleep(0.05)
	winsound.Beep(int(n_dict[end]*oct_*starting), 800)

if __name__ == "__main__":
	fanfare()