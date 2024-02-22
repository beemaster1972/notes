from datetime import datetime

import note
from dataclasses import dataclass


@dataclass
class Notes:
    notes: dict[datetime, list[note]]
