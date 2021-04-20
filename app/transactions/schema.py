from marshmallow import Schema, fields

class TransactionSchema(Schema):
  id = fields.Int(required=True)
  service = fields.Int(required=True)
  volume = fields.Int(required=True)
  recipient = fields.Str(required=True)
