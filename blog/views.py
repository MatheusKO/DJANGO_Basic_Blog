from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.urls.base import reverse

blog_posts = [
    {
        "title": "My chess progress over the last five years",
        "author": "MatheusKO",
        "last_update": "10/09/2021",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Odio tempor orci dapibus ultrices in iaculis. Mauris sit amet massa vitae tortor condimentum lacinia quis. Ac turpis egestas maecenas pharetra convallis. Diam in arcu cursus euismod quis viverra nibh cras pulvinar. Consectetur purus ut faucibus pulvinar. Dignissim diam quis enim lobortis scelerisque. Tortor pretium viverra suspendisse potenti nullam. Dui sapien eget mi proin sed libero. Auctor elit sed vulputate mi sit amet. Vulputate ut pharetra sit amet aliquam id diam maecenas. Orci dapibus ultrices in iaculis nunc sed augue lacus. Netus et malesuada fames ac. Orci ac auctor augue mauris augue. Magna fringilla urna porttitor rhoncus dolor purus non enim praesent. Feugiat pretium nibh ipsum consequat. Porttitor eget dolor morbi non. At tellus at urna condimentum mattis pellentesque id nibh. Aliquam purus sit amet luctus. Magna fringilla urna porttitor rhoncus dolor purus non. Placerat orci nulla pellentesque dignissim. Integer quis auctor elit sed vulputate. Eleifend donec pretium vulputate sapien nec sagittis aliquam malesuada bibendum. Luctus accumsan tortor posuere ac ut. Euismod in pellentesque massa placerat duis ultricies lacus sed turpis. Eu consequat ac felis donec et odio pellentesque diam volutpat. Eu facilisis sed odio morbi.",
        "image_url": "../../static/blog/images/beth harmon stare.jpg",
        "url": ""
    },
    {
        "title": "How learning how to code affected my grades",
        "author": "MatheusKO7",
        "last_update": "04/05/2017",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
        "image_url": "../../static/blog/images/coding.jpg",
        "url": ""
    },
    {
        "title": "How to look for a job after graduating",
        "author": "MatheusKO",
        "last_update": "21/07/2020",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sapien et ligula ullamcorper malesuada. Sagittis eu volutpat odio facilisis. At varius vel pharetra vel turpis nunc eget. Aliquam malesuada bibendum arcu vitae elementum. Potenti nullam ac tortor vitae purus. Turpis egestas integer eget aliquet. Nullam non nisi est sit. Amet consectetur adipiscing elit ut. Vel risus commodo viverra maecenas accumsan lacus vel facilisis. Aliquam ut porttitor leo a diam. Maecenas sed enim ut sem viverra aliquet eget. Ultricies lacus sed turpis tincidunt id aliquet. Ut venenatis tellus in metus vulputate eu. Viverra mauris in aliquam sem fringilla ut morbi tincidunt. Nisl nisi scelerisque eu ultrices vitae auctor. In pellentesque massa placerat duis. Tortor aliquam nulla facilisi cras fermentum odio eu feugiat. Volutpat commodo sed egestas egestas fringilla phasellus faucibus scelerisque eleifend. Commodo ullamcorper a lacus vestibulum sed arcu non odio euismod. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae nunc. Ultrices dui sapien eget mi proin sed libero enim. Pulvinar sapien et ligula ullamcorper. Turpis cursus in hac habitasse platea dictumst. Hac habitasse platea dictumst vestibulum rhoncus est pellentesque elit. Tincidunt id aliquet risus feugiat in ante. Adipiscing bibendum est ultricies integer. Quisque sagittis purus sit amet. Integer vitae justo eget magna fermentum iaculis. Etiam tempor orci eu lobortis elementum nibh. Vehicula ipsum a arcu cursus vitae. Vitae tortor condimentum lacinia quis vel eros donec. Risus nec feugiat in fermentum posuere urna. Viverra adipiscing at in tellus integer feugiat scelerisque varius morbi. Volutpat sed cras ornare arcu dui vivamus arcu. Mauris augue neque gravida in fermentum et. Justo donec enim diam vulputate ut pharetra sit amet. Justo donec enim diam vulputate. Venenatis cras sed felis eget velit aliquet sagittis id. Sit amet luctus venenatis lectus magna fringilla. Vitae aliquet nec ullamcorper sit amet risus nullam eget felis. Est ullamcorper eget nulla facilisi etiam dignissim diam quis enim. Nibh ipsum consequat nisl vel pretium lectus quam id leo. Leo integer malesuada nunc vel risus commodo. Morbi tristique senectus et netus et malesuada fames. Pretium nibh ipsum consequat nisl vel pretium lectus quam id. Gravida quis blandit turpis cursus in hac. Odio ut enim blandit volutpat maecenas volutpat blandit aliquam etiam. A pellentesque sit amet porttitor eget dolor morbi. Aliquet bibendum enim facilisis gravida. Sed viverra tellus in hac habitasse. Massa massa ultricies mi quis hendrerit dolor magna eget. Eget arcu dictum varius duis at. Odio morbi quis commodo odio. Eget felis eget nunc lobortis mattis aliquam faucibus. Lacus sed turpis tincidunt id aliquet risus. Sit amet consectetur adipiscing elit pellentesque habitant morbi tristique. Sed faucibus turpis in eu mi. Eu lobortis elementum nibh tellus molestie nunc. Sit amet aliquam id diam maecenas ultricies mi. Congue nisi vitae suscipit tellus mauris. Cras ornare arcu dui vivamus arcu. Mauris rhoncus aenean vel elit. Tortor pretium viverra suspendisse potenti nullam ac tortor. Egestas sed sed risus pretium quam vulputate dignissim.",
        "image_url": "../../static/blog/images/graduated loan hat.jpg",
        "url": ""
    }
]

# Create your views here.


def index(request):
    posts = []
    extracted_dict = None
    for post in blog_posts:
        extracted_dict = dict((key, post[key]) for key in ['title', 'image_url'] if key in post)
        posts.append(extracted_dict)
        print(extracted_dict)

    # posts = [blog_posts[0][k] for k in ['title', 'image_url']]
     	

    print(posts)
    # posts = [post['title', 'image_url'] for post in blog_posts]

    # list_items = ""
    # for post in posts:
    #     capitalized_post = post.capitalize()
    #     list_items += f"<li><a href=''>{capitalized_post}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"

    # return HttpResponse(response_data)

    return render(request, "blog/index.html", {
        "posts": posts
    })

def posts(request):
    posts = []
    extracted_dict = None
    for post in blog_posts:
        extracted_dict = dict((key, post[key]) for key in ['title', 'image_url'] if key in post)
        posts.append(extracted_dict)
        print(extracted_dict)

    # posts = [blog_posts[0][k] for k in ['title', 'image_url']]
     	

    print(posts)
    # posts = [post['title', 'image_url'] for post in blog_posts]

    # list_items = ""
    # for post in posts:
    #     capitalized_post = post.capitalize()
    #     list_items += f"<li><a href=''>{capitalized_post}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"

    # return HttpResponse(response_data)

    return render(request, "blog/posts.html", {
        "posts": posts
    })

def post_detail(request, slug):
    post_title = str(slug).replace("-", " ")
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