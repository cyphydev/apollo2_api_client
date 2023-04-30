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

class IncasActor(object):
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
        'annotations': 'list[IncasAnnotation]',
        'extra_attributes': 'list[IncasExtraAttribute]',
        'media_resources': 'list[IncasMediaResource]',
        'segments': 'list[IncasSegment]',
        'actor_name': 'str',
        'description': 'str',
        'entity_type': 'EntityType',
        'expose_actor_info': 'bool',
        'id': 'str',
        'knowledge_base_url': 'str',
        'links': 'IncasLinks',
        'name': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'extra_attributes': 'extra_attributes',
        'media_resources': 'media_resources',
        'segments': 'segments',
        'actor_name': 'actor_name',
        'description': 'description',
        'entity_type': 'entity_type',
        'expose_actor_info': 'expose_actor_info',
        'id': 'id',
        'knowledge_base_url': 'knowledge_base_url',
        'links': 'links',
        'name': 'name'
    }

    def __init__(self, annotations=None, extra_attributes=None, media_resources=None, segments=None, actor_name=None, description=None, entity_type=None, expose_actor_info=None, id=None, knowledge_base_url=None, links=None, name=None):  # noqa: E501
        """IncasActor - a model defined in Swagger"""  # noqa: E501
        self._annotations = None
        self._extra_attributes = None
        self._media_resources = None
        self._segments = None
        self._actor_name = None
        self._description = None
        self._entity_type = None
        self._expose_actor_info = None
        self._id = None
        self._knowledge_base_url = None
        self._links = None
        self._name = None
        self.discriminator = None
        if annotations is not None:
            self.annotations = annotations
        if extra_attributes is not None:
            self.extra_attributes = extra_attributes
        if media_resources is not None:
            self.media_resources = media_resources
        if segments is not None:
            self.segments = segments
        if actor_name is not None:
            self.actor_name = actor_name
        if description is not None:
            self.description = description
        if entity_type is not None:
            self.entity_type = entity_type
        if expose_actor_info is not None:
            self.expose_actor_info = expose_actor_info
        if id is not None:
            self.id = id
        if knowledge_base_url is not None:
            self.knowledge_base_url = knowledge_base_url
        if links is not None:
            self.links = links
        if name is not None:
            self.name = name

    @property
    def annotations(self):
        """Gets the annotations of this IncasActor.  # noqa: E501


        :return: The annotations of this IncasActor.  # noqa: E501
        :rtype: list[IncasAnnotation]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this IncasActor.


        :param annotations: The annotations of this IncasActor.  # noqa: E501
        :type: list[IncasAnnotation]
        """

        self._annotations = annotations

    @property
    def extra_attributes(self):
        """Gets the extra_attributes of this IncasActor.  # noqa: E501


        :return: The extra_attributes of this IncasActor.  # noqa: E501
        :rtype: list[IncasExtraAttribute]
        """
        return self._extra_attributes

    @extra_attributes.setter
    def extra_attributes(self, extra_attributes):
        """Sets the extra_attributes of this IncasActor.


        :param extra_attributes: The extra_attributes of this IncasActor.  # noqa: E501
        :type: list[IncasExtraAttribute]
        """

        self._extra_attributes = extra_attributes

    @property
    def media_resources(self):
        """Gets the media_resources of this IncasActor.  # noqa: E501


        :return: The media_resources of this IncasActor.  # noqa: E501
        :rtype: list[IncasMediaResource]
        """
        return self._media_resources

    @media_resources.setter
    def media_resources(self, media_resources):
        """Sets the media_resources of this IncasActor.


        :param media_resources: The media_resources of this IncasActor.  # noqa: E501
        :type: list[IncasMediaResource]
        """

        self._media_resources = media_resources

    @property
    def segments(self):
        """Gets the segments of this IncasActor.  # noqa: E501


        :return: The segments of this IncasActor.  # noqa: E501
        :rtype: list[IncasSegment]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this IncasActor.


        :param segments: The segments of this IncasActor.  # noqa: E501
        :type: list[IncasSegment]
        """

        self._segments = segments

    @property
    def actor_name(self):
        """Gets the actor_name of this IncasActor.  # noqa: E501


        :return: The actor_name of this IncasActor.  # noqa: E501
        :rtype: str
        """
        return self._actor_name

    @actor_name.setter
    def actor_name(self, actor_name):
        """Sets the actor_name of this IncasActor.


        :param actor_name: The actor_name of this IncasActor.  # noqa: E501
        :type: str
        """

        self._actor_name = actor_name

    @property
    def description(self):
        """Gets the description of this IncasActor.  # noqa: E501


        :return: The description of this IncasActor.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IncasActor.


        :param description: The description of this IncasActor.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def entity_type(self):
        """Gets the entity_type of this IncasActor.  # noqa: E501


        :return: The entity_type of this IncasActor.  # noqa: E501
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this IncasActor.


        :param entity_type: The entity_type of this IncasActor.  # noqa: E501
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def expose_actor_info(self):
        """Gets the expose_actor_info of this IncasActor.  # noqa: E501


        :return: The expose_actor_info of this IncasActor.  # noqa: E501
        :rtype: bool
        """
        return self._expose_actor_info

    @expose_actor_info.setter
    def expose_actor_info(self, expose_actor_info):
        """Sets the expose_actor_info of this IncasActor.


        :param expose_actor_info: The expose_actor_info of this IncasActor.  # noqa: E501
        :type: bool
        """

        self._expose_actor_info = expose_actor_info

    @property
    def id(self):
        """Gets the id of this IncasActor.  # noqa: E501


        :return: The id of this IncasActor.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IncasActor.


        :param id: The id of this IncasActor.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def knowledge_base_url(self):
        """Gets the knowledge_base_url of this IncasActor.  # noqa: E501


        :return: The knowledge_base_url of this IncasActor.  # noqa: E501
        :rtype: str
        """
        return self._knowledge_base_url

    @knowledge_base_url.setter
    def knowledge_base_url(self, knowledge_base_url):
        """Sets the knowledge_base_url of this IncasActor.


        :param knowledge_base_url: The knowledge_base_url of this IncasActor.  # noqa: E501
        :type: str
        """

        self._knowledge_base_url = knowledge_base_url

    @property
    def links(self):
        """Gets the links of this IncasActor.  # noqa: E501


        :return: The links of this IncasActor.  # noqa: E501
        :rtype: IncasLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IncasActor.


        :param links: The links of this IncasActor.  # noqa: E501
        :type: IncasLinks
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this IncasActor.  # noqa: E501


        :return: The name of this IncasActor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IncasActor.


        :param name: The name of this IncasActor.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(IncasActor, dict):
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
        if not isinstance(other, IncasActor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other