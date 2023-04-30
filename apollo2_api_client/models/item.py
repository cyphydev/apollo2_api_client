# coding: utf-8

"""
    Apollo2 API Server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Item(object):
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
        'id': 'str',
        'author': 'str',
        'platform': 'MediaType',
        'time_published': 'int',
        'sid': 'int',
        'source_id': 'int',
        'enrichments': 'list[Enrichment]',
        'clusters': 'list[ClusterMember]',
        'media_items': 'list[MediaItem]',
        'text': 'str',
        'data': 'AnyOfItemData'
    }

    attribute_map = {
        'id': 'id',
        'author': 'author',
        'platform': 'platform',
        'time_published': 'time_published',
        'sid': 'sid',
        'source_id': 'source_id',
        'enrichments': 'enrichments',
        'clusters': 'clusters',
        'media_items': 'media_items',
        'text': 'text',
        'data': 'data'
    }

    def __init__(self, id=None, author=None, platform=None, time_published=None, sid=None, source_id=None, enrichments=None, clusters=None, media_items=None, text=None, data=None):  # noqa: E501
        """Item - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._author = None
        self._platform = None
        self._time_published = None
        self._sid = None
        self._source_id = None
        self._enrichments = None
        self._clusters = None
        self._media_items = None
        self._text = None
        self._data = None
        self.discriminator = None
        self.id = id
        self.author = author
        self.platform = platform
        self.time_published = time_published
        if sid is not None:
            self.sid = sid
        if source_id is not None:
            self.source_id = source_id
        if enrichments is not None:
            self.enrichments = enrichments
        if clusters is not None:
            self.clusters = clusters
        if media_items is not None:
            self.media_items = media_items
        if text is not None:
            self.text = text
        self.data = data

    @property
    def id(self):
        """Gets the id of this Item.  # noqa: E501


        :return: The id of this Item.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Item.


        :param id: The id of this Item.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def author(self):
        """Gets the author of this Item.  # noqa: E501


        :return: The author of this Item.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Item.


        :param author: The author of this Item.  # noqa: E501
        :type: str
        """
        if author is None:
            raise ValueError("Invalid value for `author`, must not be `None`")  # noqa: E501

        self._author = author

    @property
    def platform(self):
        """Gets the platform of this Item.  # noqa: E501


        :return: The platform of this Item.  # noqa: E501
        :rtype: MediaType
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this Item.


        :param platform: The platform of this Item.  # noqa: E501
        :type: MediaType
        """
        if platform is None:
            raise ValueError("Invalid value for `platform`, must not be `None`")  # noqa: E501

        self._platform = platform

    @property
    def time_published(self):
        """Gets the time_published of this Item.  # noqa: E501


        :return: The time_published of this Item.  # noqa: E501
        :rtype: int
        """
        return self._time_published

    @time_published.setter
    def time_published(self, time_published):
        """Sets the time_published of this Item.


        :param time_published: The time_published of this Item.  # noqa: E501
        :type: int
        """
        if time_published is None:
            raise ValueError("Invalid value for `time_published`, must not be `None`")  # noqa: E501

        self._time_published = time_published

    @property
    def sid(self):
        """Gets the sid of this Item.  # noqa: E501


        :return: The sid of this Item.  # noqa: E501
        :rtype: int
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this Item.


        :param sid: The sid of this Item.  # noqa: E501
        :type: int
        """

        self._sid = sid

    @property
    def source_id(self):
        """Gets the source_id of this Item.  # noqa: E501


        :return: The source_id of this Item.  # noqa: E501
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this Item.


        :param source_id: The source_id of this Item.  # noqa: E501
        :type: int
        """

        self._source_id = source_id

    @property
    def enrichments(self):
        """Gets the enrichments of this Item.  # noqa: E501


        :return: The enrichments of this Item.  # noqa: E501
        :rtype: list[Enrichment]
        """
        return self._enrichments

    @enrichments.setter
    def enrichments(self, enrichments):
        """Sets the enrichments of this Item.


        :param enrichments: The enrichments of this Item.  # noqa: E501
        :type: list[Enrichment]
        """

        self._enrichments = enrichments

    @property
    def clusters(self):
        """Gets the clusters of this Item.  # noqa: E501


        :return: The clusters of this Item.  # noqa: E501
        :rtype: list[ClusterMember]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this Item.


        :param clusters: The clusters of this Item.  # noqa: E501
        :type: list[ClusterMember]
        """

        self._clusters = clusters

    @property
    def media_items(self):
        """Gets the media_items of this Item.  # noqa: E501


        :return: The media_items of this Item.  # noqa: E501
        :rtype: list[MediaItem]
        """
        return self._media_items

    @media_items.setter
    def media_items(self, media_items):
        """Sets the media_items of this Item.


        :param media_items: The media_items of this Item.  # noqa: E501
        :type: list[MediaItem]
        """

        self._media_items = media_items

    @property
    def text(self):
        """Gets the text of this Item.  # noqa: E501


        :return: The text of this Item.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Item.


        :param text: The text of this Item.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def data(self):
        """Gets the data of this Item.  # noqa: E501


        :return: The data of this Item.  # noqa: E501
        :rtype: AnyOfItemData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Item.


        :param data: The data of this Item.  # noqa: E501
        :type: AnyOfItemData
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if issubclass(Item, dict):
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
        if not isinstance(other, Item):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
