import streamlit as st
import requests
import json


def home_page():
    st.title("Sistema de gerenciamento de bicicletas")

    st.write("Este é um sistema que gerencia o empréstimo de bicicletas. Nele é possível manipular dados relacionados aos usuários. bicicletas e aos empréstimos em si.")




def get_users():
    st.title('Usuários')

    r = requests.get('String de conexão get users')
    status_code = r.status_code


    if status_code == 200:
        resposta_json = r.json()
        usuarios = resposta_json
        st.table(usuarios)













def post_user():
    st.title('Cadastrar usuário')

    nome = st.text_input('Nome')
    cpf = st.text_input('CPF')
    data_nascimento = st.text_input('Data de Nascimento')
    


    if st.button('Cadastrar'):

        if nome == '' or cpf == '' or data_nascimento == '':
            st.error('Preencha todos os campos!')

        elif nome != '' and cpf != '' and data_nascimento != '' :
            url = ("String de conexão post user")
            try:
                retorno = requests.post(url, json={"nome": nome, "CPF": cpf, "data": data_nascimento})

                if retorno.status_code == 201 or retorno.status_code == 200:
                    st.success('Usuário cadastrado com sucesso!')

                else:
                    st.error("Usuário não cadastrado!")

            except Exception as e:
                st.error("Erro ao cadastrar usuário!")










def data_user():
    st.title('Dados do usuário')
    
    if 'usuario' not in st.session_state:
        st.session_state['usuario'] = None
    
    usuario_id = st.text_input('ID do usuário', key='usuario_id')

    
    if st.button('Buscar'):
        if usuario_id:
            try:
                r = requests.get(f'string de conexão get one user')
                if r.status_code == 200:
                    st.session_state['usuario'] = r.json()

                else:
                    st.error('Usuário não encontrado.')
                    st.session_state['usuario'] = None
            except Exception as e:
                st.error(f'Erro ao buscar usuário: {e}')
                st.session_state['usuario'] = None

    if st.session_state['usuario']:
        with st.form("form_atualizar_usuario"):
       
            novo_nome = st.text_input('Nome', value=st.session_state['usuario'].get('nome', ''))
            novo_cpf = st.text_input('CPF', value=st.session_state['usuario'].get('CPF', ''))
            nova_data = st.text_input('CPF', value=st.session_state['usuario'].get('data', ''))

            atualizar_button = st.form_submit_button('Atualizar Usuário')
            
            if atualizar_button:
                try:
                    update_response = requests.put(f'String de conexão put user', json={
                        "nome": novo_nome, 
                        "CPF": novo_cpf, 
                        "data": nova_data
                    })



                    if update_response.status_code in [200, 204]:
                        st.success('Usuário atualizado com sucesso!')
        
                        st.session_state['usuario']['nome'] = novo_nome
                        st.session_state['usuario']['cpf'] = novo_cpf
                        st.session_state['usuario']['data'] = nova_data
                    else:
                        st.error('Falha ao atualizar usuário.')
                except Exception as e:
                    st.error(f'Erro ao atualizar usuário: {e}')



        if st.button('Remover Usuário'):
            try:
                
                delete_response = requests.delete(f'String de conexão delete user')

                if delete_response.status_code in [200, 204]:
                    st.success('Usuário removido com sucesso!')
                    st.session_state['usuario'] = None
                
                else:
                    st.error('Falha ao remover usuário.')

            except Exception as e:
                st.error(f'Erro ao remover usuário: {e}')









def get_bikes():
    st.title('Bicicletas')

    r = requests.get('String de conexão get bikes')
    status_code = r.status_code

    if status_code == 200:
        resposta_json = r.json()
        bicicletas = resposta_json
        st.table(bicicletas)










def post_bike():
    st.title('Cadastrar bicicleta')

    marca = st.text_input('Marca')
    modelo = st.text_input('Modelo')
    cidade = st.text_input('Cidade')
    status = st.selectbox('Status', ['disponivel', 'alugada'])


    if st.button('Cadastrar'):

        if marca == '' or modelo == '' or cidade == '' or status == '':
            st.error('Preencha todos os campos!')

        elif marca != '' and modelo != '' and cidade != '' and status != '':
            url = ("String de conexão post bike")
            try:
                retorno = requests.post(url, json={"marca": marca, "modelo": modelo, "cidade": cidade, "status": status})

                if retorno.status_code == 201 or retorno.status_code == 200:
                    st.success('Bicicleta cadastrada com sucesso!')

                else:
                    st.error("Bicicleta não cadastrada!")

            except Exception as e:
                st.error("Erro ao cadastrar bicicleta!")









