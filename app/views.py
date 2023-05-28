import pickle
from django.shortcuts import render
import requests
from django.http import JsonResponse,HttpResponse
import pandas as pd
from app.fertilizer import fertilizer_dic
from app.crop_info import crop_dict

# loading our ML model for Crop  Recommendation system
with open('./saved_models/RandomForest.pkl', 'rb') as file:
    crop_model = pickle.load(file)

# render Home Page
def home(request):
    return render(request, 'index.html')




# render Predtion Page
def predictor(request):
    return render(request, 'crop.html')

def fetch_weather(city_name):
    api_key = '98ccbfd03418f5e0e724cfc4d789fddd'  
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    
    complete_url = base_url + "?q=" + city_name + "&appid=" + api_key 
    response = requests.get(complete_url)
    data = response.json()

    if 'main' in data and 'temp' in data['main'] and 'humidity' in data['main']:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        return (temperature-273.15),(humidity)
    else:
        return None, None



def formInfo(request):
    context = {}
    if request.method == 'POST':
        N = float(request.POST.get('N'))
        P = float(request.POST.get('P'))
        K = float(request.POST.get('K'))
        ph = float(request.POST.get('ph'))
        R = float(request.POST.get('R'))
        city_name = request.POST.get("city_name")
        
        temperature, humidity = fetch_weather(city_name)
  

# Create a DataFrame with feature names
    input_data = pd.DataFrame({
    'N': [N],
    'P': [P],
    'K': [K],
    'temperature': [temperature],
    'humidity': [humidity],
    'ph': [ph],
    'rainfall': [R]
    })

# Make the prediction using the DataFrame
# prediction = RF.predict(input_data)
# print("You should Grow:", prediction)


    if temperature is not None and humidity is not None:
            print( temperature)
            print(humidity)
          #  crop_prediction = crop_model.predict([[N, P, K, temperature, humidity, ph, R]])
            crop_prediction = crop_model.predict(input_data)

            context = {
                'crop_result': "You should grow " + crop_prediction[0]
            }

            return render(request, 'crop.html', context)
    else:
        return render(request, 'try_again.html')

    return render(request, 'crop.html', context)


import pandas as pd
from django.shortcuts import render
from django.utils.safestring import mark_safe
import os
from django.conf import settings

def fert_recommend(request):
    if request.method == 'POST':
        crop_name = str(request.POST.get('crop_name'))
        N = float(request.POST.get('N'))
        P = float(request.POST.get('P'))
        K = float(request.POST.get('K'))

        file_path = os.path.join(settings.BASE_DIR, 'static', 'Dataset', 'fertilizer.csv')
        df = pd.read_csv(file_path)

        nr = df[df['Crop'] == crop_name]['N'].iloc[0]
        pr = df[df['Crop'] == crop_name]['P'].iloc[0]
        kr = df[df['Crop'] == crop_name]['K'].iloc[0]

        n = nr - N
        p = pr - P
        k = kr - K
        temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
        max_value = temp[max(temp.keys())]
        if max_value == "N":
            if n < 0:
                key = 'NHigh'
            else:
                key = "Nlow"
        elif max_value == "P":
            if p < 0:
                key = 'PHigh'
            else:
                key = "Plow"
        else:
            if k < 0:
                key = 'KHigh'
            else:
                key = "Klow"

        response = str(fertilizer_dic[key])  # Use mark_safe to render the HTML content safely

        return render(request, 'fertilizer_result.html', {'recommendation': response})

    # Default response for GET method
    return render(request, 'fertilizer.html')



def plantde(request):
    # context = {"message": "This is a dictionary"}
    return render(request, 'plantde.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')






from .crop_info import crop_dict  # Importing crop_dict from crop_info.py

def crop_search(request):
    if request.method == 'POST':
        crop_name = request.POST.get('crop_name')
        if crop_name in crop_dict:
            crop_info = crop_dict[crop_name]
            return render(request, 'crop_search_result.html', {'crop_name':crop_name,'crop_info': crop_info})
        else:
            return render(request, 'crop_search_result.html', {'crop_name':crop_name,'crop_info': None})
    return render(request, 'crop_search.html')


def crop_list(request):
    crop_name = request.GET.get('crop_name')
    if crop_name in crop_dict:
        crop_info = crop_dict[crop_name]
        return render(request, 'crop_search_result.html', {'crop_name': crop_name, 'crop_info': crop_info})
    else:
        return render(request, 'crop_search_result.html', {'crop_name': crop_name, 'crop_info': None})




# import os
# from django.conf import settings
# from django.shortcuts import render
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import matplotlib.pyplot as plt
# from PIL import Image
# import numpy as np
# def plantde(request):
#     if request.method == 'POST':
#         # Get the uploaded image from the POST request
#         uploaded_image = request.FILES['image']

#         # Save the uploaded image to a temporary file
#         img_path = os.path.join(settings.MEDIA_ROOT, uploaded_image.name)
#         with open(img_path, 'wb+') as f:
#             for chunk in uploaded_image.chunks():
#                 f.write(chunk)

#         # Load the model
#         model_path = os.path.join(settings.BASE_DIR, './saved_models/version_3.h5')  # Update with the actual path to your model file
#         model = load_model(model_path)

#         # Preprocess the input image
#         # Preprocess the input image
#         img = image.load_img(img_path, target_size=(256, 256))
#         img_array = image.img_to_array(img) / 255.0
#         img_array = img_array.reshape(1, 256, 256, 3)


#         # Make the prediction
#         class_names = ['Class 0', 'Class 1', 'Class 2']  # Update with your actual class labels
#         predictions = model.predict(img_array)
#         predicted_class_index = np.argmax(predictions[0])
#         predicted_label = class_names[predicted_class_index]

#         # Delete the temporary image file
#         os.remove(img_path)

#         # Render the result in the template
#         return render(request, 'plantde_result.html', {'predicted_label': predicted_label})

#     return render(request, 'plantde.html')


from django.shortcuts import render
from tensorflow.keras.models import load_model
import numpy as np
import tensorflow as tf

# Load the model
model = load_model('./saved_models/version_3.h5')

# Define the class names
class_names = ['class1', 'class2', ...]  # Update with your actual class names

def plantde(request):
    if request.method == 'POST':
        # Get the uploaded image from the request
        image_file = request.FILES['image']

        # Preprocess the image
        img = tf.keras.preprocessing.image.load_img(image_file, target_size=(256, 256))
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = img / 255.0  # Normalize the image

        # Make the prediction
        prediction = model.predict(img)
        predicted_class = class_names[np.argmax(prediction[0])]

        # Prepare the context to render in the template
        context = {'predicted_class': predicted_class}

        return render(request, 'plantde_result.html', context)

    return render(request, 'plantde.html')
