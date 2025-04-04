from dataclasses import dataclass, field
from datetime import datetime

#dataclass automatically creates the methods (e.g. __init__, __repr__) for all these object properties
@dataclass
class Movie:
    _id: str
    title: str
    director: str
    year: int

    #Giving default value to this object property
    rating: int = 0

    #Assigning an empty list as a default value (Using [] can cause conflict between 2 properties having an empty list or '[]' as default value)
    cast: list = field(default_factory=list)
    series: list = field(default_factory=list)
    last_watched: datetime = None
    tags: list = field(default_factory=list)
    description: str = None
    video_link: str = None


@dataclass
class Users:
    _id: str
    email: str
    password: str
    movies: list[str] = field(default_factory=list)
