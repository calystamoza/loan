import streamlit as st
import pandas as pd
from pycaret.classification import *
from PIL import Image

profile = 'https://www.youtube.com/watch?v=Hd_Dy0pl1UM&pp=ygUPbWFuZGlyaSBwcm9maWxl'
logo=Image.open('images/logo.png')
with st.sidebar:
    st.image(logo, use_column_width=True)
    st.title('Help and FAQ')
    # st.markdown("The application predicts whether a loan application will be approved or rejected.")
    st.info("Asking for any help? let us know")
    # menu=st.selectbox('Pages',('Main Menu','Help'))
    st.video(profile)

st.image('C:/Users/calys/smt 4/MLOps/loan/images/cust.jpg',use_column_width=True)
st.markdown(
    """
    <div style='background-color: darkblue; padding: 10px; border-radius: 5px;'>
        <h3 style='color: yellow;'>Help and FAQ</h3>
    </div>
    """,
    unsafe_allow_html=True,
)
st.header(' ')
# Expander untuk kartu debit yang hilang
with st.expander("Lost Mandiri Debit Card"):
    st.write("""
**What should I do if my Mandiri Debit Card is lost?**
- You should first contact our call center or a branch office to have your card blocked.

**How do I block my lost card?**
Via Livin by Mandiri:
- On the home page, select Settings.
- Select Debit Card & Credit Card.
- Select the Debit Card or Credit Card you want to block.
- Select Temporary Block.
- Double-check the information of the card you want to block, then tap Block Card.
""")

# Expander untuk kartu debit yang diblokir
with st.expander("Blocked Mandiri Debit Card"):
    st.write("""
**What should I do if my Mandiri Debit Card has been blocked?**
- You only need to request the unblocking of your Mandiri Debit Card at your branch office.

**How do I get my Mandiri Debit Card unblocked?**
- Visit your nearest branch office and submit a request for the unblocking of your Mandiri Debit Card.
- Complete the Customer Request/Complaint form.
- Show valid proof of your identity.

**How long before I can use my Mandiri Debit Card again?**
Your Mandiri Debit Card can be used again immediately after it is unblocked by the branch office.
""")

with st.expander("Mandiri Debit Card Retained by ATM"):
    st.markdown(
        """
        **What should I do if my Mandiri Debit Card is retained by an ATM?**
        - Contact our call center or a branch office to have your card blocked.
        
        **How do I block my lost card?**
        - **Via Livin by Mandiri:**
          - On the home page, select Settings
          - Select Debit Card & Credit Card
          - Select the Debit Card or Credit Card you want to block
          - Select Temporary Block
          - Double-check the information of the card you want to block, then tap Block Card
          - Wait for the notification that the card has been successfully blocked
        
        - **Via call center:**
          - Contact Bank Mandiri 14000
          - If overseas, contact 021-52997777
          - The call center officer will ask you to verify your data
          - The call center officer will block your card
        
        - **Via branch office:**
          - Bring a Loss Declaration from the Police, your ID, and your account passbook
          - The officer will block your old card and issue a replacement card

        **What is the fee for replacing a lost debit card?**
        There is no fee for replacing a card that has been retained by an ATM.
        """
    )

with st.expander("Forgotten ATM PIN"):
    st.markdown(
        """
        **What should I do if I forget the ATM PIN for my Mandiri Debit Card?**
        - Contact our call center or your nearest branch office to check if your card has been blocked due to incorrect PIN entries.
        
        **How do I unblock my Mandiri Debit Card if it has been blocked because the incorrect PIN was entered 3 times, but I still remember my 6-digit PIN?**
        - Visit your nearest Bank Mandiri branch office
        - Request that your Mandiri Debit Card be unblocked
        - Complete the Customer Request/Complaint form
        - Show valid proof of your identity
        
        **What if I no longer remember my 6-digit Mandiri Debit PIN?**
        - Visit your nearest Bank Mandiri branch office
        - Request the issuance of a new Mandiri Debit Card PIN
        - Complete the Customer Request/Complaint form
        - Show valid proof of your identity
        
        **How long before I can use my Mandiri Debit Card again?**
        Your Mandiri Debit Card can be used immediately after it is unblocked.
        
        **What is the fee for the issuance of a new Bank Mandiri Debit Card PIN?**
        The fee for the issuance of a new PIN is Rp 5,000.
        """
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