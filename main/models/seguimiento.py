from .. import db
import datetime as dt
from flask import jsonify, request

class login(db.Model):
    
    correo = db.Column(db.Integer, primary_key=True)
    contra = db.Column(db.Integer, primary_key=True)
    
class seguimiento(db.Model):
    
    accion = db.Column(db.String(50), primary_key=True, nullable=True)
    numero_accion = db.Column(db.String(50), nullable=True)
    proceso = db.Column(db.String(50), nullable=True)
    correctiva = db.Column(db.String(50), nullable=True)
    mejora = db.Column(db.String(50), nullable=True)
    fecha_definicion = db.Column(db.String(50), nullable=True)
    fecha_cierre_propuesta = db.Column(db.String(50), nullable=True)
    fecha_cierre_real = db.Column(db.String(50), nullable=True)
    eficaz = db.Column(db.String(50), nullable=True)
    nueva_accion_al_no_ser_eficaz = db.Column(db.String(50), nullable=True)
    observaciones = db.Column(db.String(50), nullable=True)
    pendientes = db.Column(db.String(50), nullable=True)
    hallazgo = db.Column(db.String(50), nullable=True)
    
    def get(self):
        
        return jsonify({
            "accion": self.accion
        })
        
    
    
def to_json(self):
    seguimiento_json = {
        'accion': self.accion,
        'numero_accion': self.numero_accion,
        'proceso': self.proceso,
        'correctiva': self.correctiva,
        'mejora': self.mejora,
        'fecha_definicion': self.fecha_definicion,
        'fecha_cierre_propuesta': self.fecha_cierre_propuesta,
        'fecha_cierre_real': self.fecha_cierre_real,
        'eficaz': self.eficaz,
        'nueva_accion_al_no_ser_eficaz': self.nueva_accion_al_no_ser_eficaz,
        'observaciones': self.observaciones,
        'pendientes': self.pendientes,
        'hallazgo': self.hallazgo
    }    
    return seguimiento_json


@staticmethod 
def from_json(seguimiento_json):
    accion = seguimiento_json.get('accion')
    numero_accion = seguimiento_json.get('numero_accion')
    proceso = seguimiento_json.get('proceso')
    correctiva = seguimiento_json.get('correctiva')
    mejora = seguimiento_json.get('mejora')
    fecha_definicion = seguimiento_json.get('fecha_definicion')
    fecha_cierre_propuesta = seguimiento_json.get('fecha_cierre_propuesta')
    fecha_cierre_real = seguimiento_json.get('fecha_cierre_real')
    eficaz = seguimiento_json.get('eficaz')
    nueva_accion_al_no_ser_eficaz = seguimiento_json.get('nueva_accion_al_no_ser_eficaz')
    observaciones = seguimiento_json.get('observaciones')
    pendientes = seguimiento_json.get('pendientes')
    hallazgo = seguimiento_json.get('hallazgo')
    return seguimiento(
        accion = accion,
        numero_accion = numero_accion,
        proceso = proceso,
        correctiva = correctiva,
        fechamejora = mejora,
        fecha_definicion = fecha_definicion,
        fecha_cierre_propuesta = fecha_cierre_propuesta,
        fecha_cierre_real = fecha_cierre_real,
        eficaz = eficaz,
        nueva_accion_al_no_ser_eficaz = nueva_accion_al_no_ser_eficaz,
        observaciones = observaciones,
        pendientes = pendientes,
        hallazgo = hallazgo
    )