import os
import logging
from flask import Flask
from flask_cors import CORS
from routes.questions import questions_bp

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-prod')
app.config['DEBUG'] = os.environ.get('DEBUG', 'True') == 'True'
app.config['SERVICE_NAME'] = 'maths-service'
app.config['SERVICE_VERSION'] = '1.0.0'
app.config['PORT'] = int(os.environ.get('PORT', 8082))

app.register_blueprint(questions_bp, url_prefix='/api/maths')


@app.route('/health')
def health():
    return {
        'service': app.config['SERVICE_NAME'],
        'version': app.config['SERVICE_VERSION'],
        'status': 'UP'
    }


if __name__ == '__main__':
    logger.info("Starting Maths Exam Service on port %d", app.config['PORT'])
    app.run(host='0.0.0.0', port=app.config['PORT'], debug=app.config['DEBUG'])
