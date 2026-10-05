#!/usr/bin/env python3
try:
    from pydantic import BaseModel, Field, model_validator
    from typing import Optional, Any
    from datetime import datetime
    from enum import Enum
except (ImportError, NameError) as e:
    print(e)
    exit(1)


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500, default=None)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def id_check(self) -> "AlienContact":

        if not self.contact_id.startswith("AC"):
            raise Exception("Contact ID must start with 'AC'.")
        return self

    @model_validator(mode='after')
    def contact_check(self) -> "AlienContact":
        if self.contact_type == ContactType.PHYSICAL:
            if not self.is_verified:
                raise Exception("Physical contact must be verified(True).")
        if self.contact_type == ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise Exception("Telepathic contact requires at least 3 "
                                "witnesses.")
        return self

    @model_validator(mode='after')
    def signal_check(self) -> "AlienContact":
        if self.signal_strength > 7.0:
            if self.message_received is None:
                raise Exception("Strong signals should include received "
                                "messages.")
        return self


alien_data: dict[str, Any] = {
    "contact_id": "AC_2024_001",
    "timestamp": datetime.now(),
    "location": "Area 51, Nevada",
    "contact_type": ContactType.RADIO,
    "signal_strength": 8.5,
    "duration_minutes": 45,
    "witness_count": 5,
    "message_received": "Greetings from Zeta Reticuli",
    "is_verified": True
}

alien_data_2: dict[str, Any] = {
    "contact_id": "AC_2024_001",
    "timestamp": datetime.now(),
    "location": "Area 51, Nevada",
    "contact_type": ContactType.TELEPATHIC,
    "signal_strength": 8.5,
    "duration_minutes": 45,
    "witness_count": 2,
    "message_received": "Greetings from Zeta Reticuli",
    "is_verified": True
}


def main() -> None:
    print("Alien Contact Log Validation")

    try:
        alien_info = AlienContact(**alien_data)
        print("=====================================")
        print("Valid contact report:")
        print(f"ID: {alien_info.contact_id}")
        print(f"Type: {alien_info.contact_type.name}")
        print(f"Location: {alien_info.location}")
        print(f"Signal: {alien_info.signal_strength}/10")
        print(f"Duration {alien_info.duration_minutes} minutes")
        print(f"Witnesses: {alien_info.witness_count}")
        print(f"Message: {alien_info.message_received}")
        print("=====================================")
    except Exception as e:
        print("Expected validation error:")
        print(e)

    try:
        alien_info_2 = AlienContact(**alien_data_2)
        print("=====================================")
        print("Valid contact report:")
        print(f"ID: {alien_info_2.contact_id}")
        print(f"Type: {alien_info_2.contact_type.name}")
        print(f"Location: {alien_info_2.location}")
        print(f"Signal: {alien_info_2.signal_strength}/10")
        print(f"Duration {alien_info_2.duration_minutes} minutes")
        print(f"Witnesses: {alien_info_2.witness_count}")
        print(f"Message: {alien_info_2.message_received}")
        print("=====================================")
    except Exception as e:
        print("Expected validation error:")
        print(e)


if __name__ == "__main__":
    main()

# pip install pydantic pydantic-settings

# Notes:
# Pydantic's ValidationError cannot be raised manually.
# It is only meant to be created internally by Pydantic's
# internal structure. The error rewuires a very specific internal
# structure
