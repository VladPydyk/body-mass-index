name_user = input('Привет! Как тебя зовут?: ')
mass_user = input(f'{name_user}, позволь поинтересоваться, какой у тебя вес (в кг): ')
height_user = input(f'{name_user}, подскажи, пожалуйста, какой у тебя рост (в см): ')
arr_mass_index = [40,35,30,25,18,16]

med_findings = {
    1: 'тебе необходимо посетить врача! У тебя ожирение третьей степени!',
    2: 'тебе срочно нужно заняться собой! У тебя ожирение второй степени',
    3: 'тебе стоит привести себя в форму. У тебя ожирение первой степени',
    4: 'я вынужден сообщить, что у тебя чрезмерная масса тела',
    5: 'Супер! Твой ИМТ в норме!',
    6: 'к сожалению, у тебя недостаток массы тела'
}

med_recommendation = {
    1: 'Необходима консультация врача по составлению диеты.',
    2: 'Необходима консультация врача по составлению диеты.',
    3: 'Соблюдай дефецит каллорий, вводи интервальное голодание, больше двигайся',
    4: 'Соблюдай дефецит каллорий, больше двигайся',
    5: 'Ты питаешься правильно! Продолжай в том же духе и со здоровьем проблем не будет.',
    6: 'Кушай мясо, яйца, морскую рыбу, твердые сыры, творог, крупы, овощи и фрукты.'
}

def calculation_index_mass_body(mass, height):
    i = 0
    for mass_index in arr_mass_index:
        i += 1
        if (mass/((height/100)**2) - mass_index) >= 0:
            return i
            break

def findings(index):
    return med_findings.get(index, 'что не так, давай начнем с начала...')

def recommendation(index):
    try:
        answer_user = input('Тебе нужен совет о правильном питании?:').lower()
        if answer_user == 'да':
            print(med_recommendation.get(index, 'что не так, давай начнем с начала...'))
        elif answer_user == 'нет':
            print('Ну и зря!')
        else:
            print('Я не понял тебя, но удачи)')
    except:
        print(f'Что-то не то, давай еще раз...')

try:
    index_user = calculation_index_mass_body(float(mass_user), float(height_user))
    findings_body_mass = findings(int(index_user))
except:
    print('Не корректное значение...')

print(f'{name_user}, {findings_body_mass}.')

recommendation = recommendation(index_user)

close_program = input('Пока)')