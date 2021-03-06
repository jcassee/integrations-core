# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from .dep import dep
from .manifest import manifest
from .metadata import metadata
from .service_checks import service_checks
from .agent_reqs import agent_reqs

ALL_COMMANDS = (
    dep,
    manifest,
    metadata,
    service_checks,
    agent_reqs,
)
