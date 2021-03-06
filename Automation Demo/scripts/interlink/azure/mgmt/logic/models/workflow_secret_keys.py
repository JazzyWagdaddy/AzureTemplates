# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WorkflowSecretKeys(Model):
    """WorkflowSecretKeys.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar primary_secret_key: Gets the primary secret key.
    :vartype primary_secret_key: str
    :ivar secondary_secret_key: Gets the secondary secret key.
    :vartype secondary_secret_key: str
    """ 

    _validation = {
        'primary_secret_key': {'readonly': True},
        'secondary_secret_key': {'readonly': True},
    }

    _attribute_map = {
        'primary_secret_key': {'key': 'primarySecretKey', 'type': 'str'},
        'secondary_secret_key': {'key': 'secondarySecretKey', 'type': 'str'},
    }

    def __init__(self):
        self.primary_secret_key = None
        self.secondary_secret_key = None
