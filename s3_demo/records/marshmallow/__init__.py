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
from .json import MetadataSchemaV1, RecordSchemaV1

"""Schemas for marshmallow."""


__all__ = ('MetadataSchemaV1', 'RecordSchemaV1',)
