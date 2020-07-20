#importing libraries
import sys
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
	return flask.render_template('index.html')



def ValuePredictor(to_predict_list): 
	to_predict = np.array(to_predict_list).reshape(1,8) 
	loaded_model = pickle.load(open("model.pkl", "rb")) 
	result = loaded_model.predict(to_predict) 
	return result[0] ,to_predict

def tree(thal, thalach, slope, exang, cp, oldpeak, ca, sex):
	res = 0
	str1 = ""
	dict1 = {"thalach" : "","slope" : "" , "oldpeak" : ""}
	if thal <= 2.5:
		if oldpeak <= 1.699999988079071:
			#dict1["oldpeak"] = "should be > 1.6"(this)
			if ca <= 0.5:
				if thalach <= 158.5:
					#dict1["thalach"] = "should be > 158.5"
					#print(dict1,file = sys.stdout)
					res = 1
					st1 = "chance of heart disease"
				else:  # if thalach > 158.5
					#dict1["thalach"] = "should be <= 158.5"
					res = 1
					#dict1["oldpeak"] = "should be > 2"
					str1 = "chance of heart disease"
			else:  # if ca > 0.5
                                dict1["oldpeak"] = "should be > 1.6" #this
                                if cp <= 0.5:
                                	str1 = "no chance of heart disease"
                                else:# if cp > 0.5
                                        if slope <= 1.5:
                                        	dict1["slope"] = "should be > 1.5"
                                        	if thal <= 1.5:
                                                        str1 = "no chance of heart disease"
                                        	else:  # if thal > 1.5
                                                        str1 = "chance of heart disease"
                                        else:  # if slope > 1.5
                                        	dict1["slope"] = "should be <= 1.5"
                                        	res = 1
                                        	#dict1["slope"] = "slope < 2"
                                        	str1 = "chance of heart disease"
		else:  # if oldpeak > 1.699999988079071
                	dict1["oldpeak"] = "should be < 1.6"
               		if cp <= 1.5:
                                str1 = "no chance of heart disease"
                	else:# if cp > 1.5
                        	str1 = "chance of heart disease"
	else:  # if thal > 2.5
        	if oldpeak <= 0.7000000178813934:
        		dict1["oldpeak"] = "should be > 0.7"
        		if thalach <= 140.5:
        			dict1["thalach"] = "thalach > 140.5"
        			if slope <= 1.5:
        				str1 = "no chance of heart disease"
        			else:  # if slope > 1.5
                                	res = 1
                                	dict1["slope"] = "slope <= 1.5"
                                	#dict1["thalach"] = "thalach > 141"
                                	#dict1["oldpeak"] = "oldpeak > 1"
                                	str1 = "chance of heart disease"
        		else: # if thalach > 140.5
                        	if thalach <= 143.5:
                                	str1 = "no chance of heart disease"
                        	else:  # if thalach > 143.5
                        		dict1["thalach"] = "thalach <= 143.5"
                        		if ca <= 0.5:
                                		res = 1
                                		str1 = "chance of heart disease"
                        		else:  # if ca > 0.5
                                                if thalach <= 155.0:
                                                        str1 = "no chance of heart disease"
                                                else:  # if thalach > 155.0
                                                        str1 = "no chance of heart disease"
        	else:  # if oldpeak > 0.7000000178813934
                        if exang <= 0.5:
                                if cp <= 1.5:
                                        str1 = "no chance of heart disease"
                                else:  # if cp > 1.5
                                        if oldpeak <= 1.949999988079071:
                                                if thalach <= 155.5:
                                                        str1 = "no chance of heart disease"
                                                else:  # if thalach > 155.5
                                                	res = 1
                                                	dict1["thalach"] = "thalach <= 155.5"
                                                	str1 = "chance of heart disease"
                                        else:  # if oldpeak > 1.949999988079071
                                                str1 = "no chance of heart disease"
                        else:  # if exang > 0.5
                                str1 = "return no chance of heart disease"
	#if(res == 0):
	#	if(dict1["thalach"] != ""):
	#		print(dict1["thalach"])
	#		if(dict1["slope"] != ""):
	#			print(dict1["slope"])
	#			if(dict1["oldpeak"] != ""):
	#				print(dict1["oldpeak"]
	#print(dict1,file = sys.stdout)
	return res,dict1

@app.route('/res', methods = ['POST']) 
def result(): 
    if request.method == 'POST': 
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values()) 
        to_predict_list.remove("Submit")
        print(to_predict_list,file = sys.stdout)
        to_predict_list = list(map(float, to_predict_list))
        str1,dict1      = tree(to_predict_list[0],to_predict_list[1],to_predict_list[2],to_predict_list[3],to_predict_list[4],to_predict_list[5],to_predict_list[6],to_predict_list[7]) 
        result,lis = ValuePredictor(to_predict_list)
        print(dict1,file = sys.stdout)
        return render_template("result.html", result = result , dict1 = dict1)  

