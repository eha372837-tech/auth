# -*- coding: utf-8 -*-
"""Configuration loaded from values assigned in start.py."""
import os


def _required(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value or value.startswith("여기에_"):
        raise RuntimeError(f"start.py에 필수 값을 입력하세요: {name}")
    return value


def _int_list(name: str) -> list[int]:
    raw = _required(name)
    try:
        return [int(item.strip()) for item in raw.split(",") if item.strip()]
    except ValueError as exc:
        raise RuntimeError(f"{name}은(는) 숫자 ID를 쉼표로 구분해야 합니다.") from exc


봇_토큰 = _required("DISCORD_BOT_TOKEN")
관리자아이디 = _int_list("DISCORD_ADMIN_IDS")
API_엔드포인트 = os.getenv("DISCORD_API_ENDPOINT", "https://discord.com/api/v10").strip()
클라이언트_아이디 = os.getenv("DISCORD_CLIENT_ID", "").strip()
클라이언트_시크릿 = os.getenv("DISCORD_CLIENT_SECRET", "").strip()
도메인 = os.getenv("PUBLIC_BASE_URL", "").strip().rstrip("/")
try:
    복구로그웹훅 = [
        int(item.strip()) for item in os.getenv("RECOVERY_LOG_WEBHOOKS", "").split(",") if item.strip()
    ]
except ValueError as exc:
    raise RuntimeError("RECOVERY_LOG_WEBHOOKS는 Discord 채널 ID를 쉼표로 구분해야 합니다.") from exc

token = 봇_토큰
admin_id = 관리자아이디
api_endpoint = API_엔드포인트
client_id = 클라이언트_아이디
client_secret = 클라이언트_시크릿
base_url = 도메인
bokweb = 복구로그웹훅
