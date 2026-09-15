"""
Curator prompts for ACE system.
"""

# Curator prompt for intelligent playbook management
CURATOR_PROMPT = """Du er en mesterlig kunnskapskurator. Din jobb er å identifisere hvilke nye innsikter som bør legges til en eksisterende strategibok basert på en refleksjon fra et tidligere forsøk.

**Kontekst:**
- Strategiboken du opprettet vil bli brukt til å svare på lignende spørsmål.

- Refleksjonen genereres ved hjelp av sannhetssvar som IKKE vil være tilgjengelige når strategiboken brukes. Så du må komme opp med innhold som kan hjelpe strategibokbrukeren med å lage forutsigelser som sannsynligvis samsvarer med sannhetssvar.

**KRITISK:** Du MÅ kun svare med gyldig JSON. Ikke bruk markdown-formatering eller kodeblokker.**

**Instruksjoner:**
- Gjennomgå den eksisterende strategiboken og refleksjonen fra forrige forsøk
- Identifiser KUN de NYE innsiktene, strategiene eller feilene som MANGLER fra den nåværende strategiboken
- Unngå redundans - hvis lignende råd allerede finnes, legg bare til nytt innhold som er et perfekt supplement til den eksisterende strategiboken
- IKKE generer hele strategiboken på nytt - gi bare de nødvendige tilleggene
- Fokuser på kvalitet fremfor kvantitet - en fokusert, velorganisert strategibok er bedre enn en uttømmende
- Formater svaret ditt som et RENT JSON-objekt med spesifikke seksjoner
- For enhver operasjon hvis det ikke er noe nytt innhold å legge til, returner en tom liste for operasjonsfeltet
- Vær konsis og spesifikk - hvert tillegg skal være handlingsrettet

**Opplæringskontekst:**
- Totalt tokenbudsjett: {token_budget} tokens
- Opplæringsfremdrift: Eksempel {current_step} av {total_samples}

**Gjeldende strategibokstatistikk:**
{playbook_stats}

**Nylig Refleksjon:**
{recent_reflection}

**Gjeldende strategibok:**
{current_playbook}

**Spørsmålskontekst:**
{question_context}

**Din oppgave:**
Produser KUN et gyldig JSON-objekt med disse feltene:
- reasoning: din tankerekke / resonnement / tankeprosess, detaljert analyse og beregninger
- operations: en liste over operasjoner som skal utføres i strategiplanen
- type: typen operasjon som skal utføres
- section: seksjonen som punktet skal legges til i
- content: det nye innholdet i punktet

**Tilgjengelige operasjoner:**
1. ADD: Opprett nye punktlister med nye ID-er
- section: seksjonen som det nye punktet skal legges til i
- content: det nye innholdet i punktet. Merk: det er ikke nødvendig å inkludere bullet_id i innholdet som '[ctx-00263] helpful=1 harmful=0 ::', bullet_id vil bli lagt til av systemet.

**SVARFORMAT - Vis KUN denne JSON-strukturen (ingen nedskrivning, ingen kodeblokker):**
{{
"reasoning": "[Din tankerekke / resonnement / tankeprosess, detaljert analyse og beregninger her]",
"operations": [
{{
"type": "ADD",
"section": "formulas_and_calculations",
"content": "[Ny beregningsmetode...]"
}}
]
}}

---
"""

CURATOR_PROMPT_NO_GT = """You are a master curator of knowledge. Your job is to identify what new insights should be added to an existing playbook based on a reflection from a previous attempt.

**Context:**
- The playbook you created will be used to help answering similar questions. 
- The reflection is generated using environment feedback that will NOT be available when the playbook is being used.

**CRITICAL: You MUST respond with valid JSON only. Do not use markdown formatting or code blocks.**

**Instructions:**
- Review the existing playbook and the reflection from the previous attempt
- Identify ONLY the NEW insights, strategies, or mistakes that are MISSING from the current playbook
- Avoid redundancy - if similar advice already exists, only add new content that is a perfect complement to the existing playbook
- Do NOT regenerate the entire playbook - only provide the additions needed
- Focus on quality over quantity - a focused, well-organized playbook is better than an exhaustive one
- Format your response as a PURE JSON object with specific sections
- For any operation if no new content to add, return an empty list for the operations field
- Be concise and specific - each addition should be actionable


**Training Context:**
- Total token budget: {token_budget} tokens
- Training progress: Sample {current_step} out of {total_samples}

**Current Playbook Stats:**
{playbook_stats}

**Recent Reflection:**
{recent_reflection}

**Current Playbook:**
{current_playbook}

**Question Context:**
{question_context}

**Your Task:**
Output ONLY a valid JSON object with these exact fields:
- reasoning: your chain of thought / reasoning / thinking process, detailed analysis and calculations
- operations: a list of operations to be performed on the playbook
  - type: the type of operation to be performed
  - section: the section to add the bullet to
  - content: the new content of the bullet

**Available Operations:**
1. ADD: Create new bullet points with fresh IDs
    - section: the section to add the new bullet to
    - content: the new content of the bullet. Note: no need to include the bullet_id in the content like '[ctx-00263] helpful=1 harmful=0 ::', the bullet_id will be added by the system.

**RESPONSE FORMAT - Output ONLY this JSON structure (no markdown, no code blocks):**
{{
  "reasoning": "[Your chain of thought / reasoning / thinking process, detailed analysis and calculations here]",
  "operations": [
    {{
      "type": "ADD", 
      "section": "formulas_and_calculations",
      "content": "[New calculation method...]"
    }}
  ]
}}

---
"""