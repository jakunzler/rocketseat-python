from datetime import datetime, timedelta
from sqlalchemy import or_, update
from sqlalchemy.orm.exc import NoResultFound
from src.models.entities.payment import Payment
from src.models.interfaces.payment_repository import PaymentRepositoryInterface
from src.errors.types.http_bad_request import HttpBadRequestError

class PaymentRepository(PaymentRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def create_payment_pix(self, value: float) -> Payment:
        with self.__db_connection as database:
            try:
                expiration_date = datetime.now() + timedelta(minutes=30)
                new_payment = Payment(
                    value=value,
                    expiration_date=expiration_date,
                )
                database.session.add(new_payment)
                database.session.commit()
                return new_payment
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_payment_by_id(self, payment_id: int) -> Payment:
        with self.__db_connection as database:
            try:
                return database.session.query(Payment).filter(Payment.id == payment_id).one()
            except NoResultFound:
                raise HttpBadRequestError("Payment not found")

    def get_payment_by_bank_payment_id(self, bank_payment_id: str) -> Payment:
        with self.__db_connection as database:
            try:
                return database.session.query(Payment).filter(Payment.bank_payment_id == bank_payment_id).one()
            except NoResultFound:
                raise HttpBadRequestError("Payment not found")

    def get_all_payments(self, page: int, page_length: int) -> list[Payment]:
        with self.__db_connection as database:
            try:
                return database.session.query(Payment).limit(page_length).offset(page * page_length).all()
            except Exception as exception:
                raise exception

    def update_payment(self, partial_payment: Payment) -> Payment:
        with self.__db_connection as database:
            try:
                partial_payment.updated_at = datetime.now()
                
                
                database.session.execute(
                    update(Payment),
                    [
                      partial_payment
                    ]
                )
                database.session.commit()
                return (
                        database.session.query(Payment)
                    .filter(Payment.id == partial_payment.id)
                    .one()
                )
            except Exception as exception:
                database.session.rollback()
                raise exception

    def delete_payment(self, payment_id: int) -> bool:
        with self.__db_connection as database:
            try:
                database.session.query(Payment).filter(Payment.id == payment_id).delete()
                database.session.commit()
                return True
            except Exception as exception:
                database.session.rollback()
                raise exception
