from sqlalchemy import Column, Integer, String, false
from .database import Base


class Betriebsstelle(Base):
    __tablename__ = "betriebsstelle"

    id = Column(Integer, primary_key=True, index=True)
    plc = Column(String)
    rl100_code = Column(String, unique=True, index=True)
    rl100_name = Column(String)
    rl100_name_short = Column(String)
    type_short = Column(String)
    type = Column(String)
    operating_status = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    branch = Column(String)
    regional_area = Column(String)
    last_modified = Column(String)
