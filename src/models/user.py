from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.database.sqlalchemy import Base, get_session


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    username: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    experience: Mapped[int] = mapped_column(Integer, default=0)
    level: Mapped[int] = mapped_column(Integer, default=1)
    is_blacklisted: Mapped[bool] = mapped_column(Boolean, default=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)


class UserModel:
    @staticmethod
    async def get(user_id: str):
        async with await get_session() as session:
            return await session.get(User, user_id)

    @staticmethod
    async def create_or_update(user_id: str, data: dict):
        async with await get_session() as session:
            user = await session.get(User, user_id)
            if user:
                for key, value in data.items():
                    setattr(user, key, value)
            else:
                user = User(id=user_id, **data)
                session.add(user)
            await session.commit()
            return user
