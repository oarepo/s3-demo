# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# S3 Repository Demo is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""API for S3 Repository Demo.

This file is imported by ``s3_demo.__init__``,
and parsed by ``setup.py``.
"""
from invenio_records_files.api import Record as FilesRecord


class Record(FilesRecord):
    """Custom record."""
    _schema = "records/record-v1.0.0.json"
