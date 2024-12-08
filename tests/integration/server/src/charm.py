#!/usr/bin/env python3
# Copyright 2024 Canonical
# See LICENSE file for licensing details.

"""Charm the application."""

import logging

import ops
from charms.filesystem_client.v0.interfaces import FsProvides, NfsInfo

_logger = logging.getLogger(__name__)


class StorageServerCharm(ops.CharmBase):
    def __init__(self, framework: ops.Framework):
        super().__init__(framework)
        self._fs_share = FsProvides(self, "fs-share", "server-peers")
        framework.observe(self.on.start, self._on_start)

    def _on_start(self, event: ops.StartEvent):
        """Handle start event."""
        self._fs_share.set_fs_info(NfsInfo("192.168.1.254", 65535, "/srv"))
        self.unit.status = ops.ActiveStatus()


if __name__ == "__main__":  # pragma: nocover
    ops.main(StorageServerCharm)  # type: ignore
