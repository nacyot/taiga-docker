import os
from .common import *
from .dockerenv import *

INSTALLED_APPS += ["taiga_contrib_slack"]
INSTALLED_APPS += ["taiga_contrib_ldap_auth"]
LDAP_SERVER = os.getenv("LDAP_SERVER")
LDAP_DN_FORMAT = os.getenv("LDAP_DN_FORMAT")
LDAP_BASE_EMAIL = os.getenv("LDAP_BASE_EMAIL")

# THROTTLING
#REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {
#    "anon": "20/min",
#    "user": "200/min",
#    "import-mode": "20/sec"
#}
