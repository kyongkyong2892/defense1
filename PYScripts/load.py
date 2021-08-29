import variables as var

var.file_card = open('../PYData/carddata.txt', 'r')

def data_load():
    temp_data = var.file_card.read().split('\n')
    temp_data.pop(0)

    for i in range(len(temp_data)):
        temp = temp_data[i].split(' ')

        var.card_data.append({'ID' : temp[0],
                              'Type' : temp[1],
                              'Element' : temp[2],
                              'Name' : temp[3],
                              'Level' : temp[4],
                              'Gold' : temp[5],
                              'Attack' : temp[6],
                              'Life' : temp[7],
                              'AttackU' : temp[8],
                              'LifeU' : temp[9],
                              'Weapon' : temp[10],
                              'Special' : temp[11],
                              'Play' : temp[12]})