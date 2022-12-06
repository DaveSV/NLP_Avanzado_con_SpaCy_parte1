# Un verbo con el lemma "comer", seguido por un sustantivo.

import spacy

# Importa el Matcher
from spacy.matcher import Matcher

# Carga el modelo y crea un objeto nlp
nlp = spacy.load("es_core_news_sm")

# Inicializa el matcher con el vocabulario compartido
matcher = Matcher(nlp.vocab)

# Añade el patrón al matcher
pattern = [
    {"LEMMA": "comer", "POS": "VERB"},
    {"POS": "NOUN"}
]
matcher.add("VERBO_SUSTANTIVO", [pattern])

# Procesa un texto
doc = nlp("Camila prefería comer sushi. Pero ahora está comiendo pasta.")

# Llama al matcher sobre el doc
matches = matcher(doc)

# Itera sobre los resultados
for match_id, start, end in matches:
    # Obtén el span resultante
    matched_span = doc[start:end]
    print(matched_span.text)

