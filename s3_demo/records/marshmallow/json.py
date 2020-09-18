# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# CESNET OA Repository Demo is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Loaders.
This file contains sample loaders that can be used to deserialize input data in
an application level data structure. The marshmallow_loader() method can be
parameterized with different schemas for the record metadata. In the provided
json_v1 instance, it uses the MetadataSchemaV1, defining the
PersistentIdentifier field.
"""

from __future__ import absolute_import, print_function

from oarepo_dc.marshmallow import DCObjectSchemaV2Mixin
from oarepo_invenio_model.marshmallow import InvenioRecordMetadataSchemaV1Mixin
from invenio_records_rest.schemas import StrictKeysMixin
from invenio_records_rest.schemas.fields import GenFunction, \
    PersistentIdentifier, SanitizedUnicode
from marshmallow import fields, missing


def files_from_context(_, context):
    """Get the record's files from context."""
    record = (context or {}).get('record', {})
    return record.get('_files', missing)


class MetadataSchemaV1(InvenioRecordMetadataSchemaV1Mixin,
                       DCObjectSchemaV2Mixin,
                       StrictKeysMixin):
    """Schema for the record metadata."""


class RecordSchemaV1(StrictKeysMixin):
    """Record schema."""

    metadata = fields.Nested(MetadataSchemaV1)
    created = fields.Str(dump_only=True)
    revision = fields.Integer(dump_only=True)
    updated = fields.Str(dump_only=True)
    links = fields.Dict(dump_only=True)
    id = PersistentIdentifier()
    files = GenFunction(
        serialize=files_from_context, deserialize=files_from_context)
