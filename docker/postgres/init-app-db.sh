#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# S3 Repository Demo is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE ROLE s3-demo WITH LOGIN PASSWORD 's3-demo';
    ALTER ROLE s3-demo CREATEDB;
    \du;
EOSQL
