from pybo.models import Question

def category_list(request):
    return {'categorylist':Question.categorylist}