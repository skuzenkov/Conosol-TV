class TV():
    condition = False

    def __init__(self, id, chanel, volume):
        self.id = id
        self.chanel = chanel
        self.volume = volume

    def channels(self):
        print('Имя канала:', self.id, ', номер канала:', self.chanel, ', уровень звука:', self.volume)

    def PowerON(self):
        global condition
        self.condition = True

    def PowerOFF(self):
        global condition
        self.condition = True

    def isPower(self):
        global condition
        return condition

    def ControlPower():
        print('Включите телевизор: кнопка ON/OFF')
        while True:
            if isPower(self):
                continue
            text = input()
            if text == 'ON':
                print('Телевизор включен!')
                channels()
                return PowerON()
            elif text == 'OFF':
                print('Телевизор выключен!')
                PowerOFF()
                break
            else:
                print('Нажмите кнопку включения!')

    ControlPower()


channels1 = TV('Disney Chanel', 1, 20)
channels2 = TV('CNN', 2, 20)
channels3 = TV('Fox News', 3, 20)
channels4 = TV('History Chanel', 4, 20)

channels1.channels()
channels2.channels()
channels3.channels()
channels4.channels()
