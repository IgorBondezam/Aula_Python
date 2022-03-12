class Errooo(Exception):
    pass

def testar():
    raise Errooo("Erradooo!!!!!!!")


try:
    testar()
except Errooo as e:
    print(f"Error: {e}")