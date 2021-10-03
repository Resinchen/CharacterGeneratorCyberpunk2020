from enum import Enum

from src.utils import roll_to_type

EventType = Enum("EventType", "FACT FRIENDS ROMANTIC NOTHING")
RollToEvent = roll_to_type(
    {
        EventType.FACT: [1, 2, 3],
        EventType.FRIENDS: [4, 5, 6],
        EventType.ROMANTIC: [7, 8],
        EventType.NOTHING: [9, 10],
    }
)


class Event:
    def __init__(self, event_type: EventType = EventType.NOTHING):
        self.type: EventType = event_type
        self.payload: str = None

    def __str__(self) -> str:
        return f"type: {self.type}\n\t{self.payload}"
