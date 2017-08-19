from db import session

from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with

from models import Doctor
from models import Review

doctor_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'reviews': fields.List,

}

review_fields = {
    'id': fields.Integer,
    'doctor_id': fields.Integer,
    'description' : fields.String


}
parser = reqparse.RequestParser()
class DoctorResource(Resource):
    @marshal_with(doctor_fields)
    def get(self,id):
        doctor = session.query(Doctor).filter(Doctor.id == id).first()
        if not doctor:
           abort(404, message="Doctor doesn't exist".format(id))
        return doctor

    def delete(self, id):
        doctor = session.query(Doctor).filter(Doctor.id == id).first()
        if not doctor:
           abort(404, message="Doctor doesn't exist".format(id))
        session.delete(doctor)
        session.commit()
        return 0

    def put(self,id):
        parsed_args = parser.parse_args()