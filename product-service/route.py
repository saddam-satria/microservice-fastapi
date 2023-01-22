from routes.product import productRoute
from routes.category import categoryRoute

def routing(app):
    app.include_router(productRoute)
    app.include_router(categoryRoute)
