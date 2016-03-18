# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeleteOperationResult(Model):
    """
    The compute long running operation response.

    :param operation_id: Gets the operation identifier.
    :type operation_id: str
    :param status: Gets the operation status. Possible values include:
     'InProgress', 'Succeeded', 'Failed'
    :type status: str
    :param start_time: Gets the operation start time
    :type start_time: datetime
    :param end_time: Gets the operation end time
    :type end_time: datetime
    :param error: Gets or sets the operation error if any occurred
    :type error: :class:`ApiError <azure.mgmt.compute.models.ApiError>`
    """ 

    _validation = {
        'operation_id': {'required': True},
        'status': {'required': True},
        'start_time': {'required': True},
    }

    _attribute_map = {
        'operation_id': {'key': 'operationId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'OperationStatus'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'error': {'key': 'error', 'type': 'ApiError'},
    }

    def __init__(self, operation_id, status, start_time, end_time=None, error=None, **kwargs):
        self.operation_id = operation_id
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.error = error
