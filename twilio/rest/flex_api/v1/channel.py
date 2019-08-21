# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class ChannelList(ListResource):
    """  """

    def __init__(self, version):
        """
        Initialize the ChannelList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v1.channel.ChannelList
        :rtype: twilio.rest.flex_api.v1.channel.ChannelList
        """
        super(ChannelList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Channels'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams ChannelInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.channel.ChannelInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.channel.ChannelInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ChannelInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ChannelInstance
        :rtype: twilio.rest.flex_api.v1.channel.ChannelPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return ChannelPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ChannelInstance
        :rtype: twilio.rest.flex_api.v1.channel.ChannelPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return ChannelPage(self._version, response, self._solution)

    def create(self, flex_flow_sid, identity, chat_user_friendly_name,
               chat_friendly_name, target=values.unset,
               chat_unique_name=values.unset, pre_engagement_data=values.unset,
               task_sid=values.unset, task_attributes=values.unset,
               long_lived=values.unset):
        """
        Create a new ChannelInstance

        :param unicode flex_flow_sid: The unique ID of the FlexFlow
        :param unicode identity: Chat User identity
        :param unicode chat_user_friendly_name: Customer friendly name
        :param unicode chat_friendly_name: Chat channel friendly name
        :param unicode target: Target Contact Identity
        :param unicode chat_unique_name: Chat channel unique name
        :param unicode pre_engagement_data: Pre-engagement data
        :param unicode task_sid: TaskRouter Task Sid.
        :param unicode task_attributes: Task attributes to be added for the TaskRouter Task
        :param bool long_lived: Long Lived flag

        :returns: Newly created ChannelInstance
        :rtype: twilio.rest.flex_api.v1.channel.ChannelInstance
        """
        data = values.of({
            'FlexFlowSid': flex_flow_sid,
            'Identity': identity,
            'ChatUserFriendlyName': chat_user_friendly_name,
            'ChatFriendlyName': chat_friendly_name,
            'Target': target,
            'ChatUniqueName': chat_unique_name,
            'PreEngagementData': pre_engagement_data,
            'TaskSid': task_sid,
            'TaskAttributes': task_attributes,
            'LongLived': long_lived,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return ChannelInstance(self._version, payload, )

    def get(self, sid):
        """
        Constructs a ChannelContext

        :param sid: Flex Chat Channel Sid

        :returns: twilio.rest.flex_api.v1.channel.ChannelContext
        :rtype: twilio.rest.flex_api.v1.channel.ChannelContext
        """
        return ChannelContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a ChannelContext

        :param sid: Flex Chat Channel Sid

        :returns: twilio.rest.flex_api.v1.channel.ChannelContext
        :rtype: twilio.rest.flex_api.v1.channel.ChannelContext
        """
        return ChannelContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.ChannelList>'


class ChannelPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the ChannelPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.flex_api.v1.channel.ChannelPage
        :rtype: twilio.rest.flex_api.v1.channel.ChannelPage
        """
        super(ChannelPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ChannelInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.channel.ChannelInstance
        :rtype: twilio.rest.flex_api.v1.channel.ChannelInstance
        """
        return ChannelInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.ChannelPage>'


class ChannelContext(InstanceContext):
    """  """

    def __init__(self, version, sid):
        """
        Initialize the ChannelContext

        :param Version version: Version that contains the resource
        :param sid: Flex Chat Channel Sid

        :returns: twilio.rest.flex_api.v1.channel.ChannelContext
        :rtype: twilio.rest.flex_api.v1.channel.ChannelContext
        """
        super(ChannelContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Channels/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a ChannelInstance

        :returns: Fetched ChannelInstance
        :rtype: twilio.rest.flex_api.v1.channel.ChannelInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ChannelInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the ChannelInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.ChannelContext {}>'.format(context)


class ChannelInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, sid=None):
        """
        Initialize the ChannelInstance

        :returns: twilio.rest.flex_api.v1.channel.ChannelInstance
        :rtype: twilio.rest.flex_api.v1.channel.ChannelInstance
        """
        super(ChannelInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'flex_flow_sid': payload['flex_flow_sid'],
            'sid': payload['sid'],
            'user_sid': payload['user_sid'],
            'task_sid': payload['task_sid'],
            'url': payload['url'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ChannelContext for this ChannelInstance
        :rtype: twilio.rest.flex_api.v1.channel.ChannelContext
        """
        if self._context is None:
            self._context = ChannelContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The ID of the account that owns this Workflow
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def flex_flow_sid(self):
        """
        :returns: The unique ID of the FlexFlow
        :rtype: unicode
        """
        return self._properties['flex_flow_sid']

    @property
    def sid(self):
        """
        :returns: Flex Chat Channel Sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def user_sid(self):
        """
        :returns: Chat User Sid.
        :rtype: unicode
        """
        return self._properties['user_sid']

    @property
    def task_sid(self):
        """
        :returns: TaskRouter Task Sid.
        :rtype: unicode
        """
        return self._properties['task_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def date_created(self):
        """
        :returns: The time the Flex Chat Channel was created, given as GMT in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The time the Flex Chat Channel was last updated, given as GMT in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_updated']

    def fetch(self):
        """
        Fetch a ChannelInstance

        :returns: Fetched ChannelInstance
        :rtype: twilio.rest.flex_api.v1.channel.ChannelInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the ChannelInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.ChannelInstance {}>'.format(context)
