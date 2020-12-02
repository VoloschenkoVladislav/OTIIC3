from encoder import GilbertMoureEncode
from even_encoder import isEven

#Умножение вектора на матрицу при помощи оператора "исключающее или"
def makeNewHemmingElem(code, G):
    code = list(code)
    newCode = ''

    if not len(code) == len(G):
        return False

    for i in range(len(G[0])):
        symbol = 0
        for j in range(len(code)):
            symbol += int(code[j]) * G[j][i]
 
        newCode += '1' if symbol % 2 else '0'

    return newCode


#Класс кодера с исправлением одиночных ошибок
class HemmingEncoder:

    alphabet = []
    encodedAlphabet = []

    # Проверочная матрица
    H = [
            [1, 1, 0],
            [1, 1, 1],
            [0, 1, 1],
            [1, 0, 1],
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]

    # Порожающая матрица
    G = [
            [1, 0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 0, 1],
        ]

    # Инициализатор: составление нового алфавита,
    # посредством умножения исходных кодовых слов на порождающую матрицу G
    def __init__(self):
        f = open('alphabet.txt')
        alphabet = str(f.read())
        self.alphabet = alphabet.split()

        for i in self.alphabet:
            self.encodedAlphabet.append(makeNewHemmingElem(i, self.G))

        
    # Кодер: подстановка вместо исходных кодовых слов закодированных
    def encode(self, message):
        out = ''

        l = len(self.alphabet[0])

        if len(message) % l:
            return False
        
        for i in range(int(len(message) / l)):
            out += self.encodedAlphabet[self.alphabet.index(message[i*l:i*l+l])]

        return out


    # Декодер: исправление ошибок и вывод исходного сообщения,
    # а также ошибок в виде:
    # (раскодированное_сообщение, [(номер_слова, позиция_ошибочного_бита)]) 
    def decode(self, message):
        out = ''
        error = []

        l = len(self.encodedAlphabet[0])

        if len(message) % l:
            return False

        for i in range(int(len(message) / l)):
            symbol = message[i*l:i*l+l]
            # Получаем одну из строк матрицы H посредством умножения каждого слова на H
            errorPlace = makeNewHemmingElem(symbol, self.H)

            if int(errorPlace, 2):
                # Положение данной строки в матрице H отвечает за положение ошибки в слове
                errorPlace = self.H.index(list(map(int, list(errorPlace))))
                if symbol[errorPlace] == '1':
                    symbol = symbol[:errorPlace] + '0' + symbol[errorPlace + 1:] 
                else:
                    symbol = symbol[:errorPlace] + '1' + symbol[errorPlace + 1:]

                error.append( (i, int(errorPlace)) )

            out += self.alphabet[self.encodedAlphabet.index(symbol)]

        return (out, error)