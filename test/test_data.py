# coding: utf-8

"""
    Apollo2 API Server

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import apollo2_api_client
from apollo2_api_client.models.data import Data  # noqa: E501
from apollo2_api_client.rest import ApiException

class TestData(unittest.TestCase):
    """Data unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Data
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Data`
        """
        model = apollo2_api_client.models.data.Data()  # noqa: E501
        if include_optional :
            return Data(
                attachments = apollo2_api_client.models.twitter_attachment.TwitterAttachment(
                    media_keys = [
                        ''
                        ], ), 
                context_annotations = [
                    apollo2_api_client.models.twitter_context_annotation.TwitterContextAnnotation(
                        domain = apollo2_api_client.models.twitter_domain.TwitterDomain(
                            description = '', 
                            id = '', 
                            name = '', ), 
                        entity = apollo2_api_client.models.twitter_entity.TwitterEntity(
                            description = '', 
                            id = '', 
                            name = '', ), )
                    ], 
                author_id = '', 
                conversation_id = '', 
                created_at = '', 
                edit_controls = apollo2_api_client.models.twitter_edit_controls.TwitterEditControls(
                    editable_until = '', 
                    edits_remaining = 56, 
                    is_edit_eligible = True, ), 
                edit_history_tweet_ids = [
                    ''
                    ], 
                entities = apollo2_api_client.models.twitter_entities.TwitterEntities(
                    annotations = [
                        apollo2_api_client.models.twitter_annotation.TwitterAnnotation(
                            end = 56, 
                            normalized_text = '', 
                            probability = 1.337, 
                            start = 56, 
                            type = '', )
                        ], 
                    hashtags = [
                        apollo2_api_client.models.twitter_hashtag.TwitterHashtag(
                            end = 56, 
                            start = 56, 
                            tag = '', )
                        ], 
                    mentions = [
                        apollo2_api_client.models.twitter_mention.TwitterMention(
                            end = 56, 
                            id = '', 
                            start = 56, 
                            username = '', )
                        ], ), 
                id = '', 
                lang = '', 
                possibly_sensitive = True, 
                public_metrics = apollo2_api_client.models.twitter_public_metrics.TwitterPublicMetrics(
                    like_count = 56, 
                    quote_count = 56, 
                    reply_count = 56, 
                    retweet_count = 56, 
                    followers_count = 56, 
                    following_count = 56, 
                    listed_count = 56, 
                    tweet_count = 56, ), 
                reference_tweets = [
                    apollo2_api_client.models.twitter_referenced_tweet.TwitterReferencedTweet(
                        id = '', 
                        type = '', )
                    ], 
                reply_settings = '', 
                tweet_id = '', 
                twitter_author_screenname = '', 
                twitter_user_id = '', 
                annotations = [
                    apollo2_api_client.models.incas_annotation.IncasAnnotation(
                        attribute = '', 
                        confidence = 1.337, 
                        id = '', 
                        name = '', 
                        offsets = [
                            apollo2_api_client.models.incas_offset.IncasOffset(
                                begin = 56, 
                                end = 56, )
                            ], 
                        provider_name = '', 
                        text = '', 
                        type = '', )
                    ], 
                data_tags = [
                    ''
                    ], 
                embedded_urls = [
                    ''
                    ], 
                extra_attributes = [
                    apollo2_api_client.models.incas_extra_attribute.IncasExtraAttribute(
                        name = '', 
                        id = '', 
                        provider_name = '', 
                        attribute_key = '', 
                        attribute_value = '', )
                    ], 
                image_urls = [
                    ''
                    ], 
                segments = [
                    apollo2_api_client.models.incas_segment.IncasSegment(
                        annotations = [
                            apollo2_api_client.models.incas_annotation.IncasAnnotation(
                                attribute = '', 
                                confidence = 1.337, 
                                id = '', 
                                name = '', 
                                offsets = [
                                    apollo2_api_client.models.incas_offset.IncasOffset(
                                        begin = 56, 
                                        end = 56, )
                                    ], 
                                provider_name = '', 
                                text = '', 
                                type = '', )
                            ], 
                        description = '', 
                        extra_attributes = [
                            apollo2_api_client.models.incas_extra_attribute.IncasExtraAttribute(
                                name = '', 
                                id = '', 
                                provider_name = '', 
                                attribute_key = '', 
                                attribute_value = '', )
                            ], 
                        id = '', 
                        name = '', 
                        provider_name = '', )
                    ], 
                author = '', 
                content_text = '', 
                geolocation = apollo2_api_client.models.geo_location.GeoLocation(
                    latitude = 1.337, 
                    longitude = 1.337, 
                    country_code = '', ), 
                language = '', 
                media_type = 'News', 
                media_type_attributes = apollo2_api_client.models.incas_one_of_media_type_attributes.IncasOneOfMediaTypeAttributes(
                    reddit_data = apollo2_api_client.models.incas_reddit_data.IncasRedditData(), 
                    twitter_data = apollo2_api_client.models.incas_twitter_data.IncasTwitterData(
                        engagement_parent_id = '', 
                        engagement_type = 'ENGAGEMENT_UNSPECIFIED', 
                        follower_count = 56, 
                        following_count = 56, 
                        like_count = 56, 
                        mentioned_users = [
                            ''
                            ], 
                        retweet_count = 56, 
                        tweet_id = '', 
                        twitter_author_screenname = '', 
                        twitter_user_id = '', ), ), 
                mentioned_users = [
                    null
                    ], 
                name = '', 
                time_published = 56, 
                title = '', 
                url = '', 
                translated_content_text = '', 
                translated_title = ''
            )
        else :
            return Data(
        )
        """

    def testData(self):
        """Test Data"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()