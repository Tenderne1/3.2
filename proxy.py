##
#
#   Copyright (C) 2002-2022 MlgmXyysd All Rights Reserved.
#
##

##
#
#   Genshin Impact script for mitmproxy
#
#   https://github.com/MlgmXyysd/
#
#   *Original fiddler script from https://github.lunatic.moe/fiddlerscript
#
#   Environment requirement:
#     - mitmdump from mitmproxy
#
#   @author MlgmXyysd
#   @version 1.1
#
##

from mitmproxy import http
from proxy_config import USE_SSL
from proxy_config import REMOTE_HOST
from proxy_config import REMOTE_PORT

class MlgmXyysd_Genshin_Impact_Proxy:
    def request(self, flow: http.HTTPFlow) -> None:
        if flow.request.host.endswith(".hoyoverse.com") or flow.request.host.endswith(".yuanshen.com") or flow.request.host.endswith(".mihoyo.com"):
            if USE_SSL:
                flow.request.scheme = "https"
            else:
                flow.request.scheme = "http"
            flow.request.host = REMOTE_HOST
            flow.request.port = REMOTE_PORT

addons = [
	MlgmXyysd_Genshin_Impact_Proxy()
]
