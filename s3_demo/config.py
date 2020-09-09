# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# S3 Repository Demo is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Version information for S3 Repository Demo.

This file is imported by ``s3_demo.__init__``,
and parsed by ``setup.py``.
"""
import os

from invenio_records_rest.utils import allow_all
from invenio_indexer.api import RecordIndexer

from invenio_search import RecordsSearch


RECORDS_REST_ENDPOINTS = {
    'recid': dict(
        pid_type='recid',
        pid_minter='recid',
        pid_fetcher='recid',
        default_endpoint_prefix=True,
        search_class=RecordsSearch,
        indexer_class=RecordIndexer,
        search_index='records',
        search_type=None,
        record_serializers={
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_response'),
        },
        search_serializers={
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_search'),
        },
        list_route='/records/',
        item_route='/records/<pid(recid,'
                   'record_class="cesnet_demo.records.api.Record")'
                   ':pid_value>',
        default_media_type='application/json',
        max_result_window=10000,
        error_handlers=dict(),
        create_permission_factory_imp=allow_all,
        read_permission_factory_imp=allow_all,
        update_permission_factory_imp=allow_all,
        delete_permission_factory_imp=allow_all,
        list_permission_factory_imp=allow_all,
        # TODO: uncomment after upgrade to newer invenio-records-files
        # links_factory_imp='invenio_records_files.'
        #                   'links:default_record_files_links_factory',
    ),
}
"""REST API for s3-demo."""

ES_USER = os.getenv('OAREPO_ES_USER', None)
ES_PASSWORD = os.getenv('OAREPO_ES_PASSWORD', None)
ES_PARAMS = {}

if ES_USER and ES_PASSWORD:
    ES_PARAMS = dict(http_auth=(ES_USER, ES_PASSWORD))

SEARCH_ELASTIC_HOSTS = [dict(host=h, **ES_PARAMS) for h in
                        os.getenv('OAREPO_SEARCH_ELASTIC_HOSTS', 'localhost').split(',')]

APP_ALLOWED_HOSTS = [h for h in os.getenv('OAREPO_APP_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')]
