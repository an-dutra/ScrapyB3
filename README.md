WebScrap que recupera dados da B3 e de outras fontes via Python para gerar um histórico em um banco de dados PostGres. A intenção é recuperar informações para análises fundamentalistas (como balanços, notícias, etc), como também para análise técnica (histórico de cotações). Futuramente também salvar informações já calculadas como as de indicadores.

#Criar banco de dados

docker run --name db-b3data -p 0.0.0.0:5435:5432 -v ~/b3scrapy/db:/usr/data --workdir /usr/data/ -e POSTGRES_PASSWORD=$DBPass -d postgres:12-alpine

#Criar Máquina de execucao
docker run -it --name empresas -v ~/b3scrapy/:/usr/src/b3scrapy --workdir /usr/src/b3scrapy --link db-b3data:db-b3data andisu/empresas 

O código está inicialmente um pouco bagunçado, pois eu estava só fazendo uns programinhas pra uso diário meus, mas resolvi abrir o código e quem sabe conseguimos algo melhor juntos.
