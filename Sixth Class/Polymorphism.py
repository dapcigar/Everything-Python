class Phone:
    def ring(self):
        print("Phone ringsa like this ----> Toon Toon")

    def vibrate(self):
        print("Phone Vibrate like this -------> Voon Voon")


class Nokia(Phone):
    def ring(self):
        print("Nokia Ring like this -----------> Pereeeen Pereeeen")

    def vibrate(self):
        print("Nokia Vibrates like this -----------> Rooooooo Pereeeen")


class Samsung(Phone):
    def ring(self):
        print("Samsung Ring like this -----------> Wooooooooooo Woooooooooo")

    def vibrate(self):
        print("Samsung Vibrates like this -----------> Grrrrrrrr Grrrrrrrrrr")


class Gadget:
    def poly(inst):
        inst.ring()
        inst.vibrate()


sam = Samsung()
Nok = Nokia()

Gadget.poly(sam)
Gadget.poly(Nok)
