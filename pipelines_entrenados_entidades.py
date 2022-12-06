# Las entidades nombradas son "objetos de la vida real" que tienen un nombre asignado. Por ejemplo, una persona, una organización o un país.

import spacy

# Carga el pipeline pequeño de español
nlp = spacy.load("es_core_news_sm")

# Procesa un texto
doc = nlp(
    "Luego del evento de Mercado de Valores titulado “El impacto del conflicto Rusia-Ucrania” se desprenden cuatro posibilidades a lo que el experto responde:"
    "Aumento exponencial de tensiones entre OTAN y Rusia : Muy poco probable "
    "Esto provocaría una reacción catastrófica en los mercados financieros"
)

# Itera sobre las entidades predichas
for ent in doc.ents:
    # Imprime en pantalla el texto y la etiqueta de la entidad
    print(ent.text, ent.label_)
