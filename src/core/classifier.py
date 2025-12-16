# src/core/classifier.py

import re
import ipaddress
from enum import Enum

class TargetType(str, Enum):
    HASH = "hash"
    IP = "ip"
    DOMAIN = "domain"
    URL = "url"
    TARGET = "target"
    UNKNOWN = "unknown"


def is_valid_ip(value: str) -> bool:
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False

class TargetClassifier:
    HASH_RE = re.compile(
        r"^(?:"
        r"[a-fA-F0-9]{32}|"   # MD5
        r"[a-fA-F0-9]{40}|"   # SHA1
        r"[a-fA-F0-9]{64}|"   # SHA256
        r"[a-fA-F0-9]{96}|"   # SHA384
        r"[a-fA-F0-9]{128}"   # SHA512
        r")$"
    )


    def classify(self, value: str) -> TargetType:
        value = value.strip()

        if not value:
            return TargetType.UNKNOWN

        if value.startswith("http://") or value.startswith("https://"):
            return TargetType.URL

        if is_valid_ip(value):
            return TargetType.IP

        if self.HASH_RE.match(value):
            return TargetType.HASH

        # domain için basit ama yeterli kontrol
        if "." in value and " " not in value:
            return TargetType.DOMAIN

        return TargetType.UNKNOWN

