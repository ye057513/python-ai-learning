from dataclasses import dataclass,asdict
from datetime import datetime

@dataclass
class Transaction:
    note: str
    amount: float
    category: str
    t_type: str
    date: str = None

    def __post_init__(self):
        if self.date is None:
            self.date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def to_dict(self):
        return asdict(self)