def data_bike():
    st.title('Dados da bicicleta')
    
    if 'bicicleta' not in st.session_state:
        st.session_state['bicicleta'] = None
    
    bicicleta_id = st.text_input('ID da bicicleta', key='bicicleta_id')

    
    if st.button('Buscar'):
        if bicicleta_id:
            try:
                r = requests.get(f'string de conexão get one bike')
                if r.status_code == 200:
                    st.session_state['bicicleta'] = r.json()

                else:
                    st.error('Bicicleta não encontrada.')
                    st.session_state['bicicleta'] = None
            except Exception as e:
                st.error(f'Erro ao buscar bicicleta: {e}')
                st.session_state['bicicleta'] = None

    if st.session_state['bicicleta']:
        with st.form("form_atualizar_bicicleta"):
       
            nova_marca = st.text_input('Marca', value=st.session_state['bicicleta'].get('marca', ''))
            novo_modelo = st.text_input('Modelo', value=st.session_state['bicicleta'].get('modelo', ''))
            nova_cidade = st.text_input('Cidade', value=st.session_state['bicicleta'].get('cidade', ''))
            novo_status = st.selectbox('Status', ['disponivel', 'alugada'], index=0 if st.session_state['bicicleta'].get('status') == 'disponivel' else 1)

            atualizar_button = st.form_submit_button('Atualizar Bicicleta')
            
            if atualizar_button:
                try:
                    update_response = requests.put(f'String de conexão put bike', json={
                        "marca": nova_marca, 
                        "modelo": novo_modelo, 
                        "cidade": nova_cidade,
                        "status": novo_status
                    })



                    if update_response.status_code in [200, 204]:
                        st.success('Bicicleta atualizada com sucesso!')
        
                        st.session_state['bicicleta']['marca'] = nova_marca
                        st.session_state['bicicleta']['modelo'] = novo_modelo
                        st.session_state['bicicleta']['cidade'] = nova_cidade
                        st.session_state['bicicleta']['status'] = novo_status
                    else:
                        st.error('Falha ao atualizar bicicleta.')
                except Exception as e:
                    st.error(f'Erro ao atualizar bicicleta: {e}')

                

        if st.button('Remover Bicicleta'):
            try:
                
                delete_response = requests.delete(f'String de conexão delete bike')

                if delete_response.status_code in [200, 204]:
                    st.success('Bicicleta removida com sucesso!')
                    st.session_state['bicicleta'] = None
                
                else:
                    st.error('Falha ao remover bicicleta.')

            except Exception as e:
                st.error(f'Erro ao remover bicicleta: {e}')






def get_loans():
    st.title('Empréstimos')

    r = requests.get('String de conexão get loans')
    status_code = r.status_code

    if status_code == 200:
        resposta_json = r.json()
        emprestimos = resposta_json
        st.table(emprestimos)






def delete_loan():
    st.title('Remover empréstimo')

    emprestimo_id = st.text_input('ID do empréstimo')

    if st.button('Remover'):

        if emprestimo_id == '':
            st.error('Preencha o campo!')

        elif emprestimo_id != '':
            url = ("String de conexão delete loan")
            try:
                retorno = requests.delete(url, json={"emprestimo_id": emprestimo_id})

                if retorno.status_code == 204:
                    st.success('Empréstimo removido com sucesso!')

                else:
                    st.error("Empréstimo não removido!")

            except Exception as e:
                st.error("Erro ao remover empréstimo!")







def post_loan():
    st.title('Realizar empréstimo')

    usuario_id = st.text_input('ID do usuário')
    bicicleta_id = st.text_input('ID da bicicleta')
    data = st.text_input('Data do empréstimo')

    

    if st.button('Enviar'):

        if usuario_id == '' or bicicleta_id == '' or data == '':
            st.error('Preencha todos os campos!')

        elif usuario_id != '' and bicicleta_id != '' and data != '':
            url = ("String de conexão post loan")
            try:
                bike = requests.get(f'String de conexão get one bike')
                status_bike = bike.json().get('status')

                if status_bike == 'disponivel':
                    retorno = requests.post(url, json={"usuario_id": usuario_id, "bicicleta_id": bicicleta_id, "data": data})

                    if retorno.status_code == 201 or retorno.status_code == 200:
                        st.success('Empréstimo cadastrado com sucesso!')

                    else:
                        st.error("Empréstimo não cadastrado!")

                else:
                    st.error("Bicicleta não disponível para empréstimo!")


            except Exception as e:
                st.error("Erro ao cadastrar empréstimo!")





st.sidebar.title("Menu")
page = st.sidebar.radio("", ('Home', "Usuários", "Cadastrar usuário", "Dados do usuário", "Bicicletas", "Cadastrar bicicleta", "Dados da bicicleta", "Empréstimos", "Realizar empréstimo", "Remover empréstimo"))

if page == 'Home':
    home_page()

elif page == 'Usuários':
    get_users()

elif page == 'Cadastrar usuário':
    post_user()

elif page == 'Dados do usuário':
    data_user()

elif page == 'Bicicletas':
    get_bikes()

elif page == 'Cadastrar bicicleta':
    post_bike()

elif page == 'Dados da bicicleta':
    data_bike()

elif page == 'Empréstimos':
    get_loans()

elif page == 'Realizar empréstimo':
    post_loan()

elif page == 'Remover empréstimo':
    delete_loan()