from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Portfolio(Base):
    __tablename__ = 'portfolios'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

class Asset(Base):
    __tablename__ = 'assets'
    id = Column(Integer, primary_key=True)
    portfolio_id = Column(Integer, ForeignKey('portfolios.id'))
    name = Column(String, nullable=False)
    weight = Column(Float, default=0.0)

    portfolio = relationship('Portfolio', back_populates='assets')

engine = create_engine("sqlite:///database.db")
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)