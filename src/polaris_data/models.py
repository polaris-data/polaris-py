"""Typed response structures returned by Polaris endpoints."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, TypedDict

JSONDict = dict[str, Any]


class PaginatedResponse(TypedDict):
    data: list[JSONDict]
    next_cursor: str | None
    has_more: bool


class DownloadUrlResponse(TypedDict):
    url: str
    totalBytes: int
    fileCount: int


@dataclass(frozen=True)
class SnapshotEntry:
    """Remote standardized snapshot metadata."""

    key: str
    filename: str


@dataclass(frozen=True)
class LocalSnapshotEntry:
    """Local standardized snapshot metadata."""

    key: str
    path: str
    filename: str
    venue: str | None
    symbol: str | None
    date: str | None
    start: datetime | None
    end: datetime | None

    @property
    def exchange(self) -> str | None:
        """Compatibility alias for earlier SDK releases."""
        return self.venue

    @property
    def asset(self) -> str | None:
        """Compatibility alias for earlier SDK releases."""
        return self.symbol
