# intapi.py
# This file is auto-generated from the same code that generates
# https://docs.patreon.com. Community pull requests against this
# file may not be accepted.

import six
import cloudscraper

from patreon.jsonapi.parser import JSONAPIParser
from patreon.jsonapi.url_util import build_url
from patreon.utils import user_agent_string
from patreon.version_compatibility.utc_timezone import utc_timezone
from six.moves.urllib.parse import urlparse, parse_qs, urlencode


class InternalAPI(object):
    def __init__(self, browser = {'browser': 'chrome', 'mobile': False}, cookies = None):
        super(InternalAPI, self).__init__()
        self.scraper = cloudscraper.create_scraper(browser = browser)
        if cookies:
            self.scraper.cookies = cookies
    
    def do_login(self, username, password):
        login_payload = {'data':  { 'email': username, 'password': password }}
        login_req = self.scraper.post("https://api.patreon.com/login", json=login_payload)
        login_json = login_req.json()
        if login_json.get('errors'):
            return login_json
        return JSONAPIParser(login_json)
          
    def get_addresses(self, includes=None, fields=None):
        url = 'addresses'
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )

    def get_attachments_by_post_id(self, resource_id, includes=None, fields=None):
        url = 'posts/{}/attachments'.format(resource_id)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )        
        
    def get_bills(self, includes=None, fields=None):
        url = 'bills'
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )        
        
    def get_cards(self, includes=None, fields=None):
        url = 'cards'
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )
        
    def get_campaign_by_id(self, resource_id, includes=None, fields=None):
        url = 'campaigns/{}'.format(resource_id)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )        
    
    def get_catagories(self, includes=None, fields=None):
        url = 'catagories'
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )
        
    def get_comment_by_id(self, resource_id, includes=None, fields=None):
        url = 'comment/{}'.format(resource_id)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )

    def get_comments_by_post_id(self, resource_id, includes=None, fields=None):
        url = 'posts/{}/comments'.format(resource_id)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )        

    def get_conversations(self, page_size=20, cursor=None, includes=None, fields=None):
        url = 'conversations'
        params = {'page[count]': page_size}
        if cursor:
            try:
                cursor = self.__as_utc(cursor).isoformat()
            except AttributeError:
                pass
            params.update({'page[cursor]': cursor})
        url += "?" + urlencode(params)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )
        
    def get_current_user(self, includes=None, fields=None):
        url = 'current_user'
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )        
        
    def get_goal_by_id(self, resource_id, includes=None, fields=None):
        url = 'goals/{}'.format(resource_id)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )        

    def get_like_by_id(self, resource_id, includes=None, fields=None):
        url = 'likes/{}'.format(resource_id)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )        
        
    def get_likes_by_post_id(self, resource_id, includes=None, fields=None):
        url = 'posts/{}/likes'.format(resource_id)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )        
       
    def get_notifications(self, includes=None, fields=None):
        url = 'notifications'
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )
    
    def get_pledges(self, includes=None, fields=None):
        url = 'pledges'
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )

    def get_post_by_id(self, resource_id, includes=None, fields=None):
        url = 'posts/{}'.format(resource_id)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )        
  
    def get_posts_by_campaign_id(self, resource_id, includes=None, fields=None):
        url = 'campaigns/{}/posts'.format(resource_id)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )

    def get_reward_by_id(self, resource_id, includes=None, fields=None):
        url = 'rewards/{}'.format(resource_id)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )        
    
    def get_settings(self, includes=None, fields=None):
        url = 'settings'
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )
        
    def get_stream(self, page_size=20, cursor=None, includes=None, fields=None, filters=None):
        url = 'stream'
        params = {'page[count]': page_size}
        if cursor:
            try:
                cursor = self.__as_utc(cursor).isoformat()
            except AttributeError:
                pass
            params.update({'page[cursor]': cursor})
        url += "?" + urlencode(params)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields, filters=filters)
        )
        
    def get_tags_by_campaign_id(self, resource_id, includes=None, fields=None):
        url = 'campaigns/{}/post-tags'.format(resource_id)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )

    def get_user_by_id(self, resource_id, includes=None, fields=None):
        url = 'user/{}'.format(resource_id)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )        
        
    def get_webhooks(self, page_size=20, cursor=None, includes=None, fields=None):
        url = 'webhooks'
        params = {'page[count]': page_size}
        if cursor:
            try:
                cursor = self.__as_utc(cursor).isoformat()
            except AttributeError:
                pass
            params.update({'page[cursor]': cursor})
        url += "?" + urlencode(params)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )        
        
    def get_webhook_by_id(self, resource_id, includes=None, fields=None):
        url = 'webhooks/{}'.format(resource_id)
        return self.__get_jsonapi_doc(
            build_url(url, includes=includes, fields=fields)
        )                               

    @staticmethod
    def extract_cursor(jsonapi_document, cursor_path='links.next'):
        def head_and_tail(path):
            if path is None:
                return None, None
            head_tail = path.split('.', 1)
            return head_tail if len(head_tail) == 2 else (head_tail[0], None)

        if isinstance(jsonapi_document, JSONAPIParser):
            jsonapi_document = jsonapi_document.json_data

        head, tail = head_and_tail(cursor_path)
        current_dict = jsonapi_document
        while head and type(current_dict) == dict and head in current_dict:
            current_dict = current_dict[head]
            head, tail = head_and_tail(tail)

        # Path was valid until leaf, at which point nothing was found
        if current_dict is None or (head is not None and tail is None):
            return None
        # Path stopped before leaf was reached
        elif current_dict and type(current_dict) != six.text_type:
            raise Exception(
                'Provided cursor path did not result in a link', current_dict
            )

        link = current_dict
        query_string = urlparse(link).query
        parsed_query_string = parse_qs(query_string)
        if 'page[cursor]' in parsed_query_string:
            return parsed_query_string['page[cursor]'][0]
        else:
            return None

    # Internal methods
    def __get_jsonapi_doc(self, suffix):
        response_json = self.__get_json(suffix)
        if response_json.get('errors'):
            return response_json
        return JSONAPIParser(response_json)

    def __get_json(self, suffix):
        response = self.scraper.get("https://www.patreon.com/api/{}".format(suffix))
        return response.json()

    @staticmethod
    def __as_utc(dt):
        if hasattr(dt, 'tzinfo'):
            if dt.tzinfo:
                return dt.astimezone(utc_timezone())
            else:
                return dt.replace(tzinfo=utc_timezone())
        return dt
        