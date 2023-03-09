from django.http import HttpResponse


def aboutUs(request):
    return HttpResponse("<b>Hello World</b>")


def course(request):
    return HttpResponse("Courses")


def courseDetail(request, courseName):
    return HttpResponse(courseName)
