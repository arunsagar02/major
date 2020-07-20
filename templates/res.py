import numpy as np
import pickle


def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, 8) 
    loaded_model = pickle.load(open("model.pkl", "rb")) 
    result = loaded_model.predict(to_predict) 
    return result[0] 

def tree(thal, thalach, slope, exang, cp, oldpeak, ca, sex):
	res = 0
	dict1 = {"thalach" : "","slope" : "" , "oldpeak" : ""}
        if thal <= 2.5:
                if oldpeak <= 1.699999988079071:
                        if ca <= 0.5:
                                if thalach <= 158.5:
                                	dict1["oldpeak"] = "should be > 1.699"
                                	res = 1
                                        return chance of heart disease
                                else:  # if thalach > 158.5
                                	res = 1
                                        dict1["oldpeak"] = "should be > 2"
                                        return chance of heart disease
                        else:  # if ca > 0.5
                                if cp <= 0.5:
                                        return no chance of heart disease
                                else:  # if cp > 0.5
                                        if slope <= 1.5:
                                                if thal <= 1.5:
                                                        return no chance of heart disease
                                                else:  # if thal > 1.5
                                                        return chance of heart disease
                                        else:  # if slope > 1.5
                                        	res = 1
                                        	dict1["slope"] = "slope < 2"
                                                return chance of heart disease
                else:  # if oldpeak > 1.699999988079071
                        if cp <= 1.5:
                                return no chance of heart disease
                        else:  # if cp > 1.5
                                return chance of heart disease
        else:  # if thal > 2.5
                if oldpeak <= 0.7000000178813934:
                        if thalach <= 140.5:
                                if slope <= 1.5:
                                        return no chance of heart disease
                                else:  # if slope > 1.5
                                	res = 1
                                	dict1["slope"] = "slope <= 2"
                                	dict1["thalach"] = "thalach > 141"
                                	dict1["oldpeak"] = "oldpeak > 1"
                                        return chance of heart disease
                        else:  # if thalach > 140.5
                                if thalach <= 143.5:
                                        return no chance of heart disease
                                else:  # if thalach > 143.5
                                        if ca <= 0.5:
                                        	res = 1
                                        	dict1["thalach"] = "thalach <= 143.5"
                                                return chance of heart disease
                                        else:  # if ca > 0.5
                                                if thalach <= 155.0:
                                                        return no chance of heart disease
                                                else:  # if thalach > 155.0
                                                        return no chance of heart disease
                else:  # if oldpeak > 0.7000000178813934
                        if exang <= 0.5:
                                if cp <= 1.5:
                                        return no chance of heart disease
                                else:  # if cp > 1.5
                                        if oldpeak <= 1.949999988079071:
                                                if thalach <= 155.5:
                                                        return no chance of heart disease
                                                else:  # if thalach > 155.5
                                                	res = 1
                                                	dict1["thalach"] = "thalach <= 155.5"
                                                        return chance of heart disease
                                        else:  # if oldpeak > 1.949999988079071
                                                return no chance of heart disease
                        else:  # if exang > 0.5
                                return no chance of heart disease
	#if(res == 0):
	#	if(dict1["thalach"] != ""):
	#		print(dict1["thalach"])
	#		if(dict1["slope"] != ""):
	#			print(dict1["slope"])
	#			if(dict1["oldpeak"] != ""):
	#				print(dict1["oldpeak"]
	return dict1

@app.route('/res', methods = ['POST']) 
def result(): 
    if request.method == 'POST': 
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values()) 
        to_predict_list = list(map(int, to_predict_list))
        str1,dict1      = tree(to_predict_list[0],to_predict_list[1],to_predict_list[2],to_predict_list[3],to_predict_list[4],to_predict_list[5],to_predict_list[6],to_predict_list[7]) 
        result = ValuePredictor(to_predict_list)
        return render_template("result.html", result = result , dict1 = dict1)  
