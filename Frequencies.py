frequecies = {  # stores the frequency table in a dictionary
    'Less than 3 × 10^9': 'Radio waves',
    '3 × 10^9 to less than 3 × 10^12': 'Microwaves',
    '3 × 10^12 to less than 4.3 × 10^14': 'Infrared Light',
    '4.3 × 10^14 to less than 7.5 × 10^14': 'Visible light',
    '7.5 × 10^14 to less than 3 × 10^17': 'Ultraviolet light',
    '3 × 10^17 to less than 3 × 10^19': 'X-rays',
    '3 × 10^19 or more': 'Gamma rays'
}

freqChecker = input('Please enter the frequency: ')  # asks user for input

print(frequecies[freqChecker])  # prints the results
