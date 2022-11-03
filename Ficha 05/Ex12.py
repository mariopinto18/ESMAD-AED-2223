
def romanNumeral(number):
    """
    receives a number and returns the correspondent Roman numeral
    """
    snumber = '{:0>3}'.format(number)
    result=''
    
# CENTENAS
    if snumber[0]== '1':
        result+= 'C'
    elif snumber[0] == '2':
        result+= 'CC'
    elif snumber[0] == '3':
        result+= 'CCC'
    elif snumber[0] == '4':
        result+= 'CD'
    elif snumber[0] == '5':
        result+= 'D'
    elif snumber[0] == '6':
        result+= 'DC'
    elif snumber[0] == '7':
        result+= 'DCC'
    elif snumber[0] == '8':
        result+= 'DCCC'
    elif snumber[0] == '9':
        result+= 'CM'    
# DEZENAS
    if snumber[1]== '1':
        result+= 'X'
    elif snumber[1] == '2':
        result+= 'XX'
    elif snumber[1] == '3':
        result+= 'XXX'
    elif snumber[1] == '4':
        result+= 'XL'
    elif snumber[1] == '5':
        result+= 'L'
    elif snumber[1] == '6':
        result+= 'LX'
    elif snumber[1] == '7':
        result+= 'LXX'
    elif snumber[1] == '8':
        result+= 'LXXX'
    elif snumber[1] == '9':
        result+= 'XC'
  # UNIDADES
    if snumber[2]== '1':
        result+= 'I'
    elif snumber[2] == '2':
        result+= 'II'
    elif snumber[2] == '3':
        result+= 'III'
    elif snumber[2] == '4':
        result+= 'IV'
    elif snumber[2] == '5':
        result+= 'V'
    elif snumber[2] == '6':
        result+= 'VI'
    elif snumber[2] == '7':
        result+= 'VII'
    elif snumber[2] == '8':
        result+= 'VIII'
    elif snumber[2] == '9':
        result+= 'IX'
        
    return result



while True:
    try:
        number = int(input("Número:"))
        if number <=0 or number > 999:
            raise ValueError()
    except ValueError:
        print('O número inserido não é válido. Tente novamente!')
    except:
        print ('Ocorreu algum problema na inserção do número. Tente novamente!')
    else:
        break
print('Número: {0}, Númeração Romana: {1}' .format(number, romanNumeral(number)))

