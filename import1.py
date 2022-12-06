import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("es_core_news_sm")

# Process whole documents
text = ("¡Hola, soy Ines! Soy una de las programadoras "
        "principales de spaCy, un paquete popular para hacer "
        "Procesamiento de Lenguaje Natural en Python. "
        "En esta lección veremos cómo empezar con spaCy y "
        "echaremos un vistazo a sus conceptos más "
        "importantes.")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
