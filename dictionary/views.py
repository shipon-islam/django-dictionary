from django.shortcuts import render
from .models import Dictionary
from django.http import JsonResponse
from django.core.paginator import Paginator
# Create your views here.
def dictionary(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        summary = request.POST.get('summary')
        description = request.POST.get('description')
        new_word = dictionary(word=word, summary=summary, description=description)
        new_word.save()

        return render(request, 'index.html', {'word': word, 'summary': summary, 'description': description})
    elif request.method == 'GET':       
        dictionary_list = Dictionary.objects.all().order_by('word')[::10]        
        return render(request, 'index.html', {'dictionary_list':dictionary_list})        
            


def dictionary_by_id(request, dictionaryId):
    if request.method == 'GET':
        dictionary_list = Dictionary.objects.get(id=dictionaryId)
        return render(request, 'dictionary_by_id.html', {'dictionary': dictionary_list})

def search_dictionary(request):
    query = request.GET.get('q', '')
    print(f"Search query: {query}")
    if not query:
        return JsonResponse([], safe=False)  # Debugging line to check the query
    results = Dictionary.objects.filter(word__istartswith=query).values('id', 'word')[:10]

    return JsonResponse(list(results), safe=False)


def filter_dictionary(request):
    if request.method == 'GET':
        page_number = request.GET.get('page', 1)
        per_page = request.GET.get('limit', 10) 
        dictionary_list = Dictionary.objects.all().order_by('word').values()
        paginator = Paginator(dictionary_list, per_page)
        print(f"count: {paginator.count}, page: {paginator.num_pages}, status=200)")
        try:
            page_obj = paginator.page(page_number)
        except:
            return JsonResponse({'error': 'Invalid page.'}, status=400)

        
        return JsonResponse({
            'dictionaries': list(page_obj.object_list),
            'total': paginator.count,
            'pages': paginator.num_pages,
            'current_page': page_obj.number,
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous(),
        })
    