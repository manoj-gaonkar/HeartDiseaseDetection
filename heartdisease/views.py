from django.shortcuts import render
import joblib


def index(request):
    if request.method == "POST":
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        cpt = int(request.POST.get('cpt'))
        trestbps = int(request.POST.get('trestbps'))
        chol = int(request.POST.get('chol'))
        fbs = int(request.POST.get('fbs'))
        rest_ecg = int(request.POST.get('rest_ecg'))
        thalach = int(request.POST.get('thalach'))
        exang = int(request.POST.get('exang'))
        oldpeak = round(float(request.POST.get('oldpeak')),1)
        slope = int(request.POST.get('slope'))
        ca = int(request.POST.get('ca'))
        thal = int(request.POST.get('thal'))
        heartlist = [[age,sex,cpt,trestbps,chol,fbs,rest_ecg,thalach,exang,oldpeak,slope,ca,thal]]

        # heartlist = [[58,0,0,100,248,0,0,122,0,1,1,0,2]]

        # print(age,sex,cpt,trestbps,chol,fbs,rest_ecg,thalach,exang,oldpeak,slope,ca,thal)
        # print(age,sex,cpt)

        heartmodel = joblib.load('heart_model.pkl')
        
        result = heartmodel.predict(heartlist)
        print(result)
        context = {
            'result': result,
        }
        return render(request, 'result.html',context)
    return render(request, 'index.html')

def result(request):
    return render(request,'result.html')