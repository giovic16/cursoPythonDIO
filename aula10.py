from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H: %M: %S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2010, 10, 10, 00, 35, 40)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2020 11: 34: 18'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H: %M: %S')
    print(type(data_convertida))
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=10, second=30)
    print(horario)

if __name__=='__main__':
    # trabalhando_com_time()
    # trabalhando_com_date()
    trabalhando_com_datetime()