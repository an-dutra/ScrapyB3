WebScrap que recupera dados da B3 e de outras fontes via Python para gerar um hist�rico em um banco de dados PostGres. A inten��o � recuperar informa��es para an�lises fundamentalistas (como balan�os, not�cias, etc), como tamb�m para an�lise t�cnica (hist�rico de cota��es). Futuramente tamb�m salvar informa��es j� calculadas como as de indicadores.

#Criar banco de dados

docker run --name db-b3data -p 0.0.0.0:5435:5432 -v ~/b3scrapy/db:/usr/data --workdir /usr/data/ -e POSTGRES_PASSWORD=$DBPass -d postgres:12-alpine

#Criar M�quina de execucao
docker run -it --name empresas -v ~/b3scrapy/:/usr/src/b3scrapy --workdir /usr/src/b3scrapy --link db-b3data:db-b3data andisu/empresas 

O c�digo est� inicialmente um pouco bagun�ado, pois eu estava s� fazendo uns programinhas pra uso di�rio meus, mas resolvi abrir o c�digo e quem sabe conseguimos algo melhor juntos.
