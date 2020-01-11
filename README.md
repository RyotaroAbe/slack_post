# slack_post
Posting message to slack from python script.

# Requirements
- Python2 or Python3
- requests
- json

# Usage
## Incoming webhooks
To use this module, you have to get the incoming webhooks.
https://api.slack.com/messaging/webhooks

Please acquire the Webhook URLs for Your Workspace.
This module post the message to the channel which be indicated by the URL.

## Setting
When the initial import of this module, '.setting' is made.
This file store the information about the Webhook URL and arbitraly channel name.
You can add the URL to the file with the following command.
```
import slack_post.slack_post as slpost
slack = slpost.slackPost()
slack.addChannel('channel1','XXX')
```

## Confirm channel information
```
slack.getChInfo()
```
-> {'channel1': 'XXX'}

## Posting message
```
slack.channel = 'channel1'
slack.post('Hello!',mention='everyone')
```
-> @everyone Hello!


# Version
version 1.0 #2020/01/11

# Author
Ryotaro Abe
