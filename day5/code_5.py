f = open("input.txt", "r")

def fill_array_with_ranges_tuple(line, array):
    line = line[:-1]
    destination_range_start, source_range_start, elm_range = map(int, line.split(' '))
    array.append([
        (source_range_start, source_range_start + elm_range - 1),
        destination_range_start - source_range_start
    ])

_, *seeds = f.readline().split(' ')
seeds = list(map(int, seeds))

seed_to_soil_ranges = []
soil_to_fertilizer_ranges = []
fertilizer_to_water_ranges = []
water_to_lights_ranges = []
light_to_temperature_ranges = []
temperature_to_humidity_ranges = []
humidity_to_location_ranges = []

tracker = None

for line in f:

    if line == '\n':
        continue

    match line:
        case 'seed-to-soil map:\n':
            tracker = 'seed_to_soil'
            continue
        case 'soil-to-fertilizer map:\n':
            tracker = 'soil_to_fertilizer'
            continue
        case 'fertilizer-to-water map:\n':
            tracker = 'fertilizer_to_water'
            continue
        case 'water-to-light map:\n':
            tracker = 'water_to_light'
            continue
        case 'light-to-temperature map:\n':
            tracker = 'light_to_temperature'
            continue
        case 'temperature-to-humidity map:\n':
            tracker = 'temperature_to_humidity'
            continue
        case 'humidity-to-location map:\n':
            tracker = 'humidity_to_location'
            continue

    match tracker:
        case 'seed_to_soil':
            fill_array_with_ranges_tuple(line, seed_to_soil_ranges)
        case 'soil_to_fertilizer':
            fill_array_with_ranges_tuple(line, soil_to_fertilizer_ranges)
        case 'fertilizer_to_water':
            fill_array_with_ranges_tuple(line, fertilizer_to_water_ranges)
        case 'water_to_light':
            fill_array_with_ranges_tuple(line, water_to_lights_ranges)
        case 'light_to_temperature':
            fill_array_with_ranges_tuple(line, light_to_temperature_ranges)
        case 'temperature_to_humidity':
            fill_array_with_ranges_tuple(line, temperature_to_humidity_ranges)
        case 'humidity_to_location':
            fill_array_with_ranges_tuple(line, humidity_to_location_ranges)
        case _:
            pass

locations = []

for seed in seeds:
    soil, fertilizer, water, light, temperature, humidity, location = -1,-1,-1,-1,-1,-1,-1
    for seed_to_soil_range, offset in seed_to_soil_ranges:
        if seed >= seed_to_soil_range[0] and seed <= seed_to_soil_range[1]:
            soil = seed + offset
    if soil == -1:
        soil = seed
    for soil_to_fertilizer_range, offset in soil_to_fertilizer_ranges:
        if soil >= soil_to_fertilizer_range[0] and soil <= soil_to_fertilizer_range[1]:
            fertilizer = soil + offset
    if fertilizer == -1:
        fertilizer = soil
    for fertilizer_to_water_range, offset in fertilizer_to_water_ranges:
        if fertilizer >= fertilizer_to_water_range[0] and fertilizer <= fertilizer_to_water_range[1]:
            water = fertilizer + offset
    if water == -1:
        water = fertilizer
    for water_to_light_range, offset in water_to_lights_ranges:
        if water >= water_to_light_range[0] and water <= water_to_light_range[1]:
            light = water + offset
    if light == -1:
        light = water
    for light_to_temperature_range, offset in light_to_temperature_ranges:
        if light >= light_to_temperature_range[0] and light <= light_to_temperature_range[1]:
            temperature = light + offset
    if temperature == -1:
        temperature = light
    for temperature_to_humidity_range, offset in temperature_to_humidity_ranges:
        if temperature >= temperature_to_humidity_range[0] and temperature <= temperature_to_humidity_range[1]:
            humidity = temperature + offset
    if humidity == -1:
        humidity = temperature
    for humidity_to_location_range, offset in humidity_to_location_ranges:
        if humidity >= humidity_to_location_range[0] and humidity <= humidity_to_location_range[1]:
            location = humidity + offset
    if location == -1:
        location = humidity

    locations.append(location)
    print(f"Seed: {seed}, Soil: {soil}, Fertilizer: {fertilizer}, Water: {water}, Light: {light}, Temperature: {temperature}, Humidity: {humidity}, Location: {location}")

print(min(locations))
