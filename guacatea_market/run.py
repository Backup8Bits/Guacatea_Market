from market import app

# Checa si el run.py ha sido ejecutado directamente y no importado
if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)