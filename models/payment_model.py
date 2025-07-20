def validate_payment(data):
    """
    Verifica que los datos del pago contengan los campos requeridos.

    Parámetros:
        data (dict): Diccionario con los datos enviados por el usuario (por ejemplo desde un formulario).

    Retorna:
        tuple:
            - True, None si todos los campos requeridos están presentes y no vacíos.
            - False, mensaje de error si falta algún campo o está vacío.
    """
    
    # Define los campos que son obligatorios para el registro de un pago
    required_fields = ["email","paymentMethod","amount", "donationDate"]

    # Recorre cada campo obligatorio
    for field in required_fields:
        # 1. Verificar si el campo existe en los datos
        if field not in data:
            return False, f"El campo '{field}' es obligatorio."

        value = data[field]

        # 2. Validar el contenido según el tipo de campo esperado
        if field in ["email", "paymentMethod", "donationDate"]:
            # Para campos de texto: verificar que sea una cadena y no esté vacía/solo espacios
            if not isinstance(value, str) or not value.strip():
                return False, f"El campo '{field}' es obligatorio y no puede estar vacío."
        elif field == "amount":
            # Para el campo 'amount': verificar que sea un número (int o float) y sea positivo
            if not isinstance(value, (int, float)) or value <= 0:
                return False, "El campo 'amount' debe ser un número positivo."


    # Si todos los campos están presentes y válidos, devuelve True y None (sin mensaje de error)
    return True, None
