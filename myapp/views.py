from django.shortcuts import render, HttpResponse
import hashlib

# Create your views here.
def home(request):
    input_data = None
    hashed_value = None
    
    if request.method == 'POST':
        input_data = request.POST.get('inputData')
        
        if input_data:
            hash_object = hashlib.sha256(input_data.encode())
            hashed_value = hash_object.hexdigest()
    
    return render(request, 'home.html', {'input_data': input_data, 'hashed_value': hashed_value})