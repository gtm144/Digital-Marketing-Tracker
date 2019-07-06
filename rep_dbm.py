from oauth2client import client

flow = client.OAuth2WebServerFlow(
    client_id="Authenticationhere",
    client_secret="Passwordt",
    scope="https://www.googleapis.com/auth/doubleclickbidmanager",
    user_agent="use",
    redirect_uri='urn:ietf:wg:oauth:2.0:oob')


authorize_url = flow.step1_get_authorize_url()

print  authorize_url

code = raw_input('Code: ').strip()

try:
  credentials = flow.step2_exchange(code)
except client.FlowExchangeError, e:
  print 'Authentication has failed'
  sys.exit(1)
