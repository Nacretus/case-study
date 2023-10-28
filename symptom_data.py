symptoms = {
    "Abscess": {"redness", "testicular pain", "swelling"},
    "Acute encephalitis syndrome": {"vomiting", "fever", "headache", "confusion", "stiff neck"},
    "Alopecia (hair loss)": {"loss hair part head body"},
    "Alzheimer's disease": {"difficulty remembering recent event", "problem language", "mood swing", "disorientation"},
    "Anxiety": {"fast heart rate", "worrying", "shakiness"},
    "Appendicitis": {"vomiting", "decreased appetite", "right lower abdominal pain"},
    "Arthritis": {"redness", "decreased range motion", "swelling", "stiffness", "joint bone pain"},
    "Asthma": {"shortness breath", "recurring episode wheezing", "chest tightness", "coughing"},
    "Astigmatism": {"headache", "distorted blurred vision distance", "eyestrain"},
    "Autism": {"trouble social interaction", "impaired communication", "restricted interest", "repetitive behavior"},
    "Bad Breath (Halitosis)": {"unpleasant smell present breath"},
    "Brain Tumour": {"vomiting", "vary depending part brain involved", "mental change", "headache", "problem vision", "seizure"},
    "Bell's Palsy": {"change taste", "inability move facial muscle one side", "pain around ear"},
    "Breast Cancer / Carcinoma": {"change breast shape", "dimpling skin", "fluid nipple", "lump breast", "newly inverted nipple", "red scaly patch skin breast"},
    "Bronchitis": {"chest discomfort", "wheezing", "shortness breath", "coughing mucus"},
    "Carbon monoxide poisoning": {"vomiting", "headache", "muscle weakness", "confusion", "dizziness", "chest pain"},
    "Cancer": {"abnormal bleeding", "change bowel movement", "lump breast", "prolonged cough", "unexplained weight loss"},
    "Chlamydia": {"discharge penis", "burning urination", "vaginal discharge"},
    "Cholera": {"vomiting", "muscle cramp", "large amount watery diarrhea"},
    "Common cold": {"barky cough", "fever", "runny nose", "sore throat"},
    "Coronary Heart Disease": {"chest pain", "shortness breath"},
    "Coronavirus disease 2019 (COVID-19)": {"fever", "barky cough", "shortness breath", "sometimes symptom", "loss smell", "fatigue"},
    "Cough": {"runny nose", "fever", "barky cough"},
    "Dehydration": {"nausea", "headache", "dizziness", "profuse sweating", "fatigue"},
    "Dengue": {"fever", "muscle joint pain", "headache", "maculopapular rash"},
    "Diabetes Mellitus": {"frequent urination", "increased hunger", "increased thirst"},
    "Diabetic Retinopathy": {"vision loss", "blurry vision", "may symptom", "blindness"},
    "Diarrhea": {"loose frequent bowel movement", "dehydration"},
    "Ear infection": {"fever", "ear pain", "hearing loss"}
}
all_symptoms = [symptom for symptom_list in symptoms.values() for symptom in symptom_list]
unique_symptoms = set(all_symptoms)
sorted_unique_symptoms = sorted(unique_symptoms) #<--- eto yung nag hahawak ng symptoms

#print(sorted_unique_symptoms)
