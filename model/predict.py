import pickle
import pandas as pd

#importing the ml model 
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

#model flow
MODEL_VERSION = "1.0.0"

#get classes form the model
class_labels = model.classes_.tolist()


def predict_output(user_input: dict):

    df = pd.DataFrame([user_input])

    #predict the class
    predicted_class = model.predict(df)[0]

    #get prob of all class
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)

    #create mapping of class and prob
    class_probs =dict(zip(class_labels, map(lambda p: round(p,4), probabilities)))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence,4),
        "class_probabilities": class_probs
    }
    # output = model.predict(input_df)[0]
    
    # return output
