# -*- coding: utf-8 -*-
"""Optional configuration for the standalone web site.

The site can start without Discord credentials. Add them later when connecting
this site to the bot's OAuth flow.
"""
import os


def _int_list(name: str) -> list[int]:
    raw = os.getenv(name, "").strip()
    if not raw:
        return []
    try:
        return [int(item.strip()) for item in raw.split(",") if item.strip()]
    except ValueError as exc:
        raise RuntimeError(f"{name}은(는) 숫자 ID를 쉼표로 구분해야 합니다.") from exc


봇_토큰 = os.getenv("DISCORD_BOT_TOKEN", "").strip()
관리자아이디 = _int_list("DISCORD_ADMIN_IDS")
API_엔드포인트 = os.getenv("DISCORD_API_ENDPOINT", "https://discord.com/api/v10").strip()
클라이언트_아이디 = os.getenv("DISCORD_CLIENT_ID", "").strip()
클라이언트_시크릿 = os.getenv("DISCORD_CLIENT_SECRET", "").strip()
도메인 = os.getenv("PUBLIC_BASE_URL", "").strip().rstrip("/")
복구로그웹훅 = [
    item.strip() for item in os.getenv("RECOVERY_LOG_WEBHOOKS", "").split(",") if item.strip()
]

token = 봇_토큰
admin_id = 관리자아이디
api_endpoint = API_엔드포인트
client_id = 클라이언트_아이디
client_secret = 클라이언트_시크릿
base_url = 도메인
bokweb = 복구로그웹훅
