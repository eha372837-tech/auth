import requests
import config as settings

def _headers():
    return {"X-Bot-API-Key": settings.BOT_API_KEY}

def guild(guild_id):
    r = requests.get(f"{settings.BOT_API_BASE_URL.rstrip('/')}/internal/guild/{int(guild_id)}", headers=_headers(), timeout=15)
    return r.json() if r.ok else None

def complete(guild_id, user_id, refresh_token):
    r = requests.post(f"{settings.BOT_API_BASE_URL.rstrip('/')}/internal/auth/complete", headers=_headers(), json={"guild_id": int(guild_id), "user_id": str(user_id), "refresh_token": refresh_token}, timeout=15)
    return r.json() if r.ok else None
