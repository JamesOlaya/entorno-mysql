from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Aprendiz
import json

class AprendizView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id > 0):
            aprendices = list(Aprendiz.objects.filter(id=id).values())
            if len(aprendices) > 0:
                aprendiz = aprendices[0]
                datos = {'message': "Success", 'company': aprendiz}
            else:
                datos = {'message': "Company not found..."}
            return JsonResponse(datos)
        else:
            aprendices = list(Aprendiz.objects.values())
            if len(aprendices) > 0:
                datos = {'message': "Success", 'companies': aprendices}
            else:
                datos = {'message': "Companies not found..."}
            return JsonResponse(datos)
    def post(self, request, ):
        jd = json.loads(request.body)
        Aprendiz.objects.create(name=jd['name'], last_name=jd['last_name'], year_birth=jd['year_birth'], document_num=jd['document_num'],document_type=jd['document_type'],ficha_num=jd['ficha_num'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    def put(self, request,id ):
        jd = json.loads(request.body)
        companies = list(Aprendiz.objects.filter(id=id).values())
        if len(companies) > 0:
            aprendiz = Aprendiz.objects.get(id=id)
            aprendiz.name = jd['name']
            aprendiz.last_name=jd['last_name']
            aprendiz.year_birth=jd['year_birth']
            aprendiz.document_num=jd['document_num']
            aprendiz.document_type=jd['document_type']
            aprendiz.ficha_num=jd['ficha_num']
            aprendiz.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Company not found..."}
        return JsonResponse(datos)
    def delete(self, request,id ):
        aprendices = list(Aprendiz.objects.filter(id=id).values())
        if len(aprendices) > 0:
            Aprendiz.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Aprendiz not found..."}
        return JsonResponse(datos)
    