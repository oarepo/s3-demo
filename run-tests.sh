#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# S3 Repository Demo is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.


pydocstyle s3_demo tests && \
isort --check-only --diff && \
check-manifest --ignore ".travis-*" && \
pytest
