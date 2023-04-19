import pickle
from django.shortcuts import render


# render Home Page
def home(request):
    return render(request, 'home.html')


# loading our ML model
with open('./saved_models/RandomForest.pkl', 'rb') as file:
    model = pickle.load(file)

# render Predtion Page


def predictor(request):
    return render(request, 'main.html')


def formInfo(request):
    context = {}
    if request.method == 'POST':
        N = float(request.POST.get('N'))
        P = float(request.POST.get('P'))
        K = float(request.POST.get('K'))
        T = float(request.POST.get('T'))
        H = float(request.POST.get('H'))
        Ph = float(request.POST.get('Ph'))
        R = float(request.POST.get('R'))

    y_pred = model.predict([[N, P, K, T, H, Ph, R]])
    print(y_pred)
    context = {
        'crop_result': "Crop Recommended: " + y_pred[0]
    }

    return render(request, 'main.html', context)


def plantde(request):
    # context = {"message": "This is a dictionary"}
    return render(request, 'plantde.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
