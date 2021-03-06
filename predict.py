import numpy as np
import pickle

def predict(babyage, ZONE, enroll_type2,enroll_age, open_rate0, 
            click_rate0, breastfed, formula, breastfed_and_formula,
            neither, redem_rate0, model_name):
    filename = model_name+".sav"
    #Loading the model from local storage
    model = pickle.load(open(filename,"rb"))
    y_pred= model.predict(
        np.array([
            [
                babyage, 
                ZONE, 
                enroll_type2,
                enroll_age,
                open_rate0,
                click_rate0,
                breastfed,
                formula,
                breastfed_and_formula,
                neither,
                redem_rate0
                ]]))

    
    return y_pred[0]