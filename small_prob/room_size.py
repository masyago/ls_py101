# Build a program that asks the user to enter the length and width of a room,
# in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# SQR_METER_TO_SQR_FEET_CONVERSION = 10.7639

# room_length = input("Enter room length in meters: ")
# room_width = input("Enter room width in meters: ")

# room_area_meters = float(room_length) * float(room_width)
# room_area_sq_feet = room_area_meters * SQR_METER_TO_SQR_FEET_CONVERSION

# print(f'Room size is {room_area_meters:.2f} square meters or {room_area_sq_feet:.2f}'  # :2.f formats to 2 decimal points
#       f' square feet')
      
# Modify the program to let the user specify the measurement type (meters or feet). 
# Compute the area accordingly and print it and its conversion in parentheses.

SQR_METER_TO_SQR_FEET_CONVERSION = 10.7639

units_request = input("Choose units: enter 1 for meters, enter 2 for feet\n")
if units_request == '1':
    selected_units = 'meters'
    other_units = 'feet'
elif units_request == '2':
    selected_units = 'feet'
    other_units = 'meters'
    
room_length = input(f"Enter room length in {selected_units}: ")
room_width = input(f"Enter room width in {selected_units}: ")

room_area = float(room_length) * float(room_width)

# Conversion
if selected_units == 'meters':
    room_area_converted = room_area * SQR_METER_TO_SQR_FEET_CONVERSION
elif selected_units == 'feet':
    room_area_converted = room_area / SQR_METER_TO_SQR_FEET_CONVERSION

print(f'Room size is {room_area:.2f} square {selected_units}'
      f' ({room_area_converted:.2f} square {other_units}).')