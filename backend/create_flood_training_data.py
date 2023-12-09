import random
import json
 
training_data = []

for i in range(12000):
    training_data.append({})
    training_data[i]['precipitation'] = random.randint(0, 8)
    training_data[i]['rain_intensity'] = random.randint(0, 40)
    training_data[i]['snow_depth'] = random.randint(1, 10) / 10
    training_data[i]['wind_speed'] = random.randint(0, 80)
    training_data[i]['cloud_cover'] = random.randint(40, 100)
    training_data[i]['temp_disparity'] = random.randint(-7, 7)
    training_data[i]['temperature'] = random.randint(-15, 30)
    training_data[i]['soil_moisture'] = random.randint(0, 100)
    
    if training_data[i]['temperature'] < 0 and training_data[i]['temperature'] + training_data[i]['temp_disparity'] > 0:
        training_data[i]['snowmelt'] = True
    else:
        training_data[i]['snowmelt'] = False
        
    flood_chance_count = 0
    
    if training_data[i]['precipitation'] >= 4:
        flood_chance_count += 1
    if training_data[i]['rain_intensity'] >= 20:
        flood_chance_count += 1
    if training_data[i]['snow_depth'] >= 0.5:
        flood_chance_count += 1
    if training_data[i]['wind_speed'] >= 20:
        flood_chance_count += 1
    if training_data[i]['cloud_cover'] >= 80:
        flood_chance_count += 1
    if training_data[i]['snowmelt']:
        flood_chance_count += 1
    if training_data[i]['soil_moisture'] >= 80:
        flood_chance_count += 1
        
    training_data[i]['chance'] = flood_chance_count
    if flood_chance_count >= 4:
        training_data[i]['is_flood'] = True
    else:
        training_data[i]['is_flood'] = False
        

with open("./training_data/flood_training_data.json", 'w') as file:
    json.dump(training_data, file, indent=4)    