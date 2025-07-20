from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    """
    Genera un hash seguro de la contraseña.

    Parámetros:
    - password (str): La contraseña en texto plano ingresada por el usuario.

    Retorna:
    - str: Un hash encriptado de la contraseña, listo para ser almacenado en la base de datos.
    """
    return generate_password_hash(password)

def verify_password(password, hashed_password):
    """
    Compara una contraseña en texto plano con su versión hasheada.

    Parámetros:
    - password (str): La contraseña en texto plano proporcionada por el usuario en login.
    - hashed_password (str): El hash almacenado en la base de datos.

    Retorna:
    - bool: True si la contraseña coincide con el hash; False si no.
    """
    return check_password_hash(hashed_password, password)
