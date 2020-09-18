# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# S3 Repository Demo is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Extension for S3 Repository Demo.

This file is imported by ``s3_demo.__init__``,
and parsed by ``setup.py``.
"""
from invenio_files_rest.signals import file_deleted, file_uploaded
from invenio_indexer.signals import before_record_index

from . import config


class OARepoS3Demo(object):
    """CESNET OA Repository S3 Demo extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions['s3-demo'] = self

    def init_config(self, app):
        """Initialize configuration.
        Override configuration variables with the values in this package.
        """
        with_endpoints = app.config.get(
            'S3_DEMO_ENDPOINTS_ENABLED', True)
        for k in dir(config):
            if k.startswith('OAREPO_DEMO_'):
                app.config.setdefault(k, getattr(config, k))
            elif k == 'SEARCH_UI_JSTEMPLATE_RESULTS':
                app.config['SEARCH_UI_JSTEMPLATE_RESULTS'] = getattr(
                    config, k)
            elif k == 'PIDSTORE_RECID_FIELD':
                app.config['PIDSTORE_RECID_FIELD'] = getattr(config, k)
            elif k == 'FILES_REST_PERMISSION_FACTORY':
                app.config['FILES_REST_PERMISSION_FACTORY'] =\
                        getattr(config, k)
            else:
                for n in ['RECORDS_REST_ENDPOINTS', 'RECORDS_UI_ENDPOINTS',
                          'RECORDS_REST_FACETS', 'RECORDS_REST_SORT_OPTIONS',
                          'RECORDS_REST_DEFAULT_SORT',
                          'RECORDS_FILES_REST_ENDPOINTS']:
                    if k == n and with_endpoints:
                        app.config.setdefault(n, {})
                        app.config[n].update(getattr(config, k))
