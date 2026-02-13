# هذا الـ Agent يركز على الملفات المتعلقة بالتسويق
from core.rag import search

def marketing_insights(query):
    """
    يبحث في المستندات ويعرض نتائج تحتوي على كلمات تسويقية
    """
    results = search(query, top_k=5)
    filtered = []
    for r in results:
        text_lower = r.lower()
        if "marketing" in text_lower or "digital" in text_lower:
            filtered.append(r[:1000] + "...")
    if not filtered:
        return "No marketing-related results found."
    return "\n\n".join(filtered)
