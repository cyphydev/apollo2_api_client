# coding: utf-8

"""
    Mips UIUC Datatypes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class IncasExtraAttribute(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'provider_name': 'str',
        'attribute_key': 'str',
        'attribute_value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'provider_name': 'provider_name',
        'attribute_key': 'attribute_key',
        'attribute_value': 'attribute_value'
    }

    def __init__(self, name=None, id=None, provider_name=None, attribute_key=None, attribute_value=None):  # noqa: E501
        """IncasExtraAttribute - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._id = None
        self._provider_name = None
        self._attribute_key = None
        self._attribute_value = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if provider_name is not None:
            self.provider_name = provider_name
        if attribute_key is not None:
            self.attribute_key = attribute_key
        if attribute_value is not None:
            self.attribute_value = attribute_value

    @property
    def name(self):
        """Gets the name of this IncasExtraAttribute.  # noqa: E501


        :return: The name of this IncasExtraAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IncasExtraAttribute.


        :param name: The name of this IncasExtraAttribute.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this IncasExtraAttribute.  # noqa: E501


        :return: The id of this IncasExtraAttribute.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IncasExtraAttribute.


        :param id: The id of this IncasExtraAttribute.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def provider_name(self):
        """Gets the provider_name of this IncasExtraAttribute.  # noqa: E501


        :return: The provider_name of this IncasExtraAttribute.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this IncasExtraAttribute.


        :param provider_name: The provider_name of this IncasExtraAttribute.  # noqa: E501
        :type: str
        """

        self._provider_name = provider_name

    @property
    def attribute_key(self):
        """Gets the attribute_key of this IncasExtraAttribute.  # noqa: E501


        :return: The attribute_key of this IncasExtraAttribute.  # noqa: E501
        :rtype: str
        """
        return self._attribute_key

    @attribute_key.setter
    def attribute_key(self, attribute_key):
        """Sets the attribute_key of this IncasExtraAttribute.


        :param attribute_key: The attribute_key of this IncasExtraAttribute.  # noqa: E501
        :type: str
        """

        self._attribute_key = attribute_key

    @property
    def attribute_value(self):
        """Gets the attribute_value of this IncasExtraAttribute.  # noqa: E501


        :return: The attribute_value of this IncasExtraAttribute.  # noqa: E501
        :rtype: str
        """
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, attribute_value):
        """Sets the attribute_value of this IncasExtraAttribute.


        :param attribute_value: The attribute_value of this IncasExtraAttribute.  # noqa: E501
        :type: str
        """

        self._attribute_value = attribute_value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IncasExtraAttribute, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IncasExtraAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
