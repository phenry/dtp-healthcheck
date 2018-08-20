import os
from app import app

#app.config['DEBUG'] = os.environ.get('DEBUG', False)
#app.config['DEBUG'] = True

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=int(os.environ.get('PORT', 5000)))
