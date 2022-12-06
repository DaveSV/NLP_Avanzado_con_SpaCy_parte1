# Predicción de etiquetas gramaticales

import spacy

# Carga el pipeline pequeño de español
nlp = spacy.load("es_core_news_sm")

# Procesa un texto
doc = nlp("Ella comió pizza con sus amigos")

# Itera sobre los tokens
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
