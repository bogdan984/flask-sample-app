# run.py
from app import app

if __name__ == '__main__':
    # host='0.0.0.0' заставляет Flask слушать все публичные IP адреса ноды
    # port=5000 — стандартный порт, который мы укажем в настройках Flux
    app.run(host='0.0.0.0', port=5000)
