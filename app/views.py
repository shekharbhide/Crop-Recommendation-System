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
    if request.method == 'GET':
        N = float(request.GET['N'])
        P = float(request.GET['P'])
        K = float(request.GET['K'])
        T = float(request.GET['T'])
        H = float(request.GET['H'])
        Ph = float(request.GET['Ph'])
        R = float(request.GET['R'])

    y_pred = model.predict([[N, P, K, T, H, Ph, R]])
  #  print(y_pred)

    context = {
        'crop_result': "Crop Recommended :  "+y_pred[0]
    }
    return render(request, 'main.html', context)


"""
def home(request):
    context = {}
    if request.method == 'POST':
        Nitrogen= float(request.POST.get('N'))
        Phosporus=float(request.POST.get('P'))
        Potasium=float(request.POST.get('K'))
        temperature=float(request.POST.get('T'))
        humidity=float(request.POST.get('H'))
        ph=float(request.POST.get('Ph'))
        rainfall=float(request.POST.get('R'))

        data = np.array([[Nitrogen, Phosporus, Potasium, temperature, humidity, ph, rainfall]])
        prediction = SVM.predict(data)

        context = {
        'result': "You should grow "+prediction[0]
        }
    
    return render(request, 'home.html',context)
 """
