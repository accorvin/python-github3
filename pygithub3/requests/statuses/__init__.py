from pygithub3.requests.base import Request, ValidationError
from pygithub3.resources.statuses import Status

class List(Request):
    uri = 'repos/{user}/{repo}/statuses/{ref}'
    resource = Status

class Create(Request):
    uri = 'repos/{user}/{repo}/statuses/{ref}'
    resource = Status
    body_schema = {
        'schema': ('state', 'target_url', 'description'),
        'required': ('state',)
    }

# vim: ai et sts=4 sw=4 ts=4
