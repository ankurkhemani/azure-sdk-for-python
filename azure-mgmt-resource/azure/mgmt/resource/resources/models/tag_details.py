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


class TagDetails(Model):
    """
    Tag details.

    :param id: Gets or sets the tag ID.
    :type id: str
    :param tag_name: Gets or sets the tag name.
    :type tag_name: str
    :param count: Gets or sets the tag count.
    :type count: :class:`TagCount
     <azure.mgmt.resource.resources.models.TagCount>`
    :param values: Gets or sets the list of tag values.
    :type values: list of :class:`TagValue
     <azure.mgmt.resource.resources.models.TagValue>`
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'tag_name': {'key': 'tagName', 'type': 'str'},
        'count': {'key': 'count', 'type': 'TagCount'},
        'values': {'key': 'values', 'type': '[TagValue]'},
    }

    def __init__(self, id=None, tag_name=None, count=None, values=None, **kwargs):
        self.id = id
        self.tag_name = tag_name
        self.count = count
        self.values = values
