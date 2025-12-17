# src/core/classifier.py

from enum import Enum

class TargetType(str, Enum):
    HASH = "hash"
    IP = "ip"
    DOMAIN = "domain"
    URL = "url"