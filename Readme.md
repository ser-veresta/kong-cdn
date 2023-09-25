## Requirements
- Docker
- Python > v3.*

## Steps to run the application
```bash
docker network create kong-net
docker run -d --name kong-dbless --network=kong-net \
-v "$(pwd):/kong/declarative/" \
-e "KONG_DATABASE=off" \
-e "KONG_DECLARATIVE_CONFIG=/kong/declarative/kong.yml" \
-e "KONG_PROXY_ACCESS_LOG=/dev/stdout" \
-e "KONG_ADMIN_ACCESS_LOG=/dev/stdout" \
-e "KONG_PROXY_ERROR_LOG=/dev/stderr" \
-e "KONG_ADMIN_ERROR_LOG=/dev/stderr" \
-e "KONG_ADMIN_LISTEN=0.0.0.0:8001" \
-e "KONG_ADMIN_GUI_URL=http://localhost:8002" \
-p 8000:8000 \
-p 8001:8001 \
kong/kong-gateway:3.4.0.0
python api_script.py
```

> Note: Test the application using the url printed in the console by the python scripts.