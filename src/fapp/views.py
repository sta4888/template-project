from django.shortcuts import render


def index(request):
    return render(request, 'fapp/index.html')


def request_attrs(request):
    print(f"--request {request}")
    print(f"--request scheme {request.scheme}")
    print(f"--request body {request.body}")
    print(f"--request path {request.path}")
    print(f"--request path_info {request.path_info}")
    print(f"--request method {request.method}")
    print(f"--request encoding {request.encoding}")
    print(f"--request content_type {request.content_type}")
    print(f"--request content_params {request.content_params}")
    print(f"--request GET {request.GET}")
    print(f"--request POST {request.POST}")
    print(f"--request COOKIES {request.COOKIES}")
    print(f"--request FILES {request.FILES}")
    print(f"--request META {request.META}")
    print(f"--request headers {request.headers}")
    print(f"--request resolver_match {request.resolver_match}")
    # это не все
    return render(request, 'fapp/request_attrs.html', context={'request': request.body})
