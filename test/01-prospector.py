#
# Copyright 2026-2026 Ghent University
#
# This file is part of vsc-base,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://www.vscentrum.be),
# the Flemish Research Foundation (FWO) (http://www.fwo.be/en)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# https://github.com/hpcugent/vsc-base
#
# vsc-base is free software: you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as
# published by the Free Software Foundation, either version 2 of
# the License, or (at your option) any later version.
#
# vsc-base is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with vsc-base. If not, see <http://www.gnu.org/licenses/>.
#
"""
Prospector code-quality test, split out from the common import checks
so it can be run/skipped independently.
"""
import pprint
from pathlib import Path
import pytest

from vsc.install.shared_setup import vsc_setup
from vsc.install.commontest import run_prospector, prospector_ignore_paths_add


prospector_ignore_paths_add(".venv")
prospector_ignore_paths_add(".git")


@pytest.fixture(scope="module")
def repo_base_dir():
    # test/01-prospector.py -> repo root is one level up
    return str(Path(__file__).resolve().parent.parent / "src")

def test_prospector(repo_base_dir):
    failures = run_prospector(repo_base_dir)
    assert not failures, f"prospector failures:\n{pprint.pformat(failures)}"
