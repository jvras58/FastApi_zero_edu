# from fastapi.testclient import TestClient

# from fast_zero.app import app


# def test_root_deve_retornar_200_e_ola_mundo():
#     client = TestClient(app) # Organiza o ambiente para o teste

#     response = client.get('/') # Ação principal que consiste em chamar o sistema sob teste no caso a rota / e a acão sobre a linha de response inteira

#     assert response.status_code == 200 # Afirmar (Verifica se tudo ocorreu como esperado sempre tem a linha assert [ela é booleana ])
#     assert response.json() == {'message': 'Olá Mundo!'} # Afirmar 
