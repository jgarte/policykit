from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, HttpResponse
import urllib.request
import urllib.parse
import logging

logger = logging.getLogger(__name__)


def execute_action(action):
    community_integration = action.community_integration
    
    obj = action.content_object
    call = community_integration.API + obj.API_METHOD
    
    
    obj_fields = [f.name for f in obj._meta.get_fields()]
    
    data = {'token': community_integration.access_token}
    
    for item in obj_fields:
        try :
            if item != 'id':
                value = getattr(obj, item)
                data[item] = value
        except obj.DoesNotExist:
            continue
        
    
    logger.info(data)
    
    data = urllib.parse.urlencode(data).encode('ascii')

    response = urllib.request.urlopen(url=call, data=data)
    
    html = response.read()
    print(html)
    
    print(call)
