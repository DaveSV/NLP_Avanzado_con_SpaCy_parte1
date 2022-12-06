# Los operadores y cuantificadores te permiten definir con qué frecuencia un token debe ser encontrado. Pueden ser añadidos con el key "OP".

import spacy

# Importa el Matcher
from spacy.matcher import Matcher

# Carga el modelo y crea un objeto nlp
nlp = spacy.load("es_core_news_sm")

# Inicializa el matcher con el vocabulario compartido
matcher = Matcher(nlp.vocab)

# Añade el patrón al matcher
pattern = [
    {"LEMMA": "comprar"},
    {"POS": "DET", "OP": "?"},  # opcional: encuentra 0 o 1 ocurrencias
    {"POS": "NOUN"}
]
matcher.add("OPERADOR_CUANTIFICADOR", [pattern])

# Procesa un texto
doc = nlp("Me compré un smartphone. Ahora le estoy comprando aplicaciones.")

# Llama al matcher sobre el doc
matches = matcher(doc)

# Itera sobre los resultados
for match_id, start, end in matches:
    # Obtén el span resultante
    matched_span = doc[start:end]
    print(matched_span.text)

