# -*- coding: utf-8 -*-
from django.shortcuts import render,reverse,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def index(request):
	return HttpResponse("<h4> <center> Thankyou for visting our website.<br> Use upload in the url to upload </center> </h4>")

#--------------------------------------------------------------------------------------------------------
"""

		You can implement the below process to choose any csv file and upload it directly 
		to the database. There are some Data Errors, try solve them in different way.

"""
#---------------------------------------------------------------------------------------------------------

from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Document
from .forms import DocumentForm

import logging
import pandas as pd
import io
def upload_csv(request):
	z = False
	LabelName.objects.all().delete()
	if request.method == 'POST' and request.FILES['myfile']:
		z = True
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		return render(request, 'simple_upload.html', {'z':z})
	return render(request, 'simple_upload.html',{'z':z})
#--------------------------------------------------------------------------------------------------------
"""

			Uploading CSV file to database. 
			The below process is working fine.

"""
#---------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
"""
		The below code is of no use. Try to get some insights. 


"""
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
"""
		Implementing ML over the data in the database😊️

"""
#--------------------------------------------------------------------------------------------------------

from .models import LabelName
from django.views.decorators.csrf import csrf_protect
import pandas as pd
import numpy as np
import os
import re
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.externals import joblib
def ml(request):
	z = False
	#data = Document1.objects.all()
	#data = serializers.serialize( "python", Document1.objects.all())
	d = os.getcwd()
	file1 = [f for f in os.listdir(d) if f.endswith('.csv')]
	try:	
		data = pd.read_csv(file1[0])
	except:
		return HttpResponse("<h2><center> Please upload the file </center> </h2>")	
	col = []
	for i in data.columns:
		col.append(i)
	test = False
	t1 = 'k'
	if(request.method == 'POST'):
		try:	
			t1 = request.POST['test']
			#t1 = t1.encode('ascii')
		except:
			print("No value entered")
	if(t1=='Y'):
		test = True
		Label = LabelName.objects.values_list('Label')[0]
		#Label = Label[0].encode('ascii')
		col.remove(Label)
		return render(request, 'index.html', {'test2':test,'col':col})
	elif(t1 == 'N'):
		os.remove(file1[0])
		os.remove('model.pkl')
		test = True
		LabelName.objects.all().delete()
		return render(request, 'index.html', {'test4':test})
	if(request.method == 'POST'):
		Preprocess = request.POST['Preprocess']
		Label = request.POST['Label Name']
		#Label = Label.encode('ascii')
		#u'label' -> label ascii
		split = request.POST['split']
		z = True
		obj = LabelName(Preprocess = Preprocess,Label = Label, split = split)
		obj.save()
	if(z):
		le = LabelEncoder()
		sc = StandardScaler()
		print("Printing label after decoding {}".format(Label))
		if(data[Label].dtype == 'object'):
			data[Label] = le.fit_transform(data[Label]) 
		y = data[Label].values
		#print(y)
		for i in data.columns:
			c1 = re.findall(r"unnamed",i.lower())
			c2 = re.findall(r"id",i.lower())
			if(len(c1)>0 or len(c2)>0):
				data = data.drop(i,axis = 1)
		if(Preprocess == 'Y'):
			dop = []
			for i in data.keys():
				s = []
				if(data[i].isna().sum()>0):
					if(data[i].dtypes == 'int64' or data[i].dtypes == 'float64'):
						data[i].fillna(data[i].mean(),inplace = True)
					elif(data[i].dtypes == 'object'):
						data[i].fillna(data[i].mode()[0],inplace = True)			
				if(data[i].dtype == 'object'):
					for j in data[i]:
						s.append(len(j))
				else:
					s.append(0)
				if(max(s) > 30):
					dop.append(i)
			for z1 in dop:
				print("Dropping the column : ", z1)
				data = data.drop(z1,axis = 1)
			for i in data.keys():
				if(data[i].dtype == 'object'):
					data[i] = le.fit_transform(data[i])
		#data1 = data.astype('float64')
		X = data.drop(Label,axis=1)
		X = X.values
		from sklearn.model_selection import train_test_split
		X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = int(split))
		X_train = sc.fit_transform(X_train)
		X_test = sc.fit_transform(X_test)
		from sklearn.linear_model import LogisticRegression
		lr  = LogisticRegression()
		lr.fit(X_train,y_train)
		y_pred = lr.predict(X_test)
		from sklearn.metrics import accuracy_score as ac
		ac1 = ac(y_test,y_pred)
		#LabelName.objects.all().delete()
		#os.remove(file1[0])
		joblib.dump(lr, "model.pkl")
		return render(request,'data.html',{'z':z,'label':Label,'ac1':ac1})
	return render(request,'data.html',{'col':col})

#---------------------------------------------------------------------------------------------------------------------------------------------		

def ml1(request):
	d = os.getcwd()
	file1 = [f for f in os.listdir(d) if f.endswith('.csv')]	
	data = pd.read_csv(file1[0])
	col = []
	for i in data.columns:
		c1  = re.findall("unnamed",i.lower())
		if(len(c1) == 0):
			col.append(i)
	Label = LabelName.objects.values_list('Label')[0]
	Label = Label[0].encode('ascii')
	col.remove(Label)
	df = pd.DataFrame()
	if(request.method == 'POST'):
		for i in col:
			n = []
			a = request.POST[i]
			a = a.encode('ascii')
			n.append(a)
			df[i] = np.asarray(n)
			test = True
		if(test):
			le = LabelEncoder()
			sc = StandardScaler()
			dop = []
			for i in df.columns:
				s = []
				if(data[i].dtype == "int64" or data[i].dtype == "float64" or data[i].dtype == "int32" or data[i].dtype == "float32"):
					df[i] = df[i].astype("float32")
				if(data[i].dtype == 'object'):
					for j in data[i]:
						s.append(len(j))
				else:
					s.append(0)
				c1 = re.findall(r"\id",i.lower())
				if(len(c1)>0):
					dop.append(i)
				if(max(s)>0):
					dop.append(s)
			if(len(dop)>0):
				for i in dop:
					df = df.drop(i,axis = 1)
			for i in df.columns:
				if(data[i].dtype == "object"):
					df[i] = le.fit_transform(df[i])
			lr = joblib.load("model.pkl")
			#df = df.astype('float32')		
			x = df.values
			print(x)
			x = sc.fit_transform(x)
			y_pred = lr.predict(x)
			os.remove('model.pkl')
			os.remove(file1[0])
			LabelName.objects.all().delete()
			return render(request,'index.html' , {'test3':test,'y_pred':y_pred[0]})
	else:
		return HttpResponse("<h3><center> Your test data is not aligned properly </center></h3>")
	return render(request, "data.html", {'test1':True})
#---------------------------------------------------------------------------------------------------------------------------------------------------















