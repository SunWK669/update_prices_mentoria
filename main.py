import requests
import json
from daofirebase import Dao

SEARCH_TERM = "iphone 12 128GB"

def main():
    url = "https://api-v1.zoom.com.br/restql/run-query/sherlock/serp_items/1?tenant=DEFAULT"
    headers = {"Content-Type": "application/json", "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    payload = {
	"query": SEARCH_TERM
}
    response = requests.post(url, json=payload, headers=headers)
    content = json.loads(response.content)
    products = []
    for product in content["serp"]["result"]["hits"]:
        product_infos = {"name": product["name"], "price": product["price"], "uri": product["url"]}
        products.append(product_infos)
    product = encontra_produto_valor_medio(products)
    dao = Dao()
    print(dao.put(json.dumps(product)))
    print(dao.get())

def encontra_produto_valor_medio(products):
    soma = 0
    for product in products:
        soma += product["price"]
    media = soma/len(products)
    diferenca = products[0]["price"] - media
    if diferenca < 0:
        diferenca = diferenca*-1
    the_one = products[0]
    for product in products:
        dif = product["price"] - media
        if dif < 0:
            dif = dif*-1
        if dif < diferenca:
            the_one = product
            diferenca = dif
    return the_one
# dao = Dao()
# dao.delete("-Msg7AU3zn7fIBiVH7Co")
# print(dao.get())
main()