import streamlit as st

st.set_page_config(
    page_title="이차함수 y=ax² 탐구",
    page_icon="📈",
    layout="wide"
)

st.title("📈 이차함수 y = ax²의 그래프 탐구")

st.write(
    "a의 값을 바꾸면서 그래프의 방향과 폭이 어떻게 달라지는지 관찰해 보세요."
)

st.info(
    "그래프를 관찰한 뒤, 발견한 내용을 종이 활동지에 기록하세요."
)


# 함수식을 보기 좋게 나타내는 함수
def function_name(a):
    if a == 1:
        return "y = x²"
    elif a == -1:
        return "y = -x²"
    else:
        return f"y = {a:g}x²"


# 그래프에 사용할 x, y값을 만드는 함수
def make_graph_data(a_values, x_limit):
    graph_data = {"x": []}

    for a in a_values:
        graph_data[function_name(a)] = []

    # 0.1 간격으로 촘촘하게 그래프를 그림
    start = int(-x_limit * 10)
    end = int(x_limit * 10)

    for i in range(start, end + 1):
        x = i / 10
        graph_data["x"].append(x)

        for a in a_values:
            y = a * x**2
            graph_data[function_name(a)].append(y)

    return graph_data


# --------------------------------------------------
# 그래프 범위 설정
# --------------------------------------------------

st.sidebar.header("그래프 설정")

x_limit = st.sidebar.slider(
    "x축 범위",
    min_value=5,
    max_value=30,
    value=20,
    step=5
)

st.sidebar.write(
    f"현재 x축의 범위는 -{x_limit}부터 {x_limit}까지입니다."
)


# --------------------------------------------------
# 탐구 1
# --------------------------------------------------

st.divider()
st.header("탐구 1. a의 값을 자유롭게 바꾸어 보기")

a = st.slider(
    "a의 값을 움직여 보세요.",
    min_value=-5.0,
    max_value=5.0,
    value=1.0,
    step=0.25
)

if a == 0:
    st.warning("a가 0이면 y = 0이므로 이차함수가 아닙니다.")

else:
    st.subheader(f"현재 함수: {function_name(a)}")

    graph_data = make_graph_data([a], x_limit)

    st.line_chart(
        graph_data,
        x="x",
        y=function_name(a),
        height=550
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("a의 값", f"{a:g}")

    with col2:
        if a > 0:
            st.metric("그래프의 방향", "아래로 볼록")
        else:
            st.metric("그래프의 방향", "위로 볼록")

    with col3:
        st.metric("꼭짓점", "(0, 0)")

    st.caption(
        f"그래프는 x의 값이 -{x_limit}부터 {x_limit}인 범위를 나타냅니다. "
        "실수 전체를 화면에 모두 표시할 수 없으므로 넓은 구간을 이용해 "
        "그래프의 전체적인 모양을 관찰합니다."
    )


# --------------------------------------------------
# 탐구 2
# --------------------------------------------------

st.divider()
st.header("탐구 2. y = x²와 y = ax² 비교하기")

compare_a = st.select_slider(
    "비교할 a의 값을 선택하세요.",
    options=[0.25, 0.5, 1, 2, 3, 4, 5],
    value=2
)

compare_data = make_graph_data([1, compare_a], x_limit)

if compare_a == 1:
    st.line_chart(
        compare_data,
        x="x",
        y="y = x²",
        height=550
    )
else:
    st.line_chart(
        compare_data,
        x="x",
        y=["y = x²", function_name(compare_a)],
        height=550
    )

st.write(
    "두 그래프의 꼭짓점과 축은 같은지, "
    "a의 값이 커질 때 그래프의 폭은 어떻게 달라지는지 관찰해 보세요."
)


# --------------------------------------------------
# 탐구 3
# --------------------------------------------------

st.divider()
st.header("탐구 3. 여러 그래프의 폭 비교하기")

width_data = make_graph_data(
    [0.25, 0.5, 1, 2, 4],
    x_limit
)

st.line_chart(
    width_data,
    x="x",
    y=[
        "y = 0.25x²",
        "y = 0.5x²",
        "y = x²",
        "y = 2x²",
        "y = 4x²"
    ],
    height=600
)

st.write(
    "a의 절댓값이 0에 가까워질 때와 커질 때를 비교하여 "
    "그래프의 폭이 어떻게 달라지는지 관찰해 보세요."
)


# --------------------------------------------------
# 탐구 4
# --------------------------------------------------

st.divider()
st.header("탐구 4. y = ax²와 y = -ax² 비교하기")

absolute_a = st.select_slider(
    "a의 절댓값을 선택하세요.",
    options=[0.25, 0.5, 1, 2, 3, 4, 5],
    value=2
)

symmetry_data = make_graph_data(
    [absolute_a, -absolute_a],
    x_limit
)

st.line_chart(
    symmetry_data,
    x="x",
    y=[
        function_name(absolute_a),
        function_name(-absolute_a)
    ],
    height=600
)

st.write(
    "두 그래프의 각 점이 어떤 축을 기준으로 서로 대응하는지 관찰해 보세요."
)


# --------------------------------------------------
# 좌표값 확인
# --------------------------------------------------

st.divider()
st.header("좌표값 확인하기")

coordinate_a = st.slider(
    "좌표를 확인할 함수의 a값",
    min_value=-5.0,
    max_value=5.0,
    value=1.0,
    step=0.25,
    key="coordinate_a"
)

coordinate_x = st.slider(
    "x의 값",
    min_value=-20.0,
    max_value=20.0,
    value=2.0,
    step=0.5
)

coordinate_y = coordinate_a * coordinate_x**2

st.latex(
    f"y = ({coordinate_a:g})"
    f"\\times ({coordinate_x:g})^2"
    f" = {coordinate_y:g}"
)

st.success(
    f"{function_name(coordinate_a)}의 그래프는 "
    f"점 ({coordinate_x:g}, {coordinate_y:g})을 지납니다."
)

st.divider()

st.caption(
    "※ 이 웹 앱은 그래프를 탐구하기 위한 도구입니다. "
    "관찰한 내용과 결론은 종이 활동지에 기록하세요."
)