from mistral_api import mistral_chat
def route_subject(query: str) -> str:
    query = query.lower()
    if "chemistry" in query or "atom" in query or "periodic" in query:
        return "chemistry"
    elif "physics" in query or "force" in query or "energy" in query or "atomic" in query:
        return "physics"
    elif "math" in query or "calculus" in query or "algebra" in query or "equation" in query:
        return "math"
    elif "history" in query or "war" in query or "king" in query or "date" in query:
        return "history"
    elif "biology" in query or "cell" in query or "organism" in query or "species" in query:
        return "biology"
    elif "english" in query or "literature" in query or "poem" in query or "grammar" in query:
        return "english"
    else:
        return "general"
