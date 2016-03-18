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

from .resource import Resource


class ExpressRouteCircuit(Resource):
    """
    ExpressRouteCircuit resource

    :param id: Resource Id
    :type id: str
    :param name: Resource name
    :type name: str
    :param type: Resource type
    :type type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :param sku: Gets or sets sku
    :type sku: :class:`ExpressRouteCircuitSku
     <azure.mgmt.network.models.ExpressRouteCircuitSku>`
    :param circuit_provisioning_state: Gets or sets CircuitProvisioningState
     state of the resource
    :type circuit_provisioning_state: str
    :param service_provider_provisioning_state: Gets or sets
     ServiceProviderProvisioningState state of the resource . Possible values
     include: 'NotProvisioned', 'Provisioning', 'Provisioned',
     'Deprovisioning'
    :type service_provider_provisioning_state: str
    :param authorizations: Gets or sets list of authorizations
    :type authorizations: list of :class:`ExpressRouteCircuitAuthorization
     <azure.mgmt.network.models.ExpressRouteCircuitAuthorization>`
    :param peerings: Gets or sets list of peerings
    :type peerings: list of :class:`ExpressRouteCircuitPeering
     <azure.mgmt.network.models.ExpressRouteCircuitPeering>`
    :param service_key: Gets or sets ServiceKey
    :type service_key: str
    :param service_provider_notes: Gets or sets ServiceProviderNotes
    :type service_provider_notes: str
    :param service_provider_properties: Gets or sets ServiceProviderProperties
    :type service_provider_properties:
     :class:`ExpressRouteCircuitServiceProviderProperties
     <azure.mgmt.network.models.ExpressRouteCircuitServiceProviderProperties>`
    :param provisioning_state: Gets or sets Provisioning state of the
     PublicIP resource Updating/Deleting/Failed
    :type provisioning_state: str
    :param etag: Gets a unique read-only string that changes whenever the
     resource is updated
    :type etag: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'ExpressRouteCircuitSku'},
        'circuit_provisioning_state': {'key': 'properties.circuitProvisioningState', 'type': 'str'},
        'service_provider_provisioning_state': {'key': 'properties.serviceProviderProvisioningState', 'type': 'ServiceProviderProvisioningState'},
        'authorizations': {'key': 'properties.authorizations', 'type': '[ExpressRouteCircuitAuthorization]'},
        'peerings': {'key': 'properties.peerings', 'type': '[ExpressRouteCircuitPeering]'},
        'service_key': {'key': 'properties.serviceKey', 'type': 'str'},
        'service_provider_notes': {'key': 'properties.serviceProviderNotes', 'type': 'str'},
        'service_provider_properties': {'key': 'properties.serviceProviderProperties', 'type': 'ExpressRouteCircuitServiceProviderProperties'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, name=None, type=None, location=None, tags=None, sku=None, circuit_provisioning_state=None, service_provider_provisioning_state=None, authorizations=None, peerings=None, service_key=None, service_provider_notes=None, service_provider_properties=None, provisioning_state=None, etag=None, **kwargs):
        super(ExpressRouteCircuit, self).__init__(id=id, name=name, type=type, location=location, tags=tags, **kwargs)
        self.sku = sku
        self.circuit_provisioning_state = circuit_provisioning_state
        self.service_provider_provisioning_state = service_provider_provisioning_state
        self.authorizations = authorizations
        self.peerings = peerings
        self.service_key = service_key
        self.service_provider_notes = service_provider_notes
        self.service_provider_properties = service_provider_properties
        self.provisioning_state = provisioning_state
        self.etag = etag
