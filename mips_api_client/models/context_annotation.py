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

class ContextAnnotation(object):
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
        'domain': 'Domain',
        'entity': 'Entity'
    }

    attribute_map = {
        'domain': 'domain',
        'entity': 'entity'
    }

    def __init__(self, domain=None, entity=None):  # noqa: E501
        """ContextAnnotation - a model defined in Swagger"""  # noqa: E501
        self._domain = None
        self._entity = None
        self.discriminator = None
        if domain is not None:
            self.domain = domain
        if entity is not None:
            self.entity = entity

    @property
    def domain(self):
        """Gets the domain of this ContextAnnotation.  # noqa: E501


        :return: The domain of this ContextAnnotation.  # noqa: E501
        :rtype: Domain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ContextAnnotation.


        :param domain: The domain of this ContextAnnotation.  # noqa: E501
        :type: Domain
        """

        self._domain = domain

    @property
    def entity(self):
        """Gets the entity of this ContextAnnotation.  # noqa: E501


        :return: The entity of this ContextAnnotation.  # noqa: E501
        :rtype: Entity
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this ContextAnnotation.


        :param entity: The entity of this ContextAnnotation.  # noqa: E501
        :type: Entity
        """

        self._entity = entity

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
        if issubclass(ContextAnnotation, dict):
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
        if not isinstance(other, ContextAnnotation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
