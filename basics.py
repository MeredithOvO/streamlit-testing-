import streamlit as st
import numpy as np
import pandas as pd

#运行方法：streamlitexamples run [file name]
#一些基础操作
#设置标题
st.title("Streamlit")
#输入信息
st.write("Streamlit")


#数据表格功能
#动态表格展示
st.subheader("动态表格")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.dataframe(dataframe.style.highlight_max(axis=0))
# 选择数据展示范围（侧边栏）
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
#静态表格展示
st.subheader("静态表格")
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

#绘制图表
st.subheader("绘制图表")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.write('line chart')
st.line_chart(chart_data)
st.write('area chart')
st.area_chart(chart_data)
st.write('bar chart')
st.bar_chart(chart_data)
st.write('altair chart')
import altair as alt
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
c = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.altair_chart(c, use_container_width=True)


#绘制地图
st.subheader("地图")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

#进度条
st.subheader('进度条')
x = st.slider('x')
st.write(x, 'squared is', x * x)

#勾选条件后展示内容
st.subheader('勾选条件后展示内容')
if st.checkbox('内容展示'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


#内容选择
st.subheader('内容选择')
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number will you select?',
     df['first column'])
'You selected: ', option


# 侧边栏中的选择框
st.subheader('选择框')
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)


#选择按钮

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# 在'with'中使用streamlit组件
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
