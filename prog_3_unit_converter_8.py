"""Write a program that can calculate unit equivalencies such as feet to meters,
inches to centimeters, kg to pounds, and grams to pounds, etc. Give error messages for bad input.
Use a list and dictionaries insted of a bunch of 'if' statements. Make sure that if the number is 1,
that singular unit is displayed in the output (ex. inch instead of inches)"""

#create a list of aceptabl eunit values
unit_vals = ['inches', 'feet', 'centimeters', 'meters', 'pounds', 'grams', 'kilograms']

#create a dictionary of unit conversion values
unit_dic = {'inches_to_centimeters' : 2.54, 'centimeters_to_inches' : 1/2.54, 'feet_to_inches' : 12, 'inches_to_feet' : 1/12, 'meters_to_inches' : 39.9071, 'inches_to_meters' : 1/39.9071,
'feet_to_centimeters' : 30.48, 'centimeters_to_feet' : 1/30.48, 'meters_to_centimeters' : 100, 'centimeters_to_meters' : 1/100, 'meters_to_feet' : 3.28084, 'feet_to_meters' : 1/3.28084,
'pounds_to_grams' : 453.592, 'grams_to_pounds' : 1/453.592, 'kilograms_to_pounds' : 2.20462, 'pounds_to_kilograms' : 1/2.20462, 'kilograms_to_grams' : 1000, 'gram_to_kilograms' : 1/1000,
'feet_to_feet' : 1, 'inches_to_inches' : 1, 'centimeters_to_centimeters' : 1, 'meters_to_meters' : 1, 'pound_to_pound' : 1, 'grams_to_grams' : 1, 'kilograms_to_kilograms' : 1}

#create dictionary of single unit values
single_unit_dic = {'inches' : 'inch', 'feet' : 'foot', 'centimeters' : 'centimeter', 'meters' : 'meter', 'pounds' : 'pound', 'grams' : 'gram', 'kilograms' : 'kilogram'}

#create a function to do unit conversion that takes three parameters (n_in, u_in, u_out)
def unit_converter(n_in, u_in, u_out):
    #convert n_in to a float
    n_in = float(n_in)
    #create an input phrase so that the proper conversion value can be obtained from the unit_dic
    input_phrase = u_in + '_to_' + u_out
    #calculate fin_out using the input number and conversion value
    fin_out = n_in * unit_dic.get(input_phrase)
    #change units to singular string for output if number in front of unit is 1
    if n_in == 1.0:
        u_in = single_unit_dic.get(u_in)
    if fin_out == 1.0:
        u_out = single_unit_dic.get(u_out)
    #return the conversion
    return print('{} {} is approximately {} {}'.format(n_in, u_in, fin_out, u_out))

#prompt the user for user_input - a number, original unit(s) and outputs, give error message for bad inputs and re-prompt, make sure the same unit type can't be entered for unit_in and unit_out
#prompt for the number of starting units, return an error if it is not a number
num_in = input('This program handles the following units: inches, feet, centimeters, meters, pounds, grams, and kilograms)\nPlease enter the NUMBER of units for the unit you are converting from:\n')
while True:
    try:
        num_in = float(num_in)
        break
    except ValueError:
        num_in = input('You must input a NUMBER:')

#prompt for the unit type the user wants to convert from. If it is not a valid unit, re-prompt
unit_in = input('Please input the UNIT TYPE that you want to convert FROM:\n').lower()
while unit_in not in unit_vals:
    unit_in = input("Please choose a valid unit ---\n(inches, feet, centimeters, meters, pounds, grams, kilograms)\nunit:").lower()

#prompt for the uit type the user wants to convert to. If it is not a valid unit or the same unit as the unit_in, re-prompt the user
unit_out = input('Please input the UNIT TYPE you want to convert TO:').lower()
while unit_out not in unit_vals:
        unit_out = input("Please choose a valid unit ---\n(inches, feet, centimeters, meters, pounds, grams, kilograms)\nunit:").lower()
        


#call the function
unit_converter(num_in, unit_in, unit_out)
