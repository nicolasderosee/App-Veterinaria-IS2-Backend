from flask import Blueprint, jsonify, request
from models.MMascota import Mascota
from utils.db import db

mascota = Blueprint('mascota', __name__)


@mascota.route("/mascota/add", methods=["POST"])
def agregar_usuario():
    nombre = request.json.get("nombre")
    edad = request.json.get("edad")
    raza = request.json.get("raza")
    color = request.json.get("color")
    tamano = request.json.get("tamano")
    sexo = request.json.get("sexo")
    usuario_id = request.json.get("usuario_id")

    # Validar los datos del formulario aquí si es necesario

    nuevo_mascota = Mascota(nombre=nombre, edad=edad, raza=raza, color=color, tamano=tamano, sexo=sexo, usuario_id=usuario_id)
    db.session.add(nuevo_mascota)
    db.session.commit()

    return "Mascota agregado satisfactoriamente"


@mascota.route("/mascota/get", methods=["GET"])
def obtener_usuarios():
    mascotas = Mascota.query.all()
    mascotas_json = [
        {
            "id": mascota.id,
            "nombre": mascota.nombre,
            "edad": mascota.edad,
            "raza": mascota.raza,
            "color": mascota.color,
            "tamano": mascota.tamano,
            "sexo": mascota.sexo,
            "usuario_id": mascota.usuario_id,
        }
        for mascota in mascotas
    ]
    return jsonify(mascotas_json)

@mascota.route("/mascota/getById/<id>", methods=["GET"])
def obtener_mascota_by_id(id):
    mascota = Mascota.query.filter_by(id=id).first()
    mascota_json = {
            "id": mascota.id,
            "nombre": mascota.nombre,
            "edad": mascota.edad,
            "raza": mascota.raza,
            "color": mascota.color,
            "tamano": mascota.tamano,
            "sexo": mascota.sexo,
            "usuario_id": mascota.usuario_id,
        }
    return jsonify(mascota_json)

@mascota.route("/mascota/put/<id>", methods=["PUT"])
def modificar_usuario(id):
    mascota = Mascota.query.get(id)
    if not mascota:
        return jsonify({"error": "Mascota no encontrado"}), 404

    # Obtén los nuevos datos del formulario o solicitud
    nombre = request.json.get("nombre")
    edad = request.json.get("edad")
    raza = request.json.get("raza")
    color = request.json.get("color")
    tamano = request.json.get("tamano")
    sexo = request.json.get("sexo")
    usuario_id = request.json.get("usuario_id")

    # Actualiza los campos del turno existente
    mascota.nombre = nombre
    mascota.edad = edad
    mascota.raza = raza
    mascota.color = color
    mascota.tamano = tamano
    mascota.sexo = sexo
    mascota.usuario_id = usuario_id

    # Guarda los cambios en la base de datos
    db.session.commit()

    return jsonify({"message": "Mascota actualizado satisfactoriamente"})

@mascota.route("/mascota/delete/<id>", methods=["DELETE"])
def eliminar_usuario(id):
    mascota = Mascota.query.get(id)
    if not mascota:
        return jsonify({"error": "Mascota no encontrado"}), 404

    db.session.delete(mascota)
    db.session.commit()

    return jsonify({"message": "Mascota eliminado satisfactoriamente"})

@mascota.route("/mascota/getByUsuarioId/<id>", methods=["GET"])
def buscar_por_nombre(id):
    mascotas = Mascota.query.filter_by(usuario_id=id)

    if not mascotas:
        return jsonify({"error": "Mascotas no encontradas"}), 404
    
    mascotas_json = [
       {
            "id": mascota.id,
            "nombre": mascota.nombre,
            "edad": mascota.edad,
            "raza": mascota.raza,
            "color": mascota.color,
            "tamano": mascota.tamano,
            "sexo": mascota.sexo,
            "usuario_id": mascota.usuario_id,
        }
        for mascota in mascotas
    ]

    return jsonify(mascotas_json)