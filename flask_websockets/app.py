from flask import Flask, jsonify, request
from repository.database import db
from db_models.payment import Payment
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'
db.init_app(app)

@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    data = request.get_json()
    
    # validações
    if 'value' not in data:
        return jsonify({'message': 'Value is required!'}), 400
      
    expiration_date = datetime.now() + timedelta(minutes=30)
    
    new_payment = Payment(value=data['value'], expiration_date=expiration_date)
    db.session.add(new_payment)
    db.session.commit()
    
    return jsonify({'message': 'Payment created successfully!',
                    "payment": new_payment.to_dict()})
      
@app.route('/payments/pix/confirmation', methods=['POST'])
def confirm_payment_pix():
    data = request.get_json()
    payment_id = data.get('payment_id')
    payment_status = data.get('payment_status')
    
    payment = Payment.query.get_or_404(payment_id)
    payment.payment_status = payment_status
    
    db.session.commit()
    return jsonify({'message': 'Payment confirmed successfully!'})
  
@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    return 'pagamento pix'
  
if __name__ == '__main__':
    app.run(debug=True)