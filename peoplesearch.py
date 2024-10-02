# import requests


# TOKEN = "77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U1A+MGUudHxhZGZzfDE0MjkyMDNAbGVhcm43NS5jYSwwZS50fGFkZnN8MTQyOTIwM0BsZWFybjc1LmNhLDEzMzcyMTg5ODE4NDU5NDEyNSxUcnVlLEEzT1FnaUs1T2V1a3gxOEtaT0l4T0pqMktPUG5vV1lSQmRGTXEwZDJKNU56MHJXemMxcWZNbldDNGlwSEFYdU53Z0t0VjVNMnZ2WmdTZ293aVB6SzlDcTJMbjA0UlkvcmF0aHJFdlVyYXBvZ1FpK0VOQWhYRnRQMFVNWHFic2Z2WkxhYTFLTXU0WXc1Z1YvSFN5Vmk0Ykw4Q0VnK2t4WFROVExVRUNYMTgrT3I2d1VCSVFPaDAxbUk1WFhLaDUybGFJWmk0cTI4OUVDaEdwZzBGVThta3Z6WW1HL0VySkxYUHpKaXlZK3VBODU2bk5hYStBQjJ6RUJJWkJxdEd1U0t2aG1rVUNKMnhWWHI4MWFDS25uejJjdjlyRXhLdWZFYnN5STAxTEhjVWw4eUFjdjY4c1JyNVV5bFY0NzA4RnpVa0FWbFU4bzdIbHRuTmkrRVdLNUlnUT09LGh0dHBzOi8vcG9ydGFsLm1wc2QuY2EvPC9TUD4="
# HOST = "https://portal.mpsd.ca"

# def POST(endpoint, payload):
#     return requests.post(HOST + endpoint, headers={"Cookie": f'SearchSession=70c7c6b2%2D42ee%2D490c%2Dbc86%2D43c81a167f76; FedAuth=77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48U1A+MGUudHxhZGZzfDE0MjkyMDNAbGVhcm43NS5jYSwwZS50fGFkZnN8MTQyOTIwM0BsZWFybjc1LmNhLDEzMzcyMTg5ODE4NDU5NDEyNSxUcnVlLEEzT1FnaUs1T2V1a3gxOEtaT0l4T0pqMktPUG5vV1lSQmRGTXEwZDJKNU56MHJXemMxcWZNbldDNGlwSEFYdU53Z0t0VjVNMnZ2WmdTZ293aVB6SzlDcTJMbjA0UlkvcmF0aHJFdlVyYXBvZ1FpK0VOQWhYRnRQMFVNWHFic2Z2WkxhYTFLTXU0WXc1Z1YvSFN5Vmk0Ykw4Q0VnK2t4WFROVExVRUNYMTgrT3I2d1VCSVFPaDAxbUk1WFhLaDUybGFJWmk0cTI4OUVDaEdwZzBGVThta3Z6WW1HL0VySkxYUHpKaXlZK3VBODU2bk5hYStBQjJ6RUJJWkJxdEd1U0t2aG1rVUNKMnhWWHI4MWFDS25uejJjdjlyRXhLdWZFYnN5STAxTEhjVWw4eUFjdjY4c1JyNVV5bFY0NzA4RnpVa0FWbFU4bzdIbHRuTmkrRVdLNUlnUT09LGh0dHBzOi8vcG9ydGFsLm1wc2QuY2EvPC9TUD4=; WSS_FullScreenMode=false; 0c37852b34d0418e91c62ac25af4be5bb0c382e7c04941d9956c1bd19c8283efi%3A0e%2Et%7Cadfs%7C1429203%40learn75%2Eca=0; 0c37852b34d0418e91c62ac25af4be5b03f530e8ffdc4cd5baf00d5593e6919f=%3Ci%20p%3D%22f9b9f7f1%2D7a2e%2D4ab5%2D842a%2Daef201fe123b%22%20m%3D%22fPEbwtNspqnYSq5S2SQf3FtiCS7h%2FFCMlxHkF%2BE0nlQ%3D%22%20%2F%3E; WOPISessionContext=https://portal.mpsd.ca/class/5pqj64q/_LAYOUTS/15/scholantis/sites/app/assignments/app.aspx#/'}, data=payload)


# def GET(endpoint):
#     return requests.get(HOST + endpoint, headers={"Cookie": f"SearchSession=70c7c6b2%2D42ee%2D490c%2Dbc86%2D43c81a167f76;FedAuth={TOKEN};"})

# print(POST("/my/_vti_bin/client.svc/ProcessQuery", open("payload.xml", "r").read()).text)
token = "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImU3NjNlMGJhLTgzMDAtNDk4YS04MzI1LWQ4Mjk4NGFlMTViOSIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE3MjczNjY3NzgsImV4cCI6MTcyNzM3MDM3OCwiaXNzIjoiaHR0cHM6Ly9hcGkuYnJpZ2h0c3BhY2UuY29tL2F1dGgiLCJhdWQiOiJodHRwczovL2FwaS5icmlnaHRzcGFjZS5jb20vYXV0aC90b2tlbiIsInN1YiI6IjIxODMwMiIsInRlbmFudGlkIjoiNjkwODIyMjMtNDNjNC00NTM4LTljNTctYzQ5MDQ3Mzc0NTQ0IiwiYXpwIjoibG1zIiwic2NvcGUiOiIqOio6KiIsImp0aSI6IjYzMDM0Y2ViLTQwMzMtNDE0My1iNjc4LTMyNDU3YmRlNDM5YSJ9.Pq3a4QjihBAd0rn0WEuzrmeI4EykMPyefGIkRf05Tf-AKj8fhlzf-w5r6veZLQrwJCxZ9aBUpQBZI9z_MwR_xjR0daTFZ-bifgadWfBCaI_yUM7hiHHRKLtrN52-4oVI7vp_5RSTTzFCZ7UZSvCC7ilVxPgopdEDUDFtQM8_MbVHlo3thPhKeQu_SlPrypKDKnl93sxE-cmwz2eS8ADvDS5C6QxBEAQrnsptCCHuxcmMXWdvA3ZIS-9ED_75XtUaNADzEy2rDMmp40abNq39kgJUTme0IIbFbIl5b_NaxUSrN9hKHv17rhqcAKNJQlKzQ8hkKBsJnzdjwm4UvX72-Q"

import requests
def CreateSessionString(session, sessionsig):
    return f"d2lSessionVal={session}; d2lSecureSessionVal={sessionsig}"
def CreateXSRF(session, sessionsig):
    url = "https://sd75.onlinelearningbc.com/d2l/wcs/media-library/?ou=73477"
    return requests.get(url,headers={"Cookie":CreateSessionString(session, sessionsig)}).text.split('D2L.LP.Web.Authentication.Xsrf.Init\\",\\"P\\":[\\"d2l_referrer\\",\\"')[1].split("\\\",")[0]
# print(CreateXSRF())
def GetAccessToken(session, sessionsig):
    print(requests.post("https://sd75.onlinelearningbc.com/d2l/lp/auth/oauth2/token", headers={"x-csrf-token":CreateXSRF(),"Cookie":CreateSessionString(session, sessionsig), "Authorization": token,
                                                                                                "content-type":
                                                                                                "application/x-www-form-urlencoded"},
                        data="scope=*:*:*").json()["access_token"])
print(GetAccessToken())