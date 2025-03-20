import csv
import math


#############################################
         
#    NAME OF THE CSV FILE
    
#############################################

# Define the name of the CSV file
csv_file = "lissajous_curve.csv"
function_name="Lissajous curve"
#############################################
         
#    CHANNELS AND VALUES
    
#############################################

# Define the two channels used in the trajectory streaming.
# IMPORTANT NOTE: Channel_A < Channel_B. e.g. Channel_A=0 and Channel_B=1
# This is due to the structure of the "Trajecotry Streaming" code.

Channel_A = 1
Channel_B = 2


# Define the range of values
# In the case of trigonometric functions the 0 to 360 values is used 
# (in this case the values represent degrees).
start_value = 0
end_value = 360


# Define the number of tuples (frames). Maximum values is 1024.
num_tuples = 1024

# Generate the values 
values = [start_value + (end_value - start_value) * i / (num_tuples-1) 
for i in range(num_tuples)]

#############################################
         
#    Parameters of the function
    
#############################################

# Define the parameters of the function. This  are specific to each function
# E.g. Define the parameters for the Lissajous curve
A = 1000000000  # Amplitude of oscillation in the x direction
B = 1000000000  # Amplitude of oscillation in the y direction
a = 3  # Frequency of oscillation in the x direction
b = 2  # Frequency of oscillation in the y direction
delta = math.pi / 2  # Phase difference (in radians)




# Write the values to a CSV file 
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header (this line gets ignored by the "trajectory streaming" code).
    writer.writerow(['Channel A', 'Position A', 'Channel B', 'Position B'])
    # Write the values and corresponding positions using  the function
    # In this case the Lissajous curve function is used.
    ##################################################
    #      PARAMETRIZATION OF THE FUNCTION
    ##################################################      
    for value in values:
        t = math.radians(value)  
        pos_chan_A = round(A * math.sin(a * t + delta))
        pos_chan_B = round(B * math.sin(b * t))
        # This line writes the channel name and positions in the CSV file.
        writer.writerow([Channel_A, int(pos_chan_A), Channel_B, int(pos_chan_B)])

# This commands prints a message in the terminal containing the information of 
# the  number of frames, name of the file, the values chosen and the name of the 
# function.
print(f"{num_tuples} frames on the CSV file '{csv_file}' with values from {start_value} to {end_value} and positions for a {function_name} has been generated.")
