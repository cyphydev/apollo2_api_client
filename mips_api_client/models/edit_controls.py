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

class EditControls(object):
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
        'editable_until': 'str',
        'edits_remaining': 'int',
        'is_edit_eligible': 'bool'
    }

    attribute_map = {
        'editable_until': 'editable_until',
        'edits_remaining': 'edits_remaining',
        'is_edit_eligible': 'is_edit_eligible'
    }

    def __init__(self, editable_until=None, edits_remaining=None, is_edit_eligible=None):  # noqa: E501
        """EditControls - a model defined in Swagger"""  # noqa: E501
        self._editable_until = None
        self._edits_remaining = None
        self._is_edit_eligible = None
        self.discriminator = None
        if editable_until is not None:
            self.editable_until = editable_until
        if edits_remaining is not None:
            self.edits_remaining = edits_remaining
        if is_edit_eligible is not None:
            self.is_edit_eligible = is_edit_eligible

    @property
    def editable_until(self):
        """Gets the editable_until of this EditControls.  # noqa: E501


        :return: The editable_until of this EditControls.  # noqa: E501
        :rtype: str
        """
        return self._editable_until

    @editable_until.setter
    def editable_until(self, editable_until):
        """Sets the editable_until of this EditControls.


        :param editable_until: The editable_until of this EditControls.  # noqa: E501
        :type: str
        """

        self._editable_until = editable_until

    @property
    def edits_remaining(self):
        """Gets the edits_remaining of this EditControls.  # noqa: E501


        :return: The edits_remaining of this EditControls.  # noqa: E501
        :rtype: int
        """
        return self._edits_remaining

    @edits_remaining.setter
    def edits_remaining(self, edits_remaining):
        """Sets the edits_remaining of this EditControls.


        :param edits_remaining: The edits_remaining of this EditControls.  # noqa: E501
        :type: int
        """

        self._edits_remaining = edits_remaining

    @property
    def is_edit_eligible(self):
        """Gets the is_edit_eligible of this EditControls.  # noqa: E501


        :return: The is_edit_eligible of this EditControls.  # noqa: E501
        :rtype: bool
        """
        return self._is_edit_eligible

    @is_edit_eligible.setter
    def is_edit_eligible(self, is_edit_eligible):
        """Sets the is_edit_eligible of this EditControls.


        :param is_edit_eligible: The is_edit_eligible of this EditControls.  # noqa: E501
        :type: bool
        """

        self._is_edit_eligible = is_edit_eligible

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
        if issubclass(EditControls, dict):
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
        if not isinstance(other, EditControls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
