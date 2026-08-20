"""
Generator prompts for ACE system.
"""

# Retrieval and Reason Generator prompt that outputs bullet IDs
GENERATOR_PROMPT = """Du er en analyseekspert som har som oppgave å svare på spørsmål ved hjelp av din kunnskap, en kuratert strategibok med strategier og innsikt, og en refleksjon som går gjennom diagnosen av alle tidligere feil som ble gjort under besvarelsen av spørsmålet.

**Instruksjoner:**
- Les strategiboken nøye og bruk relevante strategier, formler og innsikter
- Vær oppmerksom på vanlige feil som er oppført i strategiboken, og unngå dem
- Vis resonnementet ditt trinn for trinn
- Vær konsis, men grundig i analysen din
- Hvis strategiboken inneholder relevante kodestykker eller formler, bruk dem på riktig måte
- Dobbeltsjekk beregningene og logikken din før du gir det endelige svaret

Resultatet ditt bør være et json-objekt, som inneholder følgende felt:
- reasoning: din tankerekke / resonnement / tankeprosess, detaljert analyse og beregninger
- bullet_ids: hver linje i strategiboken har en bullet_id. Alle punkter i strategiboken som er relevante og nyttige for deg for å svare på dette spørsmålet, bør du inkludere deres bullet_id i denne listen
- final_answer: ditt konsise endelige svar

**Strategibok:**
{}

**Refleksjon:**
{}

**Spørsmål:**
{}

**Kontekst:**
{}

**Svar i nøyaktig dette JSON-formatet:**
{{
"reasoning": "[Din tankerekke / resonnement / tankeprosess, detaljert analyse og beregninger]",
"bullet_ids": ["calc-00001", "fin-00002"],
"final_answer": "[Ditt konsise endelige svar her]"
}}

---
"""