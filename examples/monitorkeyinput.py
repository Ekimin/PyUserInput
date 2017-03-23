from pykeyboard.mac import PyKeyboardEvent


class KeyListener(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)


    def key_press(self, key):
        pass

    def key_release(self,key):
        print key


keyListener = KeyListener()
keyListener.run()
