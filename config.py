# Render web settings. Keep secrets out of public GitHub repositories.
import os
DATABASE_URL = ""  # 웹 전용 DB가 필요하면 여기에 입력; 인증 공유 데이터는 봇 API가 담당합니다.
DISCORD_BOT_TOKEN = ""
DISCORD_ADMIN_IDS = ""
DISCORD_CLIENT_ID = "여기에_Application_ID_입력"
DISCORD_CLIENT_SECRET = "여기에_Client_Secret_입력"
PUBLIC_BASE_URL = "https://auth-8qmu.onrender.com"
RECOVERY_LOG_WEBHOOKS = ""
DISCORD_API_ENDPOINT = "https://discord.com/api/v10"
BOT_API_BASE_URL = "https://여기에-봇-api-공개-HTTPS-주소"
BOT_API_KEY = "여기에_봇과_웹이_공유할_긴_API_키"

def _value(env, direct): return os.getenv(env, "").strip() or direct.strip()
def _ids(value): return [int(x.strip()) for x in value.split(",") if x.strip()]
봇_토큰=_value("DISCORD_BOT_TOKEN", DISCORD_BOT_TOKEN)
관리자아이디=_ids(_value("DISCORD_ADMIN_IDS", DISCORD_ADMIN_IDS))
API_엔드포인트=_value("DISCORD_API_ENDPOINT", DISCORD_API_ENDPOINT)
클라이언트_아이디=_value("DISCORD_CLIENT_ID", DISCORD_CLIENT_ID)
클라이언트_시크릿=_value("DISCORD_CLIENT_SECRET", DISCORD_CLIENT_SECRET)
도메인=_value("PUBLIC_BASE_URL", PUBLIC_BASE_URL).rstrip("/")
복구로그웹훅=[x.strip() for x in _value("RECOVERY_LOG_WEBHOOKS", RECOVERY_LOG_WEBHOOKS).split(",") if x.strip()]
token=봇_토큰; admin_id=관리자아이디; api_endpoint=API_엔드포인트; client_id=클라이언트_아이디; client_secret=클라이언트_시크릿; base_url=도메인; bokweb=복구로그웹훅
