#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pygithub3.services.base import Service, MimeTypeMixin

class Status(Service):
    """ 
    Consume `Statuses API <http://developer.github.com/v3/repos/statuses>`
    """

    def __init__(self, **config):
        super(Status, self).__init__(**config)

    def list(self, repo, ref, user=None):
        """ List the statuses for a specific ref

        :param str repo: The repository of the ref
        :param str ref: The ref to get the statuses of
        :param str user: Username

        If you call it without user and you are authenticated, get the
        status of the ref in the repository owned by the authenticated
        user.

        .. warning::
            If you aren't authenticated and call without user, it returns 403
        ::
        """
        return self._get(
            self.make_request('statuses.list', user=user, repo=repo, ref=ref))

    def create(self, repo, ref, state, user=None, target_url=None, description=None):
        """ Creat a status for the specified ref

        :param str repo: The repository of the ref
        :param str ref: The ref to create a status for
        :param str state: The state of the status (can be pending, success,
            error, or failure)
        :param str user: Username
        :param str target_url: The target URL to associate with the status
        :param str description: A short description of the status

        If you call it without user and you are authenticated, the status will
        be created for the ref in the repository owned by the authenticated user.

        .. warning::
            If you aren't authenticated and call without user, it returns 403
        ::
        """
        request = self.make_request('statuses.create', repo=repo,
                                    ref=ref, user=user, state=state,
                                    description=description,
                                    target_url=target_url)

        return self._post(request, state=state, target_url=target_url,
                          description=description)

# vim: ai et sts=4 sw=4 ts=4
