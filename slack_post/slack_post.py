import requests
import json
import os

class slackPost:
    
    """
    Holds each attribute value and helper function to posting message to slack.

    Attributes
    ----------
    user_name : str
        User name displayed on slack.
    
    icon : str
        Name of icon.
        
    icons : list
        List of avairable icon name.
        
    channel : str
        Name of channel.
    """
    
    def getChInfo(self):
        
        """
        Parameters
        ----------
        CHs : dict
             key : channel name
             value : WebHookURL
        """
        
        # get channel name and url
        CHs = {}
        with open('./.setting','r') as f:
            for line in f:
                args = line.split(' ')
                ch = args[0]
                url = args[1]
                CHs[ch]=url
        return CHs
    
    def __init__(self):
        
        # default channel
        CHs = self.getChInfo()
        keys = list(CHs.keys())
        if len(keys)>0:
            self.channel = keys[0]
        
        # default user name
        self.username = 'me'
        
        # default icon name
        self.icon = u':ghost:'
        
        # set icon name list
        icons = []
        with open('./.emoji','r') as f:
            for icon in f:
                icons.append(icon.split('\n')[0])
        self.icons =  icons
        
    def addChannel(self,chName,url):
        
        """
        Parameters
        ----------
        chNames : str
             arbitraly name to detect channel
        
        url : str
             WebHookURL
        """
        
        # add channel url
        CHs = getChInfo()
        if not chName in CHs.keys():
            with open('./.setting','a') as f:
                f.write(chName+' '+url)

    def post(self,message, mention=''):
        
        """
        Parameters
        ----------
        message : str
             message to post
        
        mention : str
             channel -> @channel
             everyone -> @everyone
             here -> @here
        """
        
        # post massage to slack
        
        # get URL
        CHs = self.getChInfo()
        URL = CHs[self.channel]
        
        # add mention
        if mention == 'channel':
            message = '<!channel> '+message
        elif mention == 'everyone':
            message = '<!everyone> '+message
        elif mention == 'here':
            message = '<!here> '+message

        # post
        requests.post(URL, data = json.dumps({
        'text': message, # message
        'username': self.username, # username
        'icon_emoji': self.icon, # icon
        "link_names": 1 # mention
    }))