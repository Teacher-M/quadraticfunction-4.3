import streamlit as st


st.set_page_config(
    page_title="이차함수 y=ax² 탐구",
    page_icon="📈",
    layout="wide"
)

st.title("📈 이차함수 y = ax²의 그래프 탐구")

st.write(
    "a의 값을 바꾸면서 그래프의 모양이 "
    "어떻게 달라지는지 관찰해 보세요."
)

st.info(
    "그래프를 충분히 관찰한 뒤, 발견한 내용을 종이 활동지에 기록하세요."
)


# --------------------------------------------------
# 함수식을 보기 좋게 표시
# --------------------------------------------------

def function_name(a):
    if a == 1:
        return "y = x²"
    elif a == -1:
        return "y = -x²"
    else:
        return f"y = {a}x²"


# --------------------------------------------------
# 그래프 자료 만들기
# --------------------------------------------------

def make_graph_rows(a_values, x_min=-4, x_max=4):
    rows = []

    # 0.05 간격으로 부드러운 그래프 만들기
    start = int(x_min * 20)
    end = int(x_max * 20)

    for i in range(start, end + 1):
        x = i / 20

        for a in a_values:
            rows.append(
                {
                    "x": x,
                    "y": a * x**2,
                    "함수": function_name(a)
                }
            )

    return rows


# --------------------------------------------------
# 좌표축의 범위가 고정된 그래프
# --------------------------------------------------

def draw_fixed_graph(
    a_values,
    x_domain,
    y_domain,
    height=500
):
    rows = make_graph_rows(
        a_values,
        x_min=x_domain[0],
        x_max=x_domain[1]
    )

    chart = {
        "height": height,
        "data": {
            "values": rows
        },
        "mark": {
            "type": "line",
            "strokeWidth": 3,
            "clip": True
        },
        "encoding": {
            "x": {
                "field": "x",
                "type": "quantitative",
                "scale": {
                    "domain": x_domain
                },
                "axis": {
                    "title": "x",
                    "grid": True,
                    "tickCount": 9
                }
            },
            "y": {
                "field": "y",
                "type": "quantitative",
                "scale": {
                    "domain": y_domain
                },
                "axis": {
                    "title": "y",
                    "grid": True
                }
            },
            "color": {
                "field": "함수",
                "type": "nominal",
                "legend": {
                    "title": "함수"
                }
            },
            "tooltip": [
                {
                    "field": "함수",
                    "type": "nominal",
                    "title": "함수"
                },
                {
                    "field": "x",
                    "type": "quantitative",
                    "title": "x",
                    "format": ".2f"
                },
                {
                    "field": "y",
                    "type": "quantitative",
                    "title": "y",
                    "format": ".2f"
                }
            ]
        },
        "config": {
            "view": {
                "stroke": "gray"
            },
            "axis": {
                "labelFontSize": 13,
                "titleFontSize": 15
            },
            "legend": {
                "labelFontSize": 13,
                "titleFontSize": 14
            }
        }
    }

    st.vega_lite_chart(
        chart,
        use_container_width=True
    )


# ==================================================
# 탐구 1
# ==================================================

st.divider()
st.header("탐구 1. a의 부호에 따른 그래프의 모양")

a = st.slider(
    "a의 값을 움직여 보세요.",
    min_value=-5,
    max_value=5,
    value=1,
    step=1
)

if a == 0:
    st.warning(
        "a가 0이면 y = 0이므로 이차함수가 아닙니다. "
        "0이 아닌 값을 선택하세요."
    )

