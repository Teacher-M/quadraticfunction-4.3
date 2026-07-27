import streamlit as st

st.set_page_config(
    page_title="이차함수 y=ax² 탐구",
    page_icon="📈",
    layout="wide"
)

st.title("📈 이차함수 y = ax²의 그래프 탐구")
st.write(
    "그래프와 함숫값을 관찰하여 계수 a가 그래프에 미치는 영향을 탐구해 봅시다."
)

st.info(
    "📌 활동 방법\n\n"
    "1. 웹 앱에서 a의 값을 바꾸어 봅니다.\n"
    "2. 그래프와 표를 관찰합니다.\n"
    "3. 발견한 내용을 활동지에 기록합니다.\n"
    "4. 마지막에 탐구 결과를 스스로 정리합니다."
)

# -------------------------------------------------
# 기본 함수
# -------------------------------------------------

def calculate_y(a, x):
    return a * x**2


def show_function(a):
    if a == 1:
        return "y = x²"
    elif a == -1:
        return "y = -x²"
    else:
        return f"y = {a}x²"


# -------------------------------------------------
# 탐구 1
# -------------------------------------------------

st.divider()
st.header("탐구 1. y = x²와 y = ax²의 함숫값 비교")

st.write(
    "먼저 기준이 되는 함수 y = x²와 다른 이차함수 y = ax²를 비교해 봅시다."
)

a1 = st.select_slider(
    "비교할 a의 값을 선택하세요.",
    options=[0.25, 0.5, 1, 2, 3, 4],
    value=2,
    key="a1"
)

x_values = [-3, -2, -1, 0, 1, 2, 3]

base_values = []
compare_values = []

for x in x_values:
    base_values.append(x**2)
    compare_values.append(calculate_y(a1, x))

st.subheader("① 함숫값 표")

table_data = {
    "x": x_values,
    "y = x²": base_values,
    show_function(a1): compare_values
}

st.dataframe(
    table_data,
    use_container_width=True,
    hide_index=True
)

st.subheader("② 그래프 비교")

graph_x = []
graph_base_y = []
graph_compare_y = []

for i in range(-60, 61):
    x = i / 10

    graph_x.append(x)
    graph_base_y.append(x**2)
    graph_compare_y.append(calculate_y(a1, x))

graph_data_1 = {
    "x": graph_x,
    "y = x²": graph_base_y,
    show_function(a1): graph_compare_y
}

st.line_chart(
    graph_data_1,
    x="x",
    y=["y = x²", show_function(a1)]
)

st.warning(
    "✏️ 활동지 기록 1\n\n"
    "x의 값이 같을 때, y = ax²의 함숫값은 "
    "y = x²의 함숫값과 어떤 관계가 있는지 적어 보세요."
)

with st.expander("힌트 보기"):
    st.write(
        f"예를 들어 x = 2일 때, x²의 값은 4이고 "
        f"{show_function(a1)}의 함숫값은 {calculate_y(a1, 2)}입니다."
    )

with st.expander("탐구 결과 확인"):
    st.success(
        f"x의 값이 같을 때, {show_function(a1)}의 함숫값은 "
        f"y = x²의 함숫값의 {a1}배입니다."
    )


# -------------------------------------------------
# 탐구 2
# -------------------------------------------------

st.divider()
st.header("탐구 2. a의 부호와 그래프의 방향")

st.write("a의 값을 양수와 음수로 바꾸면서 그래프를 관찰해 봅시다.")

a2 = st.slider(
    "a의 값을 움직여 보세요.",
    min_value=-4.0,
    max_value=4.0,
    value=1.0,
    step=0.5,
    key="a2"
)

if a2 == 0:
    st.warning("a가 0이면 y = 0이므로 이차함수가 아닙니다.")
else:
    st.latex(f"y={a2}x^2")

    graph_x_2 = []
    graph_y_2 = []

    for i in range(-60, 61):
        x = i / 10
        y = calculate_y(a2, x)

        graph_x_2.append(x)
        graph_y_2.append(y)

    graph_data_2 = {
        "x": graph_x_2,
        show_function(a2): graph_y_2
    }

    st.line_chart(
        graph_data_2,
        x="x",
        y=show_function(a2)
    )

    col1, col2 = st.columns(2)

    with col1:
        st.write("현재 a의 부호")
        if a2 > 0:
            st.success("a > 0")
        else:
            st.error("a < 0")

    with col2:
        st.write("그래프의 방향")
        if a2 > 0:
            st.success("아래로 볼록")
        else:
            st.error("위로 볼록")

st.warning(
    "✏️ 활동지 기록 2\n\n"
    "① a > 0일 때 그래프는 어느 방향으로 볼록한가요?\n\n"
    "② a < 0일 때 그래프는 어느 방향으로 볼록한가요?"
)


# -------------------------------------------------
# 탐구 3
# -------------------------------------------------

st.divider()
st.header("탐구 3. |a|와 그래프의 폭")

st.write(
    "a의 부호는 같게 두고, a의 절댓값만 바꾸어 그래프의 폭을 비교해 봅시다."
)

a3 = st.select_slider(
    "양수 a의 값을 선택하세요.",
    options=[0.25, 0.5, 1, 2, 3, 4],
    value=1,
    key="a3"
)

graph_x_3 = []
wide_y = []
standard_y = []
selected_y = []

for i in range(-60, 61):
    x = i / 10

    graph_x_3.append(x)
    wide_y.append(0.5 * x**2)
    standard_y.append(x**2)
    selected_y.append(a3 * x**2)

