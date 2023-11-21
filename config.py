import os,sys
api_token=os.environ['REDCAP_API_TOKEN']
config = dict(
    api_super_token = 'ABCD1234ABCD1234ABCD1234ABCD1234ABCD1234ABCD1234ABCD1234ABCD1234',
    api_token       = api_token,
    api_url         = 'https://redcap.wustl.edu/redcap/api/'
)
