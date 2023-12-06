# f = open("sample.txt", "r")

# def fill_array_with_ranges_tuple(line, array):
#     line = line[:-1]
#     destination_range_start, source_range_start, elm_range = map(int, line.split(' '))
#     array.append([
#         (source_range_start, source_range_start + elm_range - 1),
#         destination_range_start - source_range_start
#     ])

# _, *seeds = f.readline().split(' ')
# seeds = list(map(int, seeds))

# seed_to_soil_ranges = []
# soil_to_fertilizer_ranges = []
# fertilizer_to_water_ranges = []
# water_to_lights_ranges = []
# light_to_temperature_ranges = []
# temperature_to_humidity_ranges = []
# humidity_to_location_ranges = []

# tracker = None

# for line in f:

#     if line == '\n':
#         continue

#     match line:
#         case 'seed-to-soil map:\n':
#             tracker = 'seed_to_soil'
#             continue
#         case 'soil-to-fertilizer map:\n':
#             tracker = 'soil_to_fertilizer'
#             continue
#         case 'fertilizer-to-water map:\n':
#             tracker = 'fertilizer_to_water'
#             continue
#         case 'water-to-light map:\n':
#             tracker = 'water_to_light'
#             continue
#         case 'light-to-temperature map:\n':
#             tracker = 'light_to_temperature'
#             continue
#         case 'temperature-to-humidity map:\n':
#             tracker = 'temperature_to_humidity'
#             continue
#         case 'humidity-to-location map:\n':
#             tracker = 'humidity_to_location'
#             continue

#     match tracker:
#         case 'seed_to_soil':
#             fill_array_with_ranges_tuple(line, seed_to_soil_ranges)
#         case 'soil_to_fertilizer':
#             fill_array_with_ranges_tuple(line, soil_to_fertilizer_ranges)
#         case 'fertilizer_to_water':
#             fill_array_with_ranges_tuple(line, fertilizer_to_water_ranges)
#         case 'water_to_light':
#             fill_array_with_ranges_tuple(line, water_to_lights_ranges)
#         case 'light_to_temperature':
#             fill_array_with_ranges_tuple(line, light_to_temperature_ranges)
#         case 'temperature_to_humidity':
#             fill_array_with_ranges_tuple(line, temperature_to_humidity_ranges)
#         case 'humidity_to_location':
#             fill_array_with_ranges_tuple(line, humidity_to_location_ranges)
#         case _:
#             pass

# def reverse_mapping(ranges):
#     reversed_ranges = []
#     for range_map in ranges:
#         source_range, destination_offset = range_map
#         source_start, source_end = source_range
#         for i in range(source_start, source_end + 1):
#             reversed_ranges.append((i + destination_offset, i))
#     return reversed_ranges

# location_to_humidity_ranges = reverse_mapping(humidity_to_location_ranges)
# humidity_to_temperature_ranges = reverse_mapping(temperature_to_humidity_ranges)
# temperature_to_light_ranges = reverse_mapping(light_to_temperature_ranges)
# light_to_water_ranges = reverse_mapping(water_to_lights_ranges)
# water_to_fertilizer_ranges = reverse_mapping(fertilizer_to_water_ranges)
# fertilizer_to_soil_ranges = reverse_mapping(soil_to_fertilizer_ranges)
# soil_to_seed_ranges = reverse_mapping(seed_to_soil_ranges)

# def chain_mappings(*mappings):
#     chained = mappings[0]
#     for mapping in mappings[1:]:
#         chained = [(src, dst) for src, _ in chained for _, dst in mapping if src == _]
#     return chained

# print(soil_to_fertilizer_ranges)