import math
import streamlit as st


st.set_page_config(
    page_title="이차함수 y=ax² 탐구",
    page_icon="📈",
    layout="wide"
)

st.title("📈 이차함수 y = ax²의 그래프 탐구")

st.write(
    "a의 값을 바꾸면서 그래프의 방향과 폭이 "
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

    # 0.05 간격으로 부드러운 곡선 만들기
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
# 좌표축이 고정된 그래프
# --------------------------------------------------

def draw_fixed_graph(
    a_values,
    x_domain,
    y_domain,
    height=500,
    guide_y=None
):
    rows = make_graph_rows(
        a_values,
        x_min=x_domain[0],
        x_max=x_domain[1]
    )

    layers = [
        {
            "data": {"values": rows},
            "mark": {
                "type": "line",
                "strokeWidth": 3,
                "clip": True
            },
            "encoding": {
                "x": {
                    "field": "x",
                    "type": "quantitative",
                    "scale": {"domain": x_domain},
                    "axis": {
                        "title": "x",
                        "grid": True,
                        "tickCount": 9
                    }
                },
                "y": {
                    "field": "y",
                    "type": "quantitative",
                    "scale": {"domain": y_domain},
                    "axis": {
                        "title": "y",
                        "grid": True
                    }
                },
                "color": {
                    "field": "함수",
                    "type": "nominal",
                    "legend": {"title": "함수"}
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
            }
        }
    ]

    # 같은 높이에서 폭을 비교하기 위한 가로선
    if guide_y is not None:
        layers.append(
            {
                "data": {
                    "values": [{"y": guide_y}]
                },
                "mark": {
                    "type": "rule",
                    "strokeDash": [6, 4],
                    "strokeWidth": 2
                },
                "encoding": {
                    "y": {
                        "field": "y",
                        "type": "quantitative"
                    }
                }
            }
        )

    chart = {
        "height": height,
        "layer": layers,
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
st.header("탐구 1. a의 부호에 따른 그래프의 방향")

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

    # x축과 y축 범위를 고정
    draw_fixed_graph(
        a_values=[a],
        x_domain=[-4, 4],
        y_domain=[-20, 20],
        height=520
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("a의 값", a)

    with col2:
        if a > 0:
            st.metric("그래프의 방향", "아래로 볼록")
        else:
            st.metric("그래프의 방향", "위로 볼록")

    with col3:
        st.metric("꼭짓점", "(0, 0)")

    st.caption(
        "모든 a값에서 좌표축의 범위를 똑같이 유지합니다. "
        "따라서 a값에 따른 그래프의 실제 변화를 비교할 수 있습니다."
    )


# ==================================================
# 탐구 2
# ==================================================

st.divider()
st.header("탐구 2. y = x²와 y = ax²의 폭 비교")

st.write(
    "a의 값을 1부터 5까지 바꾸면서 두 그래프의 폭을 비교해 보세요."
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
    height=550,
    guide_y=4
)

st.write(
    "그래프에 표시된 가로 점선은 **y = 4**입니다. "
    "두 그래프가 이 선과 만나는 위치를 비교해 보세요."
)

if compare_a > 0:
    intersection_x = math.sqrt(4 / compare_a)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "y = x²가 y = 4와 만나는 x값",
            "±2"
        )

    with col2:
        st.metric(
            f"{function_name(compare_a)}가 y = 4와 만나는 x값",
            f"약 ±{intersection_x:.2f}"
        )

st.info(
    "a가 커질수록 같은 높이에서 그래프의 두 점 사이 거리가 줄어드는지 "
    "관찰해 보세요."
)


# ==================================================
# 탐구 3
# ==================================================

st.divider()
st.header("탐구 3. 여러 그래프의 폭 한눈에 비교")

st.write(
    "좌표축을 고정한 상태에서 여러 그래프를 한꺼번에 비교해 보세요."
)

width_values = [1, 2, 3, 4, 5]

draw_fixed_graph(
    a_values=width_values,
    x_domain=[-4, 4],
    y_domain=[0, 20],
    height=600,
    guide_y=4
)

st.write(
    "모든 그래프는 원점을 지나지만, a값이 커질수록 "
    "그래프가 y축 가까이에 모이는지 관찰해 보세요."
)

st.caption(
    "실수 전체를 화면에 전부 나타내는 것은 불가능합니다. "
    "포물선의 개형을 잘 관찰할 수 있도록 "
    "x축은 -4부터 4, y축은 0부터 20으로 고정했습니다."
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

st.write(
    "두 그래프의 모양과 폭은 같고, 어느 축을 기준으로 "
    "서로 뒤집힌 모양인지 관찰해 보세요."
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

    draw_fixed_graph(
        a_values=[coordinate_a],
        x_domain=[-4, 4],
        y_domain=[-20, 20],
        height=420
    )


st.divider()

st.caption(
    "※ 이 웹 앱은 그래프를 탐구하기 위한 도구입니다. "
    "관찰한 내용과 결론은 종이 활동지에 기록하세요."
)