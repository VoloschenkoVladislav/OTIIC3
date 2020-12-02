from encoder import GilbertMoureEncode

# Проверка слова на четность единиц
def isEven(string):
    outNum = 0
    for i in string:
        if i == '1':
            outNum += 1
    if outNum % 2 == 0:
        return True
    else:
        return False

# Класс кодера с обнаружением ошибок: наследуется от кодера по алгоритму Гильберта-Мура
class EvenEncode(GilbertMoureEncode):

    # Кодер
    def encode(self, message):

        out = ''
        for symbol in message:
            out += self.encodedAlphabet[self.alphabet.index(symbol)]
            out += '0' if isEven(self.encodedAlphabet[self.alphabet.index(symbol)]) else '1'
        return out


    # Декодер:
    # вывод сообщения в виде: (раскодированное_сообщение, [индекс_искажённого_слова])
    def decode(self, message):
        l = len(self.encodedAlphabet[0]) + 1

        out = ''
        errorPosition = []

        for i in range(int(len(message) / l)):
            word = message[i*l:i*l+l]
            if not isEven(word):
                out += '[error]'
                errorPosition.append(i)
            else:
                try:
                    out += self.alphabet[self.encodedAlphabet.index(word[:-1])]
                except:
                    out += '[error]'
                    errorPosition.append(i)

        return (out, errorPosition)