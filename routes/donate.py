from flask import Blueprint, request, jsonify
from core.db import db  # Conexión a la base de datos MongoDB
from models.payment_model import validate_payment # Validación de datos del usuario
from utils.security import hash_password, verify_password  # Funciones para manejo seguro de contraseñas

# Crea un blueprint para el módulo de autenticación
donations = Blueprint("donations", __name__)

# Accede a la colección 'users' de la base de datos
donations_collection = db["donations"]

# Ruta para registrar nuevos usuarios
@donations.route("/donate", methods=["POST"])
def register():
    data = request.json  # Obtiene los datos enviados en formato JSON
    # Valida que todos los campos requeridos estén presentes y no vacíos
    valid, error = validate_payment(data)
    if not valid:
        return jsonify({"msg": error}), 400  # Si hay error, responde con mensaje y código 400


    # Inserta el nuevo pago en la base de datos
    donations_collection.insert_one({
        "email": data["email"],
        "paymentMethod": data["paymentMethod"],
        "amount": data["amount"],
        "donationDate": data["donationDate"]
    })

    # Respuesta exitosa
    return jsonify({"msg": "Donación registrada exitosamente"}), 201

from pymongo import DESCENDING

@donations.route("/donations", methods=["GET"])
def get_donations_by_email():
    email = request.args.get("email")
    if not email:
        return jsonify({"msg": "Falta el parámetro 'email' en la consulta"}), 400

    # Busca las donaciones por correo, ordenadas por fecha descendente
    donations = list(
        donations_collection.find({"email": email}).sort("donationDate", DESCENDING)
    )

    # Convierte ObjectId y fechas a strings legibles (si es necesario)
    for donation in donations:
        donation["_id"] = str(donation["_id"])  # convierte ObjectId a string
        if "donationDate" in donation:
            try:
                # Normaliza fechas si están en formato ISO (MongoDB puede devolver datetime)
                donation["donationDate"] = str(donation["donationDate"])
            except Exception:
                pass

    return jsonify(donations), 200

@donations.route('/error')
def error():
    return "Algo falló", 500