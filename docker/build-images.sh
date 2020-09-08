#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# S3 Repository Demo is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

# Extract Pipfile.lock hash to use as the docker image tag
INVENIO_VERSION=${OAREPO_VERSION:-"3.2.1"}
ES_VERSION=${OAREPO_ES_VERSION:-"es7"}

# Build application image
docker build --build-arg DEPENDENCIES_VERSION="${INVENIO_VERSION}-${ES_VERSION}" . -t s3-demo
