from quart import Quart, Blueprint, render_template

bp = Blueprint("routes", __name__, static_folder="static/react", static_url_path="/static/react")

@bp.route('/')
async def index():
    return await render_template('react/index.html')

def create_app():
    app = Quart(__name__)
    app.register_blueprint(bp)

    @app.route('/api/v1/hello')
    async def hello():
        return {'message': 'Hello World'}

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=50000)