class Jogo:

    def __init__(self,nome,vezes_que_joguei):
        print("Construindo objeto... {}".format(self))
        self.__nome = nome
        self.__vezes_que_joguei = vezes_que_joguei

    def get_nome(self):
       return self.__nome

    def get_vezes_que_joguei(self):
       return self.__vezes_que_joguei

    def set_vezes_que_joguei(self,vezes_que_joguei):
        self.__vezes_que_joguei = vezes_que_joguei


