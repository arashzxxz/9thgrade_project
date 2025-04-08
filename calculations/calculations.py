
def calculate_bmi(height,weight):
    height2=height/100
    height_s=height2*height2
    bmi=weight/height_s
    return round(bmi,1)
def calculate_ideal_weight(age,gender,height,bmi):
    males_avg = [  
        (71.12 + 81.28) / 2,  # Age 2  
        (80.01 + 91.44) / 2,  # Age 3  
        (87.63 + 102.87) / 2, # Age 4  
        (93.98 + 109.22) / 2, # Age 5  
        (106.68 + 124.46) / 2, # Age 6  
        (114.3 + 137.16) / 2, # Age 7  
        (127 + 147.32) / 2,   # Age 8  
        (137.16 + 160.02) / 2, # Age 9  
        (139.7 + 152.4) / 2,  # Age 10  
        (142.24 + 162.56) / 2, # Age 11  
        (149.86 + 171.45) / 2, # Age 12  
        (152.4 + 171.45) / 2,  # Age 13  
        (162.56 + 172.72) / 2, # Age 14  
        (165.1 + 172.72) / 2,  # Age 15  
        (167.64 + 172.72) / 2, # Age 16  
        (170.18 + 172.72) / 2, # Age 17  
        (167.64 + 173.99) / 2   # Age 18  
    ]  
    females_avg = [  
        (68.58 + 78.74) / 2,  # Age 2  
        (80.01 + 91.44) / 2,  # Age 3  
        (87.63 + 101.6) / 2,  # Age 4  
        (93.98 + 108.0) / 2,  # Age 5  
        (106.68 + 124.46) / 2, # Age 6  
        (114.3 + 137.16) / 2, # Age 7  
        (127 + 149.86) / 2,   # Age 8  
        (137.16 + 160.02) / 2, # Age 9  
        (139.7 + 149.86) / 2, # Age 10  
        (142.24 + 152.4) / 2, # Age 11  
        (149.86 + 171.45) / 2, # Age 12  
        (152.4 + 172.72) / 2,  # Age 13  
        (162.56 + 172.72) / 2, # Age 14  
        (165.1 + 172.72) / 2,  # Age 15  
        (167.64 + 172.72) / 2, # Age 16  
        (170.18 + 172.72) / 2, # Age 17  
        (167.64 + 173.99) / 2   # Age 18  
    ]  
    ideal_weight=0
    if age<19:
        if gender=="male":
            ideal_weight=2.27*age+10.5+(0.5*(height-males_avg[age-1]))
        if gender=="female":
            ideal_weight=2.27*age+11+(0.5*(height-females_avg[age-1]))
    else:
        ideal_weight=bmi*(height/100)*(height/100)
    return round(ideal_weight,1)

def calorys_needed_per_day(weight, ideal_weight, days, gender, height, age, activity_level):  
    weight_loss = weight - ideal_weight  
    daily_caloric_deficit = (weight_loss * 3500) / days  
    
    if gender == "male":  
        total_daily_caloric_needs = 10 * weight + 6.25 * height - 5 * age + 5  
    else:  
        total_daily_caloric_needs = 10 * weight + 6.25 * height - 5 * age - 161  

    if activity_level == 'sedentary':  
        total_daily_caloric_needs *= 1.2  
    elif activity_level == 'lightly_active':  
        total_daily_caloric_needs *= 1.375  
    elif activity_level == 'moderately_active':  
        total_daily_caloric_needs *= 1.55  
    elif activity_level == 'very_active':  
        total_daily_caloric_needs *= 1.725  
    elif activity_level == 'super_active':  
        total_daily_caloric_needs *= 1.9  

    daily_caloric_intake = total_daily_caloric_needs - daily_caloric_deficit  
    return round(daily_caloric_intake, 1)


def string_to_list(string, separator=', '):  
    return string.split(separator) 
def list_to_string(list, separator=', '):  
    return separator.join(map(str, list)) 

def calculate_macronutrient_needed_perday(weight_kg, activity_level, age=None, sex=None):  
    activity_factors = {  
        'sedentary': (0.8, 3.0, 0.8),  
        'lightly_active': (1.0, 4.0, 1.0),  
        'moderately_active': (1.2, 5.0, 1.0),  
        'very_active': (1.6, 6.0, 1.2),  
        'super_active': (1.6, 8.0, 1.2)  
    }  


    protein_factor, carb_factor, fat_factor = activity_factors[activity_level]  

    if age is not None and age >= 50:  
        protein_factor = 1.2 if sex == 'male' else 1.0  

    daily_protein_needs = weight_kg * protein_factor  
    daily_carb_needs = weight_kg * carb_factor  
    daily_fat_needs = weight_kg * fat_factor  
    #all in grams :
    macronutrient_needs = {  
        'protein': daily_protein_needs,  
        'carbohydrates': daily_carb_needs,  
        'fat': daily_fat_needs  
    }  
    
    return macronutrient_needs  

