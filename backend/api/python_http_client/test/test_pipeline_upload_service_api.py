# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Kubeflow Pipelines API

    This file contains REST API specification for Kubeflow Pipelines. The file is autogenerated from the swagger definition.

    Contact: kubeflow-pipelines@google.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kfp_server_api
from kfp_server_api.api.pipeline_upload_service_api import PipelineUploadServiceApi  # noqa: E501
from kfp_server_api.rest import ApiException


class TestPipelineUploadServiceApi(unittest.TestCase):
    """PipelineUploadServiceApi unit test stubs"""

    def setUp(self):
        self.api = kfp_server_api.api.pipeline_upload_service_api.PipelineUploadServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_upload_pipeline(self):
        """Test case for upload_pipeline

        """
        pass

    def test_upload_pipeline_version(self):
        """Test case for upload_pipeline_version

        """
        pass


if __name__ == '__main__':
    unittest.main()
