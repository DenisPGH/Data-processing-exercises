import json
import os

import requests

#_sn:#8$_se:26$_ss:0$_st:1654584130867$browser_client_id:xfsq0qy$user_anon_id:anon_1520784316553$dc_visit:8$ses_id:1654580820603%3Bexp-session$_pn:5%3Bexp-session$dc_event:26%3Bexp-session$dc_region:eu-central-1%3Bexp-session = os.getenv('_sn:8$_se:26$_ss:0$_st:1654584130867$browser_client_id:xfsq0qy$user_anon_id:anon_1520784316553$dc_visit:8$ses_id:1654580820603%3Bexp-session$_pn:5%3Bexp-session$dc_event:26%3Bexp-session$dc_region:eu-central-1%3Bexp-session')
#_sn:#8$_se:26$_ss:0$_st:1654584130867$browser_client_id:xfsq0qy$user_anon_id:anon_1520784316553$dc_visit:8$ses_id:1654580820603%3Bexp-session$_pn:5%3Bexp-session$dc_event:26%3Bexp-session$dc_region:eu-central-1%3Bexp-session; = os.getenv('_sn:8$_se:26$_ss:0$_st:1654584130867$browser_client_id:xfsq0qy$user_anon_id:anon_1520784316553$dc_visit:8$ses_id:1654580820603%3Bexp-session$_pn:5%3Bexp-session$dc_event:26%3Bexp-session$dc_region:eu-central-1%3Bexp-session;')

cookies = {
    'ASID': '02dc0aeb-6173-4a16-b9fd-90c6af5f4285|20220520|20',
    'CONSENTMGR': 'c1:1%7Cc4:1%7Cc2:0%7Cc3:0%7Cc5:0%7Cc6:0%7Cc7:0%7Cc8:0%7Cc9:0%7Cc10:0%7Cc11:0%7Cc12:0%7Cc13:0%7Cc14:0%7Cc15:0%7Cts:1653026236856%7Cconsent:true',
    'JS24_CONSENT': 'sn|ff|mr|1',
    '_gcl_au': '1.1.1468808755.1653026238',
    '_hjSessionUser_373146': 'eyJpZCI6ImI1ZmQwMGVmLTZjNGUtNWVhMy05NzA3LWZmOGQ3ZmIzMDNlOCIsImNyZWF0ZWQiOjE2NTMwMjYyMzgwOTMsImV4aXN0aW5nIjp0cnVlfQ==',
    '_gid': 'GA1.2.1579453522.1654505721',
    '_JS24A': '0',
    'ASP.NET_SessionId': 'xm2lp2rz4wpaxngmizdyilid',
    '__RequestVerificationToken': 'fm0XFBUtpU2skpslyx1_STV8ESR2P7DdX6TZRh9tLoEpzKthvw2S9lX4TC3GWzBYJfZlmMpHA68LW9auz9mOwbezvBI1',
    'xm_jobweb': '3389002762.20480.0000',
    '_hjAbsoluteSessionInProgress': '1',
    '_hjSession_373146': 'eyJpZCI6ImE2MTc1ZmY4LWQzMDEtNGE5Zi1hNzYyLTY5YjQzZTg2MWUwYyIsImNyZWF0ZWQiOjE2NTQ1ODA4MjIxOTgsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjIncludedInPageviewSample': '1',
    '_hjIncludedInSessionSample': '0',
    'TS01ce6450': '017721f21f79e863847a7f7dc3e7bb2c1f494ed1e9bec96e77d6dd676c4f09689a788ddf59d85c48d3225b743c155760055f3e3ed9',
    'ViewSource': '',
    '_ga_3EKC6G4KSB': 'GS1.1.1654580821.5.1.1654582330.0',
    #'utag_main': f"v_id:0180e00aa34f001afe859fddd98d0506f0029067007e8{_sn:8$_se:26$_ss:0$_st:1654584130867$browser_client_id:xfsq0qy$user_anon_id:anon_1520784316553$dc_visit:8$ses_id:1654580820603%3Bexp-session$_pn:5%3Bexp-session$dc_event:26%3Bexp-session$dc_region:eu-central-1%3Bexp-session}",
    '_ga': 'GA1.1.xfsq0qy',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': f"ASID=02dc0aeb-6173-4a16-b9fd-90c6af5f4285|20220520|20; CONSENTMGR=c1:1%7Cc4:1%7Cc2:0%7Cc3:0%7Cc5:0%7Cc6:0%7Cc7:0%7Cc8:0%7Cc9:0%7Cc10:0%7Cc11:0%7Cc12:0%7Cc13:0%7Cc14:0%7Cc15:0%7Cts:1653026236856%7Cconsent:true; JS24_CONSENT=sn|ff|mr|1; _gcl_au=1.1.1468808755.1653026238; _hjSessionUser_373146=eyJpZCI6ImI1ZmQwMGVmLTZjNGUtNWVhMy05NzA3LWZmOGQ3ZmIzMDNlOCIsImNyZWF0ZWQiOjE2NTMwMjYyMzgwOTMsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.1579453522.1654505721; _JS24A=0; ASP.NET_SessionId=xm2lp2rz4wpaxngmizdyilid; __RequestVerificationToken=fm0XFBUtpU2skpslyx1_STV8ESR2P7DdX6TZRh9tLoEpzKthvw2S9lX4TC3GWzBYJfZlmMpHA68LW9auz9mOwbezvBI1; xm_jobweb=3389002762.20480.0000; _hjAbsoluteSessionInProgress=1; _hjSession_373146=eyJpZCI6ImE2MTc1ZmY4LWQzMDEtNGE5Zi1hNzYyLTY5YjQzZTg2MWUwYyIsImNyZWF0ZWQiOjE2NTQ1ODA4MjIxOTgsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjIncludedInSessionSample=0; TS01ce6450=017721f21f79e863847a7f7dc3e7bb2c1f494ed1e9bec96e77d6dd676c4f09689a788ddf59d85c48d3225b743c155760055f3e3ed9; ViewSource=; _ga_3EKC6G4KSB=GS1.1.1654580821.5.1.1654582330.0; utag_main=v_id:0180e00aa34f001afe859fddd98d0506f0029067007e8{_sn:8$_se:26$_ss:0$_st:1654584130867$browser_client_id:xfsq0qy$user_anon_id:anon_1520784316553$dc_visit:8$ses_id:1654580820603%3Bexp-session$_pn:5%3Bexp-session$dc_event:26%3Bexp-session$dc_region:eu-central-1%3Bexp-session;} _ga=GA1.1.xfsq0qy",
    'Origin': 'https://www.jobscout24.ch',
    'Referer': 'https://www.jobscout24.ch/de/jobs/?psz=3000&actuality=0&p=2',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'psz': '3000',
    'p': '2',
    'actuality': '0',
}

response = requests.get('https://www.jobscout24.ch/de/jobs/', params=params, cookies=cookies, headers=headers)
print(response.text)

# result=json.loads(response.text)
# print(result['markup'])
# with open('jobscout.txt', 'w') as file:
#     file.write(result['markup'])

"""
<div class="upper-line">
	<a href="/de/job/dipl-wirtschaftspr%C3%BCfer/7376622/" 
       class="job-link-detail job-title" 
       title="Dipl. Wirtschaftsprüfer/in" 
       target="_self" 
       rel=""
       >Dipl. Wirtschaftsprüfer/in</a>

	</div>
"""