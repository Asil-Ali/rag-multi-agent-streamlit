# هذا الـ Agent مصمم للإجابة على أسئلة المستخدم
# يبحث في المستندات ويعرض أعلى 3 نتائج كاملة
from core.rag import search

def answer_question(query):
    """
    يعرض الإجابات المطابقة من المستندات
    """
    results = search(query, top_k=3)
    answer = ""
    for i, r in enumerate(results, start=1):
        answer += f"Result {i}:\n{r[:1000]}...\n\n"  # عرض أول 1000 حرف لكل نتيجة
    if not answer:
        answer = "No matching results found."
    return answer
