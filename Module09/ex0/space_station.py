#!/usr/bin/env python3
try:
    from pydantic import BaseModel, Field, ValidationError
    from datetime import datetime
    from typing import Optional, Any
except (ImportError, NameError) as e:
    print("Import error: ", e)
    exit(1)


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(ge=200, default=None)


space_data: dict[str, Any] = {
    "station_id": "ISS001",
    "name": "International Space Sation",
    "crew_size": 6,
    "power_level": 85.5,
    "oxygen_level": 92.3,
    "last_maintenance": datetime.now(),
    "is_operational": True
}

space_data_2: dict[str, Any] = {
    "station_id": "ISS002",
    "name": "International Space Sation",
    "crew_size": 21,
    "power_level": 55.5,
    "oxygen_level": 62.3,
    "last_maintenance": datetime.now(),
    "is_operational": False
}


def main() -> None:
    print("Space Station Data Validation")
    try:
        space_info = SpaceStation(**space_data)
        print("=====================================")
        print(f"Valid station created: {space_info.last_maintenance}")
        print(f"ID: {space_info.station_id}")
        print(f"Name: {space_info.name}")
        print(f"Crew: {space_info.crew_size} people")
        print(f"Power: {space_info.power_level}%")
        print(f"Oxygen: {space_info.oxygen_level}%")
        print(f"Status: {space_info.is_operational}")
        print("=====================================")
    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(err["msg"])

    try:
        space_info_2 = SpaceStation(**space_data_2)
        print("=====================================")
        print(f"Valid station created: {space_info_2.last_maintenance}")
        print(f"ID: {space_info_2.station_id}")
        print(f"Name: {space_info_2.name}")
        print(f"Crew: {space_info_2.crew_size} people")
        print(f"Power: {space_info_2.power_level}%")
        print(f"Oxygen: {space_info_2.oxygen_level}%")
        print(f"Status: {space_info_2.is_operational}")
        print("=====================================")
    except ValidationError as e:
        print("Expected validation error:")
        for err in e.errors():
            print(err["msg"])


if __name__ == "__main__":
    main()
