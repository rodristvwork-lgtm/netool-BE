from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class Ping:
    
    byte: int = 0
    server: str = ""
    timestamp: str = ""
    time_history: List[Tuple] = field(default_factory=list)
    packets_transmitted: int = 0
    packets_received: int = 0
    total_time: int = 0
    packet_loss_perc: str = ""
    rrt_min: float = 0
    rrt_avg: float = 0
    rtt_max: float = 0
    rtt_mdev: float = 0