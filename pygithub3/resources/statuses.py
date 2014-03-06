from .base import Resource

class Status(Resource):
    def __str__(self):
        return '<Status {0}>'.format(getattr(self, 'ref', ''))

# vim: ai et sts=4 ts=4 sw=4
