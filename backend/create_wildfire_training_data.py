import random
import json
 
training_data = []

for i in range(12000):
    training_data.append({})
    training_data[i]['temperature'] = random.randint(-15, 40)
    training_data[i]['relative_humidity'] = random.randint(0, 100)
    training_data[i]['dewpoint'] = random.randint(0, 8)
    training_data[i]['precipitation'] = random.randint(0, 5)
    training_data[i]['wind_speed'] = random.randint(0, 70)
    training_data[i]['cloud_cover'] = random.randint(0, 50)
    training_data[i]['soil_moisture'] = random.randint(0, 45)
    
    wildfire_chance_count = 0
    
    if training_data[i]['temperature'] >= 35:
        wildfire_chance_count += 1
    if training_data[i]['relative_humidity'] <= 20:
        wildfire_chance_count += 1
    if training_data[i]['dewpoint'] <= 10:
        wildfire_chance_count += 1
    if training_data[i]['precipitation'] == 0:
        wildfire_chance_count += 1
    if training_data[i]['wind_speed'] >= 25:
        wildfire_chance_count += 1
    if training_data[i]['cloud_cover'] <= 10:
        wildfire_chance_count += 1
    if training_data[i]['soil_moisture'] <= 15:
        wildfire_chance_count += 1
        
    training_data[i]['chance'] = wildfire_chance_count
    if wildfire_chance_count >= 4:
        training_data[i]['is_wildfire'] = True
    else:
        training_data[i]['is_wildfire'] = False
        

with open("./training_data/wildfire_training_data.json", 'w') as file:
    json.dump(training_data, file, indent=4)    