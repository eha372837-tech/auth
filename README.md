# WSV OAuth 인증 사이트(Render용)

이 폴더는 **Discord 봇 없이도 먼저 띄울 수 있는 독립형 웹사이트**입니다. 기본 홈페이지와 상태 확인 페이지가 바로 표시되며, 나중에 Discord OAuth 환경변수를 추가해 인증 기능을 연결할 수 있습니다.

## GitHub 업로드

ZIP 압축을 풀었을 때 생긴 이 폴더 안의 파일을 GitHub 저장소 최상위에 올립니다. GitHub에 `render_auth_site` 폴더 자체를 한 겹 더 넣지 말고, 아래 구조가 저장소 최상위가 되게 하세요.

```text
web.py
config.py
w.py
db.py
requirements.txt
render.yaml
.gitignore
templates/error.html
templates/success.html
templates/Wave.js
```

## Render 생성

1. Render Dashboard → **New → Web Service**
2. GitHub 저장소 선택
3. 설정:

```text
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn web:app --bind 0.0.0.0:$PORT
Plan: Free
```

`render.yaml`을 사용하는 Blueprint 배포라면 해당 값이 자동으로 채워집니다.

## Render 환경변수 (사이트만 먼저 띄울 때는 생략 가능)

사이트 화면만 확인할 때는 환경변수를 입력하지 않아도 됩니다. Discord OAuth를 연결할 때만 Render 서비스의 Environment에 아래 값을 입력합니다.

```text
DATABASE_URL=Supabase_Connection_String
DISCORD_BOT_TOKEN=새로_발급한_봇_토큰
DISCORD_ADMIN_IDS=관리자_디스코드_ID
DISCORD_CLIENT_ID=Discord_OAuth2_Client_ID
DISCORD_CLIENT_SECRET=Discord_OAuth2_Client_Secret
PUBLIC_BASE_URL=https://auth.wsv.kr
RECOVERY_LOG_WEBHOOKS=
DISCORD_API_ENDPOINT=https://discord.com/api/v10
```

`DISCORD_ADMIN_IDS`가 여러 개면 쉼표로 구분합니다.

## 도메인 연결

Render 배포 후 Service → Settings → Custom Domains에서 다음을 추가합니다.

```text
auth.wsv.kr
```

Render가 표시하는 CNAME 값을 가비아 DNS에 입력합니다. 기존에 같은 `auth` 호스트에 설정한 A 레코드가 있다면 삭제하고 Render가 안내하는 CNAME으로 교체합니다.

최종 주소:

```text
https://auth.wsv.kr
```

## Discord OAuth2 설정

Discord Developer Portal → OAuth2 → Redirects에 아래 주소를 정확히 추가합니다.

```text
https://auth.wsv.kr/callback
```

또한 Pterodactyl에서 실행하는 봇의 설정에도 동일하게 입력해야 합니다.

```text
PUBLIC_BASE_URL=https://auth.wsv.kr
```

## 기본 확인 주소

배포 후 `/`에서 기본 홈페이지가 보이고, 아래 주소가 `{"status":"ok"}`를 반환하면 웹 서버가 실행 중입니다.

```text
https://auth.wsv.kr/health
```

`/callback`을 OAuth 코드 없이 직접 열었을 때 인증 오류 페이지가 보이는 것은 정상입니다.

## 중요: 현재 DB 구조

이 버전은 Supabase PostgreSQL을 사용합니다. Render와 Pterodactyl 양쪽의 `DATABASE_URL`에 같은 Supabase 연결 문자열을 입력하면 라이센스·역할·인증 사용자가 공유됩니다.

토큰과 Client Secret은 GitHub 파일에 절대 입력하지 말고 Render Environment에만 입력하세요.
