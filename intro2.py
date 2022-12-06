import spacy
nlp = spacy.blank("es")
doc = nlp("¿Cómo estás?")
print(doc.text)
 
