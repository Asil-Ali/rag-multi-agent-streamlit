# هذا الـ Agent يملخص محتوى الملفات حسب استعلام المستخدم
# يستخدم دالة search من core/rag.py
from core.rag import search
import os

api_key = os.getenv("OPENROUTER_API_KEY")


def summarize_document(query):
    """
    يبحث في المستندات ويعطي ملخص أول 3 نتائج
    """
    results = search(query, top_k=3)
    summary = ""
    for r in results:
        summary += r[:500] + "...\n"  # أول 500 حرف لكل نتيجة
    return summary
