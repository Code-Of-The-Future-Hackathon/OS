import random
import json
 
training_data = [{}]

for i in range(12000):
    training_data.append({})
    training_data[i]['precipitation'] = random.randint(0, 8)
    training_data[i]['rain_intensity'] = random.randint(0, 40)
    training_data[i]['soil_moisture'] = random.randint(35, 100)
    training_data[i]['wind_speed'] = random.randint(0, 80)
    training_data[i]['relative_humidity'] = random.randint(40, 100)
    training_data[i]['temp_disparity'] = random.randint(-7, 7)
    training_data[i]['temperature'] = random.randint(-15, 30)
    training_data[i]['evapotranspiration'] = random.randint(1, 6) / 10
    
    if training_data[i]['temperature'] < 0 and training_data[i]['temperature'] + training_data[i]['temp_disparity'] > 0:
        training_data[i]['snowmelt'] = True
    else:
        training_data[i]['snowmelt'] = False
        
    landslide_chance_count = 0
    
    if training_data[i]['precipitation'] >= 4:
        landslide_chance_count += 1
    if training_data[i]['rain_intensity'] >= 15:
        landslide_chance_count += 1
    if training_data[i]['soil_moisture'] >= 75:
        landslide_chance_count += 1
    if training_data[i]['wind_speed'] >= 35:
        landslide_chance_count += 1
    if training_data[i]['relative_humidity'] >= 80:
        landslide_chance_count += 1
    if training_data[i]['snowmelt']:
        landslide_chance_count += 1
    if training_data[i]['evapotranspiration'] >= 0.45:
        landslide_chance_count += 1
        
    training_data[i]['chance'] = landslide_chance_count
    if landslide_chance_count >= 4:
        training_data[i]['is_landslide'] = True
    else:
        training_data[i]['is_landslide'] = False
        

with open("./training_data/landslide_training_data.json", 'w') as file:
    json.dump(training_data, file, indent=4)    