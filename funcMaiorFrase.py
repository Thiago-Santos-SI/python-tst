string = 'eu acredito que seja um bom exemplo'


def maior_palavra(frase):
    stringCheck = ''
    string = ''
    for i in frase:
        if i != ' ':
            string += i
        else:
            if len(string) > len(stringCheck):
                stringCheck = string
                string = ''
            else:
                string = ''
    return stringCheck


string = 'eu acredito que seja um bom acreditooo exemplo'

print(maior_palavra(string))

