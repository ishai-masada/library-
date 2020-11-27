education = ['SAT', 'math for dummies', 'english']
story = ['Lord of the Rings', 'Star Wars', 'Twilight']
events = ['War for Independance', 'pony express', 'great music concerts']
people = ['Martin Luther', 'Socrates', 'jason']
advocacy = ['civil rights', 'company policies', 'environmental']
science = ['moon landing', 'neurofeedback', 'biology'] 
lib = [education, story, events, people, advocacy, science]
def library(name, category=lib):
	book = name
	for subject in category:
		if subject == name:
			return subject 
		elif category == subject:
			book = library(name, subject)
	return book
	
print(library('the life and liberties of ishai masada vol 1') )