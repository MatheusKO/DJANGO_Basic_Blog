from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.urls.base import reverse

# blog_posts = {
#     "january": "Vegan for a month!",
#     "february": "Walk 2 miles everyday!",
#     "march": "Study chess daily!",
#     "april": "Medidate 30 minutes a day.",
#     "may": "Take a cold shower every two days.",
#     "june": "Study Django for 40 minutes everyday.",
#     "july": "Read 15 pages of a book everyday.",
#     "august": "Do 10 pushups everyday.",
#     "september": "Brush your teeth twice a day",
#     "october": "Keep a journal",
#     "november": "Practice singing",
#     "december": None
# }

blog_posts = [
    {
        "title": "My chess progress over the last five years",
        "author": "MatheusKO",
        "last_update": "10/09/2021",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
        "image_url": None,
        "url": ""
    },
    {
        "title": "How programming affected my grades",
        "author": "MatheusKO7",
        "last_update": "04/05/2017",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
        "image_url": None,
        "url": ""
    },
    {
        "title": "How to look for a job after graduating",
        "author": "MatheusKO",
        "last_update": "21/07/2020",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
        "image_url": None,
        "url": ""
    }
]

# Create your views here.


def index(request):    
    posts = [post['title'] for post in blog_posts]

    # list_items = ""
    # for post in posts:
    #     capitalized_post = post.capitalize()
    #     list_items += f"<li><a href=''>{capitalized_post}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"

    # return HttpResponse(response_data)

    return render(request, "blog/index.html", {
        "posts": posts
    })

def post(request, post_title_url):
    post_title = str(post_title_url).replace("-", " ")
    try:
        post_data = next((post for post in blog_posts if post["title"] == post_title), None)
        return render(request, "blog/post.html", {
            "title": post_data["title"],
            "author": post_data["author"],
            "last_update": post_data["last_update"],
            "content": post_data["content"],
            "image_url": post_data["image_url"]
         })

        # simples html return
        # response_data = f"<h1>{challenge_text}</h1>"

        # return a static html template with render_to_string (template values should be hard-coded for this to work)
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:

        # render always return success, so it can't be used in this case
        # render_to_string works
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)

        # Django has a built-in solution for this - Http404 looks for a 404.html file in your root templates folder
        # NOTE: To really return the page, DEBUG must be set to false on our settings.py file, which is only the case in production 
        raise Http404()