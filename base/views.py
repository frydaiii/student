# Create your views here.

from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from base.models import Student


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def students_list(request):
    students = serializers.serialize('json', Student.objects.filter())
    return HttpResponse(students)


@csrf_exempt
def student_detail(request, student_id):
    if request.method == 'GET':
        student = serializers.serialize('json', [Student.objects.get(pk=student_id)])
        return HttpResponse(student)
    if request.method == 'PUT' or request.method == 'POST':
        body = QueryDict(request.body, mutable=True).dict()

        student_id = body['id']
        update_fields = dict((k, body[k]) for k in body.keys() if k != 'id')

        Student.objects.update_or_create(
            id=student_id,
            defaults=update_fields
        )
        return HttpResponse(None)

    if request.method == 'DELETE':
        Student.objects.get(pk=student_id).delete()
        return HttpResponse(None)
