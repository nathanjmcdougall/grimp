import pytest  # type: ignore

from grimp.application.graph import ImportGraph
from grimp.adaptors.modulefinder import ModuleFinder
from tests.config import override_settings


@pytest.fixture(scope="module", autouse=True)
def configure_unit_tests():
    with override_settings(
        IMPORT_GRAPH_CLASS=ImportGraph,
        MODULE_FINDER=ModuleFinder(),
        FILE_SYSTEM=None,
    ):
        yield
