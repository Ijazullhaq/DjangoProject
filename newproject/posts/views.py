from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        "id":1,
        "title":'Let Explore Python',
        "content": 'Python is interpreted, high-level language'
    }
]

def home(request):
    html = ""
    for post in posts:
        html += f'''
            <div>
                <h1>{post['id']} - {post['title']}</h1>
                <p>{post['content']}</p>
            </div>
'''
    return HttpResponse(html)
# dynamic url id 
def post (request, id):
    return HttpResponse(id)

