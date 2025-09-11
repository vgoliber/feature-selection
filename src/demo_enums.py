# Copyright 2024 D-Wave
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import Enum


class SolverType(Enum):
    """Add a list of solver options here. If this demo only requires 1 solver,
    this functionality can be removed.
    """

    CQM = 0
    NL = 1

    @property
    def label(self):
        return {
            SolverType.CQM: "Quantum Hybrid (CQM)",
            SolverType.NL: "Quantum Hybrid (NL)",
        }[self]


### If any settings or variables are being used repeatedly, thoughout the code, create a new
### Enum for the setting here to avoid string comparisons or other fragile code practices.
