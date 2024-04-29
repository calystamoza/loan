import streamlit as st
import pandas as pd
from pycaret.classification import *
from PIL import Image

# Muat model (sesuaikan path jika diperlukan)
model = load_model('C:/Users/calys/smt 4/MLOps/loan/loan_pipeline')

# Fungsi untuk membuat prediksi
def predict(model, input_df):
    predictions_df = predict_model(model, data=input_df)
    st.write(predictions_df)
    prediction = predictions_df['prediction_label'][0]
    return prediction

tab1, tab2 = st.tabs(["Loans Applicant Form", "About Us"])
with tab1:
    # Fungsi untuk halaman informasi pribadi
    def personal_info_form():
        st.header("Personal Information")
        st.image("images/mandirai.jpg")
        # Variabel informasi pribadi
        name = st.text_input("Name", "Your Name")
        gender = st.selectbox("Gender", ("Male", "Female"), index=None)
        married = st.selectbox("Marriage status", ("Yes", "No"), index=None)
        dependent = st.selectbox("Dependents", ("0", "1", "2", "3+"), index=None)
        edu = st.selectbox("Education", ("Graduate", "Not Graduate"), index=None)
        employed = st.selectbox("Self Employed", ("Yes", "No"), index=None)
        
        # Simpan data di session state
        st.session_state["personal_info"] = {
            "Gender": gender,
            "Married": married,
            "Dependents": dependent,
            "Education": edu,
            "Self_Employed": employed,
        }
        
        if st.button("Next"):
            st.session_state["page"] = "financial_form"

    def financial_info_form():
        st.header("Loan Application Form")
        st.image("images/mandirai.jpg")

        if st.button("Back"):
            st.session_state["page"] = "personal_info_form"
        
        # Variabel keuangan
        inc = st.number_input("Applicant Income ($)", value=0)
        coinc = st.number_input("Co-Applicant Income ($)", value=0)
        amount = st.number_input("Loan Amount ($)", value=0)
        term = st.number_input("Loan Term (Month)", value=0)
        hist_mapping = {'Yes': 1, 'No': 0}
        hist = st.selectbox("Credit History", list(hist_mapping.keys()))
        area = st.selectbox("Property Area", ("Urban", "Semi-Urban", "Rural"), index=None)

        st.session_state["financial_info"] = {
            "ApplicantIncome": inc,
            "CoapplicantIncome": coinc,
            "LoanAmount": amount,
            "Loan_Amount_Term": term,
            "Credit_History": hist_mapping[hist],
            "Property_Area": area,
        }
        
        if st.button("Submit"):
            input_dict = {**st.session_state["personal_info"], **st.session_state["financial_info"]}
            input_df = pd.DataFrame([input_dict])
            prediction = predict(model, input_df)
            if prediction == "Y":
                st.info("Loan Approved")
                st.balloons()
            else:
                st.error("Loan Rejected")
        

    def run():
        if "page" not in st.session_state:
            st.session_state["page"] = "personal_info_form"  

        if st.session_state["page"] == "personal_info_form":
            personal_info_form()
        elif st.session_state["page"] == "financial_form":
            financial_info_form()

    if __name__ == "__main__":
        run()

# Sidebar
profile = 'https://www.youtube.com/watch?v=Hd_Dy0pl1UM&pp=ygUPbWFuZGlyaSBwcm9maWxl'
logo=Image.open('images/logo.png')
with st.sidebar:
    st.image(logo, use_column_width=True)
    st.title('Customer Loans')
    # st.markdown("The application predicts whether a loan application will be approved or rejected.")
    st.info("The application predicts whether a loan application will be approved or rejected.")
    # menu=st.selectbox('Pages',('Main Menu','Help'))
    st.video(profile)

with tab2:
    st.snow()
    st.image("C:/Users/calys/smt 4/MLOps/loan/images/ab.jpg")
    st.markdown("<h1 style='color: navy;'>Bank Mandiri's Transformation</h1>", unsafe_allow_html=True)
    st.markdown("Bank Mandiri was established on 2 October 1998, as part of the bank restructuring program of the Government of Indonesia. In July 1999, four state-owned banks - Bank Bumi Daya, Bank Dagang Negara, Bank Exim and Bapindo - were amalgamated into Bank Mandiri. The history of these four banks can be traced back to over 140 years, and together they had contributed to the beginning of the Indonesian banking sector.")

    st.markdown(
        """
        <div style='background-color: darkblue; padding: 15px; border-radius: 10px;'>
            <h3 style='color: yellow;'>Vision</h3>
            <p style='color: white;'>
                We aim to be your preferred financial partner
            </p>
            <h3 style='color: yellow;'>Mission</h3>
            <p style='color: white;'>
                Seamlessly integrate our financial products & services into our customers' lives by delivering simple, fast digital banking solutions
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.header(' ')
    st.image("C:/Users/calys/smt 4/MLOps/loan/images/cor.jpg")
    st.markdown('Through our long and historic journey, always committed to making a maximum contribution')
    st.markdown(
    """
    <div style='background-color: #f0f8ff; padding: 15px; border-radius: 10px;'>
        <h1 style='color: #2c3e50;'>With Us</h1>
        <p style='color: #2c3e50;'>
            "With the spirit of Leading, Trusted, and Growing with You, Bank Mandiri Group has pledged itself to be an innovative, responsive, and solutive financial entity in order to be able to anticipate the challenges of economic development and to fulfill all of the customer’s needs."
        </p>
        <p style='color: #3498db;'>
        -Bank Mandiri
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
    st.markdown("## Contact Us")

    st.markdown(
        """
        | Contact Method | Details                |
        | -------------- | ---------------------- |
        | Email          | calystakeren@example.com        |
        | Facebook       | [anjaykeren](https://www.facebook.com/hahahihihoho.hahahihihoho.58) |
        | Twitter        | [@calkeren](https://twitter.com/mandiricare) |
        | WhatsApp       | MITA                   |
        | Hubungi Kami   | +62 8136 7407 310           |
        | Mandiri Call   | 14000                  |
        """
    )

