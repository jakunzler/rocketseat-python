from src.models.sqlite.repository.interfaces.products_repository import ProductsRepositoryInterface
from src.models.redis.repository.interfaces.redis_repository import RedisRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse


class ProductFinder:
    def __init__(
            self,
            redis_repo: RedisRepositoryInterface,
            products_repo: ProductsRepositoryInterface
        ) -> None:
        self.__redis_repo = redis_repo
        self.__products_repo = products_repo

    def find_by_name(self, http_request: HttpRequest) -> HttpResponse:
        product_name = http_request.params["product_name"]
        product = None

        product = self.__find_in_cache(product_name)
        if not product:
            product = self.__find_in_sql(product_name)
            self.__insert_in_cache(product)

        return self.__format_response(product)

    def __find_in_cache(self, product_name: str) -> tuple:
        product_infos = self.__redis_repo.get_key(product_name)
        if product_infos:
            product_infos_list = product_infos.split(",") # price,quantity -> [price, quantity]
            return (0, product_name, product_infos_list[0], product_infos_list[1])

        return None

    def __find_in_sql(self, product_name: str) -> tuple:
        product = self.__products_repo.find_product_by_name(product_name)
        if not product:
            raise Exception("Produto nao encontrado!")

        return product

    def __insert_in_cache(self, product: tuple) -> None:
        product_name = product[1]
        value = f"{product[2]},{product[3]}" # 1999.99,10
        self.__redis_repo.insert_ex(product_name, value, ex=60)

    def __format_response(self, product: tuple) -> HttpResponse:
        return HttpResponse(
            status_code=200,
            body={
                "type": "PRODUCT",
                "count": 1,
                "attributes": {
                    "name": product[1],
                    "price": product[2],
                    "quantity": product[3]
                }
            }
        )