graph_data_3 = {
    "x": graph_x_3,
    "y = 0.5x²": wide_y,
    "y = x²": standard_y,
    show_function(a3): selected_y
}

st.line_chart(
    graph_data_3,
    x="x",
    y=["y = 0.5x²", "y = x²", show_function(a3)]
)

st.warning(
    "✏️ 활동지 기록 3\n\n"
    "① |a|가 1보다 클 때 그래프의 폭은 y = x²보다 어떻게 되나요?\n\n"
    "② 0 < |a| < 1일 때 그래프의 폭은 y = x²보다 어떻게 되나요?\n\n"
    "③ |a|가 커질수록 그래프의 폭은 어떻게 변하나요?"
)

with st.expander("탐구 결과 확인"):
    st.success(
        "|a|가 커질수록 그래프의 폭은 좁아지고, "
        "|a|가 작아질수록 그래프의 폭은 넓어집니다."
    )


# -------------------------------------------------
# 탐구 4
# -------------------------------------------------

st.divider()
st.header("탐구 4. y = ax²와 y = -ax²의 관계")

st.write(
    "a와 -a를 계수로 가지는 두 이차함수의 그래프를 비교해 봅시다."
)

a4 = st.select_slider(
    "a의 절댓값을 선택하세요.",
    options=[0.5, 1, 2, 3, 4],
    value=2,
    key="a4"
)

graph_x_4 = []
positive_y = []
negative_y = []

for i in range(-60, 61):
    x = i / 10

    graph_x_4.append(x)
    positive_y.append(a4 * x**2)
    negative_y.append(-a4 * x**2)

positive_name = show_function(a4)
negative_name = show_function(-a4)

graph_data_4 = {
    "x": graph_x_4,
    positive_name: positive_y,
    negative_name: negative_y
}

st.line_chart(
    graph_data_4,
    x="x",
    y=[positive_name, negative_name]
)

st.warning(
    "✏️ 활동지 기록 4\n\n"
    f"{positive_name}의 그래프와 {negative_name}의 그래프는 "
    "어떤 축에 대하여 대칭인가요?"
)

with st.expander("탐구 결과 확인"):
    st.success(
        "y = ax²의 그래프와 y = -ax²의 그래프는 "
        "x축에 대하여 대칭입니다."
    )


# -------------------------------------------------
# 탐구 5
# -------------------------------------------------

st.divider()
st.header("탐구 5. 포물선의 공통점 찾기")

st.write("a의 값을 여러 번 바꾸어 보면서 변하지 않는 특징을 찾아봅시다.")

a5 = st.slider(
    "a의 값을 바꾸어 보세요.",
    min_value=-5.0,
    max_value=5.0,
    value=2.0,
    step=0.5,
    key="a5"
)

if a5 == 0:
    st.warning("a는 0이 아닌 값으로 선택하세요.")
else:
    graph_x_5 = []
    graph_y_5 = []

    for i in range(-60, 61):
        x = i / 10

        graph_x_5.append(x)
        graph_y_5.append(a5 * x**2)

    graph_data_5 = {
        "x": graph_x_5,
        show_function(a5): graph_y_5
    }

    st.line_chart(
        graph_data_5,
        x="x",
        y=show_function(a5)
    )

    st.write("현재 그래프가 지나는 점: **(0, 0)**")
    st.write("현재 그래프의 축: **y축**")
    st.write("현재 그래프의 꼭짓점: **(0, 0)**")

st.warning(
    "✏️ 활동지 기록 5\n\n"
    "① 모든 y = ax²의 그래프가 공통으로 지나는 점을 적어 보세요.\n\n"
    "② 그래프의 축을 적어 보세요.\n\n"
    "③ 꼭짓점의 좌표를 적어 보세요.\n\n"
    "④ 이러한 모양의 곡선을 무엇이라고 하는지 적어 보세요."
)


# -------------------------------------------------
# 최종 정리
# -------------------------------------------------

st.divider()
st.header("📝 최종 탐구 결과 정리")

st.write("활동지의 빈칸을 자신의 말로 완성해 보세요.")

st.markdown(
    """
    **1.** 이차함수 \(y=ax^2\)의 그래프는 원점을 __________으로 하고,
    __________을 축으로 하는 포물선이다.

    **2.** \(a>0\)이면 그래프는 __________로 볼록하다.

    **3.** \(a<0\)이면 그래프는 __________로 볼록하다.

    **4.** \(|a|\)가 클수록 그래프의 폭은 __________진다.

    **5.** \(y=ax^2\)와 \(y=-ax^2\)의 그래프는 __________에 대하여 대칭이다.
    """
)

student_summary = st.text_area(
    "웹 앱을 통해 새롭게 알게 된 점을 한 문장으로 적어 보세요.",
    placeholder="예: a의 절댓값이 커질수록 그래프의 폭이 좁아진다는 것을 알게 되었다."
)

if st.button("최종 정답 확인"):
    st.success(
        "1. 꼭짓점, y축\n\n"
        "2. 아래\n\n"
        "3. 위\n\n"
        "4. 좁아\n\n"
        "5. x축"
    )

    if student_summary:
        st.write("내가 작성한 탐구 결과")
        st.info(student_summary)

st.divider()
st.caption(
    "※ 입력한 내용은 웹 페이지를 새로고침하면 사라질 수 있습니다. "
    "중요한 탐구 결과는 반드시 활동지에 기록하세요."
)