from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sql.db'
db = SQLAlchemy(app)
api = Api(app)

# Tables in Models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# API Endpoints
class ProductListResource(Resource):
    def get(self):
        products = Product.query.all()
        return jsonify([{
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'image_url': product.image_url
        } for product in products])

class ProductResource(Resource):
    def get(self, product_id):
        product = Product.query.get_or_404(product_id)
        return jsonify({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'image_url': product.image_url
        })

class CartResource(Resource):
    def post(self):
        data = request.get_json()
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        if not product_id or not quantity:
            return {'message': 'Invalid request'}, 400

        cart_item = CartItem(product_id=product_id, quantity=quantity)
        db.session.add(cart_item)
        db.session.commit()

        return {'message': 'Product added to cart successfully'}, 201

    def get(self):
        cart_items = CartItem.query.all()
        return jsonify([{
            'id': cart_item.id,
            'product_id': cart_item.product_id,
            'quantity': cart_item.quantity
        } for cart_item in cart_items])

class CartItemResource(Resource):
    def delete(self, cart_id):
        cart_item = CartItem.query.get_or_404(cart_id)
        db.session.delete(cart_item)
        db.session.commit()
        return {'message': 'Item removed from cart successfully'}

# Add API resources
api.add_resource(ProductListResource, '/products')
api.add_resource(ProductResource, '/products/<int:product_id>')
api.add_resource(CartResource, '/cart')
api.add_resource(CartItemResource, '/cart/<int:cart_id>')

# Database Integration
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
