from django.shortcuts import render

import json
import os
# Create your views here.
def index(request):    
    with open('jianli/data.json','r') as f:
        data = json.load(f)
    dic = {}
    for k,v in data.items():
        dic[k] = v
    
    return render(request, 'jianli/index.html', dic)