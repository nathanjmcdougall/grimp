from __future__ import annotations

from typing import TYPE_CHECKING

from grimp.application.ports.packagefinder import AbstractPackageFinder

if TYPE_CHECKING:
    from collections.abc import Mapping

    from grimp.application.ports.filesystem import AbstractFileSystem


class BaseFakePackageFinder(AbstractPackageFinder):
    directory_map: Mapping[str, set[str]] = {}

    def determine_package_directories(
        self, package_name: str, file_system: AbstractFileSystem
    ) -> set[str]:
        return self.directory_map[package_name]
