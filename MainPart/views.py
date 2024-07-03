from django.shortcuts import render


def runoob(request):
    context = {}
    context["hello"] = "Hello World!"
    views_name = {}
    views_name["name"] = "Newinfo"
    views_list = {}
    views_list["list"] = ["1", "2", "3", "4", "5"]
    return render(request, "runoob.html", context, views_name, views_list)
