import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

# st.write('DataFrame')
# st.write('Display Image')
st.write('Interactive Widgets')


# インタラクティブなウィジェット
text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', text

option = st.selectbox(
  'あなたが好きな数字を教えてください。',
  list(range(1, 100))
)
'あなたの好きな数字は「', option, '」です。'

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition

# 画像表示
# if st.checkbox('Show Image'):
#   img = Image.open('no_image.jpg')
#   st.image(img, caption='No Image', use_column_width=True)


# データフレーム
# df = pd.DataFrame({
#   '1列目': [1, 2, 3, 4],
#   '2列目': [10, 20, 30, 40]
# })

# チャート
# df = pd.DataFrame(
#   np.random.rand(20, 3),
#   columns=['a', 'b', 'c']
# )

# マッピング
# df = pd.DataFrame(
#   np.random.rand(100, 2)/[30, 30] + [35.69, 139.70],
#   columns=['lat', 'lon']
# )

# データフレーム
# st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)
# st.dataframe(df.style.highlight_max(axis=1), width=300, height=300)
# st.dataframe(df, width=100, height=100)
# st.write(df)
# st.table(df.style.highlight_max(axis=0))

# チャート
# st.write(df)
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# マッピング
# st.map(df)

# 表示
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """