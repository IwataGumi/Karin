from sqlalchemy.sql import func
from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp


class TimestampMixin:
    created_at = Column(
        Timestamp,
        server_default=text("current_timestamp"),
        nullable=False,
        comment="作成日時",
    )
    updated_at = Column(
        Timestamp,
        server_default=func.now(),
        server_onupdate=func.now(),
        nullable=False,
        comment="更新日時",
    )
