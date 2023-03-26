from database import Database
from writeAJson import writeAJson
from ProductAnalyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
db.resetDatabase()

productAnalyzer = ProductAnalyzer(db.collection)

writeAJson(productAnalyzer.totalFromDay(), 'total do dia')
writeAJson(productAnalyzer.MostSoldProduct(), 'Produto mais vendido')
writeAJson(productAnalyzer.MostSpender(), 'Cliente que mais gastou')
writeAJson(productAnalyzer.productsSoldWithMoreThanOne(), 'Produtos vendidos com mais de 1 unidade')