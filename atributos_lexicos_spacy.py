import spacy
nlp = spacy.load("es_core_news_sm")
nlp = spacy.blank("es")

doc = nlp("Eso cuesta €5.")
print("Índice:   ", [token.i for token in doc])
print("Texto:    ", [token.text for token in doc])

print("is_alpha:", [token.is_alpha for token in doc])
print("is_punct:", [token.is_punct for token in doc])
print("like_num:", [token.like_num for token in doc])
