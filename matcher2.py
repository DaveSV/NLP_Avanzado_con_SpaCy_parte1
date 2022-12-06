# Para usar el patrón primero importamos el matcher desde spacy.matcher

import spacy

# Importa el Matcher
from spacy.matcher import Matcher

# Carga el modelo y crea un objeto nlp
nlp = spacy.load("es_core_news_sm")

# Inicializa el matcher con el vocabulario compartido
matcher = Matcher(nlp.vocab)

# Añade el patrón al matcher
pattern = [
    {"IS_DIGIT": True},
    {"LOWER": "copa"},
    {"LOWER": "mundial"},
    {"LOWER": "fifa"},
    {"IS_PUNCT": True}
]
matcher.add("FIFA_PATTERN", [pattern])

# Procesa un texto
doc = nlp("2014 Copa Mundial FIFA: Alemania ganó!")

# Llama al matcher sobre el doc
matches = matcher(doc)

# Itera sobre los resultados
for match_id, start, end in matches:
    # Obtén el span resultante
    matched_span = doc[start:end]
    print(matched_span.text)