else:
    st.subheader(f"현재 함수: {function_name(a)}")

    draw_fixed_graph(
        a_values=[a],
        x_domain=[-4, 4],
        y_domain=[-20, 20],
        height=520
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("a의 값", a)

    with col2:
        if a > 0:
            st.metric("그래프가 향하는 방향", "위쪽")
        else:
            st.metric("그래프가 향하는 방향", "아래쪽")

    st.info(
        "a가 양수일 때와 음수일 때 그래프가 향하는 방향을 비교해 보세요."
    )


# ==================================================
# 탐구 2
# ==================================================

st.divider()
st.header("탐구 2. y = x²와 y = ax²의 모양 비교")

st.write(
    "a의 값을 1부터 5까지 바꾸면서 "
    "두 그래프의 벌어진 정도를 비교해 보세요."
)

compare_a = st.slider(
    "비교할 a의 값",
    min_value=1,
    max_value=5,
    value=2,
    step=1
)

if compare_a == 1:
    compare_values = [1]
else:
    compare_values = [1, compare_a]

draw_fixed_graph(
    a_values=compare_values,
    x_domain=[-4, 4],
    y_domain=[0, 20],
    height=550
)

st.info(
    "a의 값이 커질수록 y = ax²의 그래프 모양이 "
    "어떻게 달라지는지 관찰해 보세요."
)


# ==================================================
# 탐구 3
# ==================================================

st.divider()
st.header("탐구 3. 여러 그래프를 한눈에 비교")

st.write(
    "a의 값이 다른 여러 그래프를 한 좌표평면에서 비교해 보세요."
)

width_values = [1, 2, 3, 4, 5]

draw_fixed_graph(
    a_values=width_values,
    x_domain=[-4, 4],
    y_domain=[0, 20],
    height=600
)

st.info(
    "a의 값이 커질수록 그래프가 y축 가까이에 모이는지, "
    "좌우로 벌어진 정도는 어떻게 변하는지 관찰해 보세요."
)


# ==================================================
# 탐구 4
# ==================================================

st.divider()
st.header("탐구 4. y = ax²와 y = -ax² 비교")

absolute_a = st.slider(
    "a의 절댓값",
    min_value=1,
    max_value=5,
    value=2,
    step=1
)

draw_fixed_graph(
    a_values=[absolute_a, -absolute_a],
    x_domain=[-4, 4],
    y_domain=[-20, 20],
    height=600
)

st.info(
    "두 그래프의 모양과 벌어진 정도를 비교하고, "
    "한 그래프를 어떻게 뒤집으면 다른 그래프와 겹치는지 생각해 보세요."
)


# ==================================================
# 좌표값 확인
# ==================================================

st.divider()
st.header("좌표값 확인하기")

coordinate_a = st.slider(
    "좌표를 확인할 함수의 a값",
    min_value=-5,
    max_value=5,
    value=1,
    step=1,
    key="coordinate_a"
)

coordinate_x = st.slider(
    "x의 값",
    min_value=-10,
    max_value=10,
    value=2,
    step=1
)

coordinate_y = coordinate_a * coordinate_x**2

if coordinate_a == 0:
    st.warning(
        "a가 0이면 이차함수가 아닙니다. "
        "0이 아닌 정수를 선택하세요."
    )

else:
    st.latex(
        f"y=({coordinate_a})"
        f"\\times({coordinate_x})^2"
        f"={coordinate_y}"
    )

    st.success(
        f"{function_name(coordinate_a)}의 그래프는 "
        f"점 ({coordinate_x}, {coordinate_y})을 지납니다."
    )


# ==================================================
# 탐구 후 용어 정리
# ==================================================

st.divider()
st.header("탐구 후 용어 알아보기")

st.write(
    "활동지의 탐구를 모두 마친 뒤 선생님과 함께 "
    "그래프의 모양과 각 부분의 이름을 정리해 봅시다."
)

with st.expander("용어 보기"):
    st.write(
        "이차함수 y = ax²의 그래프와 같은 모양의 곡선을 "
        "**포물선**이라고 합니다."
    )

    st.write(
        "그래프를 반으로 접었을 때 서로 겹치게 하는 직선을 "
        "포물선의 **축**이라고 합니다."
    )

    st.write(
        "포물선과 축이 만나는 점을 포물선의 "
        "**꼭짓점**이라고 합니다."
    )

    st.write(
        "이차함수 y = ax²의 그래프에서는 "
        "y축이 축이고 원점이 꼭짓점입니다."
    )


st.divider()

st.caption(
    "※ 이 웹 앱은 그래프를 탐구하기 위한 도구입니다. "
    "관찰한 내용과 결론은 종이 활동지에 기록하세요."
)