import streamlit as st


st.set_page_config(
    page_title="이차함수 y=ax² 탐구",
    page_icon="📈",
    layout="wide"
)

st.title("📈 이차함수 y = ax²의 그래프 탐구")

st.write(
    "a의 값을 바꾸면서 y = x²의 그래프와 비교해 보고, "
    "그래프의 모양이 어떻게 달라지는지 관찰해 보세요."
)

st.info(
    "이 웹 앱에서는 그래프의 변화를 눈으로 관찰합니다. "
    "발견한 내용과 그 이유는 활동지와 모둠 토의에서 정리하세요."
)


# --------------------------------------------------
# 함수 이름
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

def make_graph_rows(a_values, x_min, x_max):
    rows = []

    # 0.05 간격으로 값을 만들어 부드러운 곡선 표시
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
# 좌표축이 드러나는 그래프
# --------------------------------------------------

def draw_graph(
    a_values,
    x_domain,
    y_domain,
    graph_key,
    height=560
):
    rows = make_graph_rows(
        a_values=a_values,
        x_min=x_domain[0],
        x_max=x_domain[1]
    )

    chart = {
        "height": height,
        "layer": [
            # 함수 그래프
            {
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
                            "domain": x_domain,
                            "nice": False
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
                            "domain": y_domain,
                            "nice": False
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
                }
            },

            # x축
            {
                "data": {
                    "values": [{"y": 0}]
                },
                "mark": {
                    "type": "rule",
                    "color": "black",
                    "strokeWidth": 2
                },
                "encoding": {
                    "y": {
                        "field": "y",
                        "type": "quantitative"
                    }
                }
            },

            # y축
            {
                "data": {
                    "values": [{"x": 0}]
                },
                "mark": {
                    "type": "rule",
                    "color": "black",
                    "strokeWidth": 2
                },
                "encoding": {
                    "x": {
                        "field": "x",
                        "type": "quantitative"
                    }
                }
            }
        ],
        "config": {
            "view": {
                "stroke": "gray"
            },
            "axis": {
                "labelFontSize": 13,
                "titleFontSize": 16
            },
            "legend": {
                "labelFontSize": 13,
                "titleFontSize": 14
            }
        }
    }

    value_key = "_".join(str(a) for a in a_values)

    st.vega_lite_chart(
        chart,
        use_container_width=True,
        key=f"{graph_key}_{value_key}"
    )


# ==================================================
# 탐구 1
# ==================================================

st.divider()
st.header("탐구 1. y = x²와 y = ax² 비교")

st.write(
    "y = x²의 그래프를 기준으로, "
    "a의 값을 바꾸면서 두 그래프의 모양을 비교해 보세요."
)

a1 = st.slider(
    "비교할 a의 값",
    min_value=1,
    max_value=5,
    value=2,
    step=1,
    key="a1"
)

if a1 == 1:
    compare_values_1 = [1]
else:
    compare_values_1 = [1, a1]

draw_graph(
    a_values=compare_values_1,
    x_domain=[-3, 3],
    y_domain=[-2, 16],
    graph_key="explore1",
    height=570
)

st.info(
    "💭 a의 값이 1, 2, 3, 4, 5로 커질수록 "
    "y = ax²의 그래프는 어떻게 달라지나요?"
)


# ==================================================
# 탐구 2
# ==================================================

st.divider()
st.header("탐구 2. 여러 양수 a의 그래프 비교")

st.write(
    "a의 값이 서로 다른 여러 그래프를 한 좌표평면에서 비교해 보세요."
)

draw_graph(
    a_values=[1, 2, 3, 4, 5],
    x_domain=[-3, 3],
    y_domain=[-2, 16],
    graph_key="explore2",
    height=610
)

st.info(
    "💭 여러 그래프의 공통점과 차이점을 찾아보세요."
)


# ==================================================
# 탐구 3
# ==================================================

st.divider()
st.header("탐구 3. a의 부호와 그래프의 방향")

st.write(
    "a의 값을 양수와 음수로 바꾸면서 "
    "그래프가 향하는 방향을 비교해 보세요."
)

a3 = st.slider(
    "a의 값",
    min_value=-5,
    max_value=5,
    value=1,
    step=1,
    key="a3"
)

if a3 == 0:
    st.warning(
        "a가 0이면 y = 0이므로 이차함수가 아닙니다. "
        "0이 아닌 값을 선택하세요."
    )

else:
    st.subheader(f"현재 함수: {function_name(a3)}")

    if a3 > 0:
        y_range_3 = [-3, 22]
    else:
        y_range_3 = [-22, 3]

    draw_graph(
        a_values=[a3],
        x_domain=[-4, 4],
        y_domain=y_range_3,
        graph_key="explore3",
        height=570
    )

    st.info(
        "💭 a가 양수일 때와 음수일 때 "
        "그래프의 모양은 어떻게 달라지나요?"
    )


# ==================================================
# 탐구 4
# ==================================================

st.divider()
st.header("탐구 4. y = ax²와 y = -ax² 비교")

st.write(
    "절댓값은 같고 부호만 다른 두 그래프의 관계를 관찰해 보세요."
)

a4 = st.slider(
    "a의 절댓값",
    min_value=1,
    max_value=5,
    value=2,
    step=1,
    key="a4"
)

draw_graph(
    a_values=[a4, -a4],
    x_domain=[-6, 6],
    y_domain=[-30, 30],
    graph_key="explore4",
    height=610
)

st.info(
    "💭 두 그래프의 모양과 위치에는 어떤 관계가 있나요?"
)


st.divider()

st.caption(
    "※ 앱에서는 그래프의 변화를 먼저 발견하고, "
    "활동지에서는 표와 좌표를 이용하여 그 이유를 설명해 보세요."
)