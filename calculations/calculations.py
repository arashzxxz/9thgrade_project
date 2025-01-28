
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
    if age<=19:
        if gender=="male":
            ideal_weight=2.27*age+10.5+(0.5*(height-males_avg[age-1]))
        if gender=="female":
            ideal_weight=2.27*age+11+(0.5*(height-females_avg[age-1]))
    else:
        ideal_weight=bmi*(height/100)*(height/100)
    return round(ideal_weight,1)
def calorys_needed_per_day(weight,ideal_weight,days,gender,height,age):
    weight_loss=weight-ideal_weight
    daily_caloric_deficit=(weight_loss*3500)/days
    if gender=="male":
        total_daily_caloric_needs=10*weight+6.25*height-5*age+5
    if gender=="female":
        total_daily_caloric_needs=10*weight+6.25*height-5*age-161
    daily_caloric_intake=total_daily_caloric_needs-daily_caloric_deficit
    return round(daily_caloric_intake,1)

