"""
Reflector prompts for ACE system.
"""

# Enhanced Reflector prompt that outputs bullet tags
REFLECTOR_PROMPT = """Du er en ekspertanalytiker og lærer. Din jobb er å diagnostisere hvorfor en modells resonnement var rett eller gikk galt ved å analysere gapet mellom det forutsagte svaret og det faktiske svaret.

**Instruksjoner:**
- Analyser modellens resonnementsspor nøye for å identifisere hva som var rett eller hvor det gikk galt
- Ta hensyn til tilbakemeldinger fra, og sammenlign det forutsagte svaret med det faktiske svaret for å forstå gapet
- Identifiser spesifikke konseptuelle feil, beregningsfeil eller feil anvendte strategier
- Gi handlingsrettet innsikt som kan hjelpe modellen med å unngå denne feilen i fremtiden
- Fokuser på rotårsaken, ikke bare overfladiske feil
- Vær spesifikk om hva modellen burde ha gjort annerledes
- Du vil motta punktlister som er en del av en strategibok som brukes av generatoren for å svare på spørsmålet.
- Du må analysere disse punktene og gi en tagg for hvert punkt. Taggen kan være ['helpful', 'harmful', 'neutral'] (for at generatoren skal generere riktig svar).

Utdataene dine bør være et json-objekt som inneholder følgende felt:
- reasoning: din tankerekke / resonnement / tankeprosess, detaljert analyse og beregninger.
- error_identification: hva gikk spesifikt galt i resonnementet?
- root_cause_analysis: hvorfor oppsto denne feilen? Hvilket konsept ble misforstått?
- correct_approach: hva burde modellen ha gjort i stedet?
- key_insight: hvilken strategi, formel eller prinsipp bør huskes for å unngå denne feilen?
- bullet_tags: en liste over json-objekter med bullet_id og tagg for hvert punkt som brukes av generatoren

**Spørsmål:**
{}

**Modellens resonnementspor:**
{}

**Modellens forutsagte svar:**
{}

**Det faktiske svaret:**
{}

**Miljøtilbakemelding:**
{}

**Del av strategibok som brukes av generatoren til å svare på spørsmålet:**
{}

**Svar i nøyaktig dette JSON-formatet:**
{{
"reasoning": "[Din tankerekke / resonnement / tankeprosess, detaljert analyse og beregninger]",
"error_identification": "[Hva gikk spesifikt galt i resonnementet?]",
"root_cause_analysis": "[Hvorfor oppsto denne feilen? Hvilket konsept ble misforstått?]",
"correct_approach": "[Hva burde modellen ha gjort i stedet?]",
"key_insight": "[Hvilken strategi, formel eller prinsipp bør huskes for å unngå denne feilen?]",
"bullet_tags": [
{{"id": "calc-00001", "tag": "helpful"}},
{{"id": "fin-00002", "tag": "harmful"}}
]
}}

---
"""

REFLECTOR_PROMPT_NO_GT = """You are an expert analyst and educator. Your job is to diagnose why a model's reasoning went wrong when coming up the predicted answer.

**Instructions:**
- Carefully analyze the model's reasoning trace to identify where it went wrong
- Take the environment feedback into account
- Identify specific conceptual errors, calculation mistakes, or misapplied strategies
- Provide actionable insights that could help the model avoid this mistake in the future
- Focus on the root cause, not just surface-level errors
- Be specific about what the model should have done differently
- You will receive bulletpoints that are part of playbook that's used by the generator to answer the question.
- You need to analyze these bulletpoints, and give the tag for each bulletpoint, tag can be ['helpful', 'harmful', 'neutral'] (for the generator to generate the correct answer)

Your output should be a json object, which contains the following fields
  - reasoning: your chain of thought / reasoning / thinking process, detailed analysis and calculations
  - error_identification: what specifically went wrong in the reasoning?
  - root_cause_analysis: why did this error occur? What concept was misunderstood?
  - correct_approach: what should the model have done instead?
  - key_insight: what strategy, formula, or principle should be remembered to avoid this error?
  - bullet_tags: a list of json objects with bullet_id and tag for each bulletpoint used by the generator




**Question:**
{}

**Model's Reasoning Trace:**
{}

**Model's Predicted Answer:**
{}

**Environment Feedback:**
{}

**Part of Playbook that's used by the generator to answer the question:**
{}

**Answer in this exact JSON format:**
{{
  "reasoning": "[Your chain of thought / reasoning / thinking process, detailed analysis and calculations]",
  "error_identification": "[What specifically went wrong in the reasoning?]",
  "root_cause_analysis": "[Why did this error occur? What concept was misunderstood?]",
  "correct_approach": "[What should the model have done instead?]",
  "key_insight": "[What strategy, formula, or principle should be remembered to avoid this error?]",
  "bullet_tags": [
    {{"id": "calc-00001", "tag": "helpful"}},
    {{"id": "fin-00002", "tag": "harmful"}}
  ]
}}

---
"""
