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

class TwitterData(object):
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
        'attachments': 'TwitterAttachment',
        'context_annotations': 'list[TwitterContextAnnotation]',
        'author_id': 'str',
        'conversation_id': 'str',
        'created_at': 'str',
        'edit_controls': 'TwitterEditControls',
        'edit_history_tweet_ids': 'list[str]',
        'entities': 'TwitterEntities',
        'id': 'str',
        'lang': 'str',
        'possibly_sensitive': 'bool',
        'public_metrics': 'TwitterPublicMetrics',
        'reference_tweets': 'list[TwitterReferencedTweet]',
        'reply_settings': 'str',
        'tweet_id': 'str',
        'twitter_author_screenname': 'str',
        'twitter_user_id': 'str'
    }

    attribute_map = {
        'attachments': 'attachments',
        'context_annotations': 'context_annotations',
        'author_id': 'author_id',
        'conversation_id': 'conversation_id',
        'created_at': 'created_at',
        'edit_controls': 'edit_controls',
        'edit_history_tweet_ids': 'edit_history_tweet_ids',
        'entities': 'entities',
        'id': 'id',
        'lang': 'lang',
        'possibly_sensitive': 'possibly_sensitive',
        'public_metrics': 'public_metrics',
        'reference_tweets': 'reference_tweets',
        'reply_settings': 'reply_settings',
        'tweet_id': 'tweet_id',
        'twitter_author_screenname': 'twitter_author_screenname',
        'twitter_user_id': 'twitter_user_id'
    }

    def __init__(self, attachments=None, context_annotations=None, author_id=None, conversation_id=None, created_at=None, edit_controls=None, edit_history_tweet_ids=None, entities=None, id=None, lang=None, possibly_sensitive=None, public_metrics=None, reference_tweets=None, reply_settings=None, tweet_id=None, twitter_author_screenname=None, twitter_user_id=None):  # noqa: E501
        """TwitterData - a model defined in Swagger"""  # noqa: E501
        self._attachments = None
        self._context_annotations = None
        self._author_id = None
        self._conversation_id = None
        self._created_at = None
        self._edit_controls = None
        self._edit_history_tweet_ids = None
        self._entities = None
        self._id = None
        self._lang = None
        self._possibly_sensitive = None
        self._public_metrics = None
        self._reference_tweets = None
        self._reply_settings = None
        self._tweet_id = None
        self._twitter_author_screenname = None
        self._twitter_user_id = None
        self.discriminator = None
        if attachments is not None:
            self.attachments = attachments
        if context_annotations is not None:
            self.context_annotations = context_annotations
        if author_id is not None:
            self.author_id = author_id
        if conversation_id is not None:
            self.conversation_id = conversation_id
        if created_at is not None:
            self.created_at = created_at
        if edit_controls is not None:
            self.edit_controls = edit_controls
        if edit_history_tweet_ids is not None:
            self.edit_history_tweet_ids = edit_history_tweet_ids
        if entities is not None:
            self.entities = entities
        if id is not None:
            self.id = id
        if lang is not None:
            self.lang = lang
        if possibly_sensitive is not None:
            self.possibly_sensitive = possibly_sensitive
        if public_metrics is not None:
            self.public_metrics = public_metrics
        if reference_tweets is not None:
            self.reference_tweets = reference_tweets
        if reply_settings is not None:
            self.reply_settings = reply_settings
        if tweet_id is not None:
            self.tweet_id = tweet_id
        if twitter_author_screenname is not None:
            self.twitter_author_screenname = twitter_author_screenname
        if twitter_user_id is not None:
            self.twitter_user_id = twitter_user_id

    @property
    def attachments(self):
        """Gets the attachments of this TwitterData.  # noqa: E501


        :return: The attachments of this TwitterData.  # noqa: E501
        :rtype: TwitterAttachment
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this TwitterData.


        :param attachments: The attachments of this TwitterData.  # noqa: E501
        :type: TwitterAttachment
        """

        self._attachments = attachments

    @property
    def context_annotations(self):
        """Gets the context_annotations of this TwitterData.  # noqa: E501


        :return: The context_annotations of this TwitterData.  # noqa: E501
        :rtype: list[TwitterContextAnnotation]
        """
        return self._context_annotations

    @context_annotations.setter
    def context_annotations(self, context_annotations):
        """Sets the context_annotations of this TwitterData.


        :param context_annotations: The context_annotations of this TwitterData.  # noqa: E501
        :type: list[TwitterContextAnnotation]
        """

        self._context_annotations = context_annotations

    @property
    def author_id(self):
        """Gets the author_id of this TwitterData.  # noqa: E501


        :return: The author_id of this TwitterData.  # noqa: E501
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this TwitterData.


        :param author_id: The author_id of this TwitterData.  # noqa: E501
        :type: str
        """

        self._author_id = author_id

    @property
    def conversation_id(self):
        """Gets the conversation_id of this TwitterData.  # noqa: E501


        :return: The conversation_id of this TwitterData.  # noqa: E501
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """Sets the conversation_id of this TwitterData.


        :param conversation_id: The conversation_id of this TwitterData.  # noqa: E501
        :type: str
        """

        self._conversation_id = conversation_id

    @property
    def created_at(self):
        """Gets the created_at of this TwitterData.  # noqa: E501


        :return: The created_at of this TwitterData.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TwitterData.


        :param created_at: The created_at of this TwitterData.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def edit_controls(self):
        """Gets the edit_controls of this TwitterData.  # noqa: E501


        :return: The edit_controls of this TwitterData.  # noqa: E501
        :rtype: TwitterEditControls
        """
        return self._edit_controls

    @edit_controls.setter
    def edit_controls(self, edit_controls):
        """Sets the edit_controls of this TwitterData.


        :param edit_controls: The edit_controls of this TwitterData.  # noqa: E501
        :type: TwitterEditControls
        """

        self._edit_controls = edit_controls

    @property
    def edit_history_tweet_ids(self):
        """Gets the edit_history_tweet_ids of this TwitterData.  # noqa: E501


        :return: The edit_history_tweet_ids of this TwitterData.  # noqa: E501
        :rtype: list[str]
        """
        return self._edit_history_tweet_ids

    @edit_history_tweet_ids.setter
    def edit_history_tweet_ids(self, edit_history_tweet_ids):
        """Sets the edit_history_tweet_ids of this TwitterData.


        :param edit_history_tweet_ids: The edit_history_tweet_ids of this TwitterData.  # noqa: E501
        :type: list[str]
        """

        self._edit_history_tweet_ids = edit_history_tweet_ids

    @property
    def entities(self):
        """Gets the entities of this TwitterData.  # noqa: E501


        :return: The entities of this TwitterData.  # noqa: E501
        :rtype: TwitterEntities
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this TwitterData.


        :param entities: The entities of this TwitterData.  # noqa: E501
        :type: TwitterEntities
        """

        self._entities = entities

    @property
    def id(self):
        """Gets the id of this TwitterData.  # noqa: E501


        :return: The id of this TwitterData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TwitterData.


        :param id: The id of this TwitterData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def lang(self):
        """Gets the lang of this TwitterData.  # noqa: E501


        :return: The lang of this TwitterData.  # noqa: E501
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this TwitterData.


        :param lang: The lang of this TwitterData.  # noqa: E501
        :type: str
        """

        self._lang = lang

    @property
    def possibly_sensitive(self):
        """Gets the possibly_sensitive of this TwitterData.  # noqa: E501


        :return: The possibly_sensitive of this TwitterData.  # noqa: E501
        :rtype: bool
        """
        return self._possibly_sensitive

    @possibly_sensitive.setter
    def possibly_sensitive(self, possibly_sensitive):
        """Sets the possibly_sensitive of this TwitterData.


        :param possibly_sensitive: The possibly_sensitive of this TwitterData.  # noqa: E501
        :type: bool
        """

        self._possibly_sensitive = possibly_sensitive

    @property
    def public_metrics(self):
        """Gets the public_metrics of this TwitterData.  # noqa: E501


        :return: The public_metrics of this TwitterData.  # noqa: E501
        :rtype: TwitterPublicMetrics
        """
        return self._public_metrics

    @public_metrics.setter
    def public_metrics(self, public_metrics):
        """Sets the public_metrics of this TwitterData.


        :param public_metrics: The public_metrics of this TwitterData.  # noqa: E501
        :type: TwitterPublicMetrics
        """

        self._public_metrics = public_metrics

    @property
    def reference_tweets(self):
        """Gets the reference_tweets of this TwitterData.  # noqa: E501


        :return: The reference_tweets of this TwitterData.  # noqa: E501
        :rtype: list[TwitterReferencedTweet]
        """
        return self._reference_tweets

    @reference_tweets.setter
    def reference_tweets(self, reference_tweets):
        """Sets the reference_tweets of this TwitterData.


        :param reference_tweets: The reference_tweets of this TwitterData.  # noqa: E501
        :type: list[TwitterReferencedTweet]
        """

        self._reference_tweets = reference_tweets

    @property
    def reply_settings(self):
        """Gets the reply_settings of this TwitterData.  # noqa: E501


        :return: The reply_settings of this TwitterData.  # noqa: E501
        :rtype: str
        """
        return self._reply_settings

    @reply_settings.setter
    def reply_settings(self, reply_settings):
        """Sets the reply_settings of this TwitterData.


        :param reply_settings: The reply_settings of this TwitterData.  # noqa: E501
        :type: str
        """

        self._reply_settings = reply_settings

    @property
    def tweet_id(self):
        """Gets the tweet_id of this TwitterData.  # noqa: E501


        :return: The tweet_id of this TwitterData.  # noqa: E501
        :rtype: str
        """
        return self._tweet_id

    @tweet_id.setter
    def tweet_id(self, tweet_id):
        """Sets the tweet_id of this TwitterData.


        :param tweet_id: The tweet_id of this TwitterData.  # noqa: E501
        :type: str
        """

        self._tweet_id = tweet_id

    @property
    def twitter_author_screenname(self):
        """Gets the twitter_author_screenname of this TwitterData.  # noqa: E501


        :return: The twitter_author_screenname of this TwitterData.  # noqa: E501
        :rtype: str
        """
        return self._twitter_author_screenname

    @twitter_author_screenname.setter
    def twitter_author_screenname(self, twitter_author_screenname):
        """Sets the twitter_author_screenname of this TwitterData.


        :param twitter_author_screenname: The twitter_author_screenname of this TwitterData.  # noqa: E501
        :type: str
        """

        self._twitter_author_screenname = twitter_author_screenname

    @property
    def twitter_user_id(self):
        """Gets the twitter_user_id of this TwitterData.  # noqa: E501


        :return: The twitter_user_id of this TwitterData.  # noqa: E501
        :rtype: str
        """
        return self._twitter_user_id

    @twitter_user_id.setter
    def twitter_user_id(self, twitter_user_id):
        """Sets the twitter_user_id of this TwitterData.


        :param twitter_user_id: The twitter_user_id of this TwitterData.  # noqa: E501
        :type: str
        """

        self._twitter_user_id = twitter_user_id

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
        if issubclass(TwitterData, dict):
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
        if not isinstance(other, TwitterData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
