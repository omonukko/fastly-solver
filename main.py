import requests, hashlib, re


string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def answer(base, hash):
    for a in range(len(string)):
        for a2 in range(len(string)):
            if hashlib.sha256((base + string[a] + string[a2]).encode()).hexdigest() == hash:
                return string[a] + string[a2]

def search(query: str):
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0"
    })
    c = session.get(f"https://pypi.org/search/?q={query}")
    session.cookies.update(c.cookies.get_dict())
    js = c.text.split("script.src = '")[1].split("'")[0]
    content = session.get(f"https://pypi.org{js}")
    j = content.text
    print(content.url, content.status_code)
    t = re.search(r'init\(\s*\[.*?"ty"\s*:\s*"pat".*?\],\s*"(?P<v>[^"]+)"', j)
    if t:
        t = t.group("v")
    else:
        raise Exception("Failed to get init data")
    d = session.post(
        f"https://pypi.org/{js.split("/")[1].split("?reload=true")[0]}/fst-post-back",
        json={
            "token": t,
            "data": [{
                "ty": "pat",
                "auth": ""
            }]
        },
    ).json()
    print(d)
    data = d["ch"][0]["data"]
    base = data["base"]
    hash = data["hash"]
    hmac = data["hmac"]
    expires = data["expires"]
    ans = answer(base, hash)
    check = session.post(
        f"https://pypi.org/{js.split('/')[1]}/fst-post-back", 
        json={
            "token": d["tok"],
            "data": [
                {
                    "ty": "pow",
                    "base": base,
                    "answer": ans,
                    "hmac": hmac,
                    "expires": expires
                },
                {
			        "bot_detection_result": {
		            "bot_detected": False,
			        "bot_kind": None
		            },
		            "browser_metrics": {
			            "client_data": "{\"rtt\":{\"error\":\"BotdError: navigator.connection is undefined\"},\"android\":{\"value\":false},\"browserKind\":{\"value\":\"firefox\"},\"browserEngineKind\":{\"value\":\"gecko\"},\"documentFocus\":{\"value\":true},\"userAgent\":{\"value\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0\"},\"appVersion\":{\"value\":\"5.0 (Windows)\"},\"windowSize\":{\"value\":{\"outerWidth\":1252,\"outerHeight\":1080,\"innerWidth\":1185,\"innerHeight\":1032}},\"pluginsLength\":{\"value\":5},\"pluginsArray\":{\"value\":true},\"productSub\":{\"value\":\"20100101\"},\"windowExternal\":{\"value\":\"[object External]\"},\"mimeTypesConsistent\":{\"value\":true},\"evalLength\":{\"value\":37},\"webGL\":{\"value\":{\"vendor\":\"Mozilla\",\"renderer\":\"ANGLE (Intel, Intel(R) HD Graphics Direct3D11 vs_5_0 ps_5_0), or similar\"}},\"webDriver\":{\"value\":false},\"languages\":{\"value\":[[\"ja\"],[\"ja\",\"en-US\",\"en\"]]},\"documentElementKeys\":{\"value\":[\"lang\"]},\"functionBind\":{\"value\":\"function bind() {\\n    [native code]\\n}\"},\"distinctiveProps\":{\"value\":{\"awesomium\":false,\"cef\":false,\"cefsharp\":false,\"coachjs\":false,\"fminer\":false,\"geb\":false,\"nightmarejs\":false,\"phantomas\":false,\"phantomjs\":false,\"rhino\":false,\"selenium\":false,\"webdriverio\":false,\"webdriver\":false,\"headless_chrome\":false}},\"iframeSrcdoc\":{\"value\":{\"hasSelfGet\":false}},\"notificationPermissions\":{\"value\":false}}",
			            "error_trace": f"\"e@https://pypi.org/{js.split('/')[1]}:1:10131\\e/</</</</<@https://pypi.org/{js.split('/')[1]}:1:5708\\c@https://pypi.org/{js.split('/')[1]}:1:4849\\e/u/<@https://pypi.org/{js.split('/')[1]}:1:4132\\e/<@https://pypi.org/{js.split('/')[1]}:1:3850\\e@https://pypi.org/{js.split('/')[1]}:1:3647\\e/</</<@https://pypi.org/{js.split('/')[1]}:1:5547\\e/</<@https://pypi.org/{js.split('/')[1]}:1:5524\\c@https://pypi.org/{js.split('/')[1]}:1:4849\\e/u/<@https://pypi.org/{js.split('/')[1]}:1:4132\\e/<@https://pypi.org/{js.split('/')[1]}:1:3850\\e@https://pypi.org/{js.split('/')[1]}:1:3647\\e@https://pypi.org/{js.split('/')[1]}:1:5382\\e.prototype.collect/e8</<@https://pypi.org/{js.split('/')[1]}:1:45025\\c@https://pypi.org/{js.split('/')[1]}:1:4849\\e/u/<@https://pypi.org/{js.split('/')[1]}:1:4132\\e/<@https://pypi.org/{js.split('/')[1]}:1:3850\\e@https://pypi.org/{js.split('/')[1]}:1:3647\\e.prototype.collect@https://pypi.org/{js.split('/')[1]}:1:44921\\e/</<@https://pypi.org/{js.split('/')[1]}:1:17881\\c@https://pypi.org/{js.split('/')[1]}:1:4849\\e/u/<@https://pypi.org/{js.split('/')[1]}:1:4132\\e/<@https://pypi.org/{js.split('/')[1]}:1:3850\\e@https://pypi.org/{js.split('/')[1]}:1:3647\\e@https://pypi.org/{js.split('/')[1]}:1:17765\\e9/e9</<@https://pypi.org/{js.split('/')[1]}:1:45348\\c@https://pypi.org/{js.split('/')[1]}:1:2600\\l/u/<@https://pypi.org/{js.split('/')[1]}:1:1891\\n@https://pypi.org/{js.split('/')[1]}:1:201\\u@https://pypi.org/{js.split('/')[1]}:1:413\\promise callback*n@https://pypi.org/{js.split('/')[1]}:1:280\\u@https://pypi.org/{js.split('/')[1]}:1:413\\r/</<@https://pypi.org/{js.split('/')[1]}:1:472\\r/<@https://pypi.org/{js.split('/')[1]}:1:353\\e9@https://pypi.org/{js.split('/')[1]}:1:45657\\e6@https://pypi.org/{js.split('/')[1]}:1:45124\\tt/tt</<@https://pypi.org/{js.split('/')[1]}:1:46132\\c@https://pypi.org/{js.split('/')[1]}:1:2600\\l/u/<@https://pypi.org/{js.split('/')[1]}:1:1891\\n@https://pypi.org/{js.split('/')[1]}:1:201\\u@https://pypi.org/{js.split('/')[1]}:1:413\\r/</<@https://pypi.org/{js.split('/')[1]}:1:472\\r/<@https://pypi.org/{js.split('/')[1]}:1:353\\te@https://pypi.org/{js.split('/')[1]}:1:45708\\ts/ts</<@https://pypi.org/{js.split('/')[1]}:1:49647\\c@https://pypi.org/{js.split('/')[1]}:1:2600\\l/u/<@https://pypi.org/{js.split('/')[1]}:1:1891\\n@https://pypi.org/{js.split('/')[1]}:1:201\\u@https://pypi.org/{js.split('/')[1]}:1:413\\promise callback*n@https://pypi.org/{js.split('/')[1]}:1:280\\u@https://pypi.org/{js.split('/')[1]}:1:413\\r/</<@https://pypi.org/{js.split('/')[1]}:1:472\\r/<@https://pypi.org/{js.split('/')[1]}:1:353\\ts@https://pypi.org/{js.split('/')[1]}:1:50229\\tc@https://pypi.org/{js.split('/')[1]}:1:49104\\tu/tu</<@https://pypi.org/{js.split('/')[1]}:1:48528\\c@https://pypi.org/{js.split('/')[1]}:1:2600\\l/u/<@https://pypi.org/{js.split('/')[1]}:1:1891\\n@https://pypi.org/{js.split('/')[1]}:1:201\\u@https://pypi.org/{js.split('/')[1]}:1:413\\promise callback*n@https://pypi.org/{js.split('/')[1]}:1:280\\u@https://pypi.org/{js.split('/')[1]}:1:413\\r/</<@https://pypi.org/{js.split('/')[1]}:1:472\\r/<@https://pypi.org/{js.split('/')[1]}:1:353\\to@https://pypi.org/{js.split('/')[1]}:1:47886\\ti@https://pypi.org/{js.split('/')[1]}:1:47529\\@https://pypi.org/{js.split('/')[1]}:1:50349\\\""
		            },
		            "ty": "clientmetrics",
		            "webdriver": False
		        }
            ]
        }
    )
    print(check.cookies.get_dict())
    print(check.text)
    if check.json().get("status", None) == "success":
        session.cookies.update(check.cookies.get_dict())
        return session.get(f"https://pypi.org/search/?q={query}")
    else:
        raise Exception("Failed to solve fastly")
    
print(search("requests"))
