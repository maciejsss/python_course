print('Nazwa modułu: ', __name__)

print('Nazwa drugiego modułu: ', __name__)

if __name__ == '__main__':
    print('uruchamiamy bezpośrednio')
else:
    print('uruchamiamy z importu')
