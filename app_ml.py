import joblib
import numpy as np
import streamlit as st

def run_ml() :
    st.subheader('문장을 입력하면 긍정 / 부정을 예측해준다.')

    sentence = st.text_input('문장 입력')

    # 유저가 버튼을 누르면 예측하도록 만든다.
    if st.button('예측 실행') :


        vec = joblib.load('data/vec.pkl')
        classifier = joblib.load('data/classifier.pkl')
        new_data = np.array([sentence])
        X_new = vec.transform(new_data)       
        X_new = X_new.toarray()
        y_pred = classifier.predict(X_new)

        if y_pred[0] == 5 :
            st.text('입력하신 문장은 긍정입니다.')
        else :
            st.text('입력하신 문장은 부정입니다.')