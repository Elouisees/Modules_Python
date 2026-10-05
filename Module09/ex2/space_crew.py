#!/usr/bin/env python3
try:
    from pydantic import BaseModel, Field, model_validator
    from datetime import datetime
    from enum import Enum
    from typing import Any
except (ImportError, NameError) as e:
    print("Mssing imports: ", e)
    exit(1)


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def id_check(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise Exception("Mission ID must start with 'M'.")
        return self

    @model_validator(mode='after')
    def crew_check(self) -> "SpaceMission":
        sign: int = 0
        for member in self.crew:
            if member.rank == Rank.CAPTAIN or\
               member.rank == Rank.COMMANDER:
                sign = 1
            if not member.is_active:
                raise Exception("All crew members must be active.")
        if sign == 0:
            raise Exception("Crew must have at least one Commander or "
                            "Captain.")
        return self

    @model_validator(mode='after')
    def duration_check(self) -> "SpaceMission":
        crew_size: int = int(len(self.crew) / 2)
        check: int = 0
        if self.duration_days > 365:
            for member in self.crew:
                if member.years_experience > 5:
                    check += 1
            if not check >= crew_size:
                raise Exception("Long missions need 50% experienced crew.")
        return self


mission_data: dict[str, Any] = {
    "mission_id": "M2024_MARS",
    "mission_name": "Mars Colony Establishment",
    "destination": "Mars",
    "launch_date": datetime.now(),
    "duration_days": 900,
    "crew": [
        {
            "member_id": "M2024_SC",
            "name": "Sarah Connor",
            "rank": Rank.COMMANDER,
            "age": 46,
            "specialization": "Mission Command",
            "years_experience": 15,
            "is_active": True
        },
        {
            "member_id": "M2024_JS",
            "name": "John Smith",
            "rank": Rank.LIEUTENANT,
            "age": 38,
            "specialization": "Navigation",
            "years_experience": 11,
            "is_active": True
        },
        {
            "member_id": "M2024_AJ",
            "name": "Alice Johnson",
            "rank": Rank.OFFICER,
            "age": 32,
            "specialization": "Engineering",
            "years_experience": 9,
            "is_active": True
        }
    ],
    "budget_millions":  2500.0
}

mission_data_2: dict[str, Any] = {
    "mission_id": "M2024_MARS",
    "mission_name": "Mars Colony Establishment",
    "destination": "Mars",
    "launch_date": datetime.now(),
    "duration_days": 900,
    "crew": [
        {
            "member_id": "M2024_SC",
            "name": "Sarah Connor",
            "rank": Rank.CADET,
            "age": 46,
            "specialization": "Mission Command",
            "years_experience": 15,
            "is_active": True
        },
        {
            "member_id": "M2024_JS",
            "name": "John Smith",
            "rank": Rank.LIEUTENANT,
            "age": 38,
            "specialization": "Navigation",
            "years_experience": 11,
            "is_active": True
        },
        {
            "member_id": "M2024_AJ",
            "name": "Alice Johnson",
            "rank": Rank.OFFICER,
            "age": 32,
            "specialization": "Engineering",
            "years_experience": 9,
            "is_active": True
        }
    ],
    "budget_millions":  2500.0
}


def main() -> None:
    print("Space Mission Crew Validation")
    try:
        mission_info = SpaceMission(**mission_data)
        print("===============================")
        print("Valid mission created:")
        print(f"Mission: {mission_info.mission_name}")
        print(f"ID: {mission_info.mission_id}")
        print(f"Destination: {mission_info.destination}")
        print(f"Duration: {mission_info.duration_days}")
        print(f"Budget: ${mission_info.budget_millions}M")
        print(f"Crew size: {len(mission_info.crew)}")
        print("Crew members:")
        for member in mission_info.crew:
            print(f"- {member.name} ({member.rank.value}) - "
                  f"{member.specialization}")
        print("===============================")
    except Exception as e:
        print("Expected validation error:")
        print(e)

    try:
        mission_info_2 = SpaceMission(**mission_data_2)
        print("===============================")
        print("Valid mission created:")
        print(f"Mission: {mission_info_2.mission_name}")
        print(f"ID: {mission_info_2.mission_id}")
        print(f"Destination: {mission_info_2.destination}")
        print(f"Duration: {mission_info_2.duration_days}")
        print(f"Budget: ${mission_info_2.budget_millions}M")
        print(f"Crew size: {len(mission_info_2.crew)}")
        print("Crew members:")
        for member in mission_info_2.crew:
            print(f"- {member.name} ({member.rank.value}) - "
                  f"{member.specialization}")
        print("===============================")
    except Exception as e:
        print("Expected validation error:")
        print(e)


if __name__ == "__main__":
    main()
