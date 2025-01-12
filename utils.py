from datetime import datetime

def validar_entrada_numerica(caracter):
    # Permite solo dígitos y la tecla de retroceso
    return caracter.isdigit() or caracter == ""

def validar_entrada_data(data):
    try:
        datetime.fromisoformat(data)
        return True

    except Exception:
        return False