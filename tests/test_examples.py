import os
from pathlib import Path

import pytest
from beet import ProjectCache, run_beet
from lectern import Document
from pytest_insta import SnapshotFixture

EXAMPLES = [
    f
    for f in os.listdir("examples")
    if not (f.endswith("_nosnap") or f.startswith("."))
]


@pytest.mark.parametrize("directory", EXAMPLES)
def test_build(snapshot: SnapshotFixture, directory: str, tmp_path: Path):
    with run_beet(
        directory=f"examples/{directory}",
        cache=ProjectCache(tmp_path / ".beet_cache", tmp_path / "generated"),
    ) as ctx:
        expected: Document = snapshot("pack.md")
        actual = ctx.inject(Document)
        for o in actual.data.overlays:
            if actual.data.overlays[o].mcmeta:
                del actual.data.overlays[o].mcmeta
        for o in actual.assets.overlays:
            if actual.assets.overlays[o].mcmeta:
                del actual.assets.overlays[o].mcmeta
        assert actual == expected
