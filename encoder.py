from float_to_binary import floatToFracBin
from math import ceil, log2


class GilbertMoureEncode:
    alphabet = ['+', '-', '*', '/', '=']
    probability = []
    omega = []
    encodedAlphabet = []


    def __init__(self):

        f = open('probability.txt', 'r')
        probability = str(f.read())
        probability = probability.split()
        self.probability = list(map(float, probability))


        #инициализация списка кумулятивных вероятностей
        self.QProbability = [0]
        for i in range(1, len(self.probability)):
            s = 0
            for elem in self.probability[:i]:
                s += elem
            self.QProbability.append(s)
            
        #инициализация списка омега
        for p, q in zip(self.probability, self.QProbability):
            self.omega.append(p/2 + q)

        #составление нового алфавита
        for p, o in zip(self.probability, self.omega):
            frac = floatToFracBin(o)
            while len(frac) < ceil(-log2(p/2)):
                frac += '0'
            self.encodedAlphabet.append( frac[:ceil(-log2(p/2))] )


    #кодирование сообщения
    def encode(self, message):
        out = ''
        for symbol in message:
            out += self.encodedAlphabet[self.alphabet.index(symbol)]
        return out


    #декодирование сообщения
    def decode(self, message):
        alpha = ''
        out = ''
        for i in message:
            alpha += i
            if alpha in self.encodedAlphabet:
                out += self.alphabet[self.encodedAlphabet.index(alpha)]
                alpha = ''
        return out