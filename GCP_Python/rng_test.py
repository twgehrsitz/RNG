# Copyright 2016 Google Inc. All rights reserved.
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
# ------------------------------------------------------------------------
# This code was modified by OUCS4263-SoftBearEngineering to display
# a random number to the page for practice and is in no way meant
# to serve as a distributable project.

import webtest
import rng


def test_get():
    app = webtest.TestApp(rng.app)
    response = app.get('/')
    assert response.status_int == 200
