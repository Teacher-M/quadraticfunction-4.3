import streamlit as st


st.set_page_config(
    page_title="이차함수 y=ax² 탐구",
    page_icon="📈",
    layout="wide"
)

st.title("📈 이차함수 y = ax²의 그래프 탐구")

st.write(
    "a의 값을 바꾸면서 그래프의 방향과 벌어진 정도가 "
    "어떻게 달라지는지 관찰해 보세요."
)

st.info(
    "웹 앱에서 그래프를 충분히 관찰한 뒤, "
    "발견한 내용을 종이 활동지에 기록하세요."
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

    # 0.05 간격으로 값을 만들어 곡선을 부드럽게 표시
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
# x축과 y축이 표시된 그래프
# --------------------------------------------------

def draw_graph(
    a_values,
    x_domain,
    y_domain,
    graph_key,
    height=520
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

            # x축: y = 0
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

            # y축: x = 0
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

    # a값이 바뀔 때 그래프를 새로 그리도록 고유한 key 사용
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
st.header("탐구 1. a의 부호와 그래프의 방향")

st.write(
    "a의 값을 양수와 음수로 바꾸면서 "
    "그래프가 어느 방향으로 향하는지 관찰해 보세요."
)

a1 = st.slider(
    "a의 값",
    min_value=-5,
    max_value=5,
    value=1,
    step=1,
    key="a1"
)

if a1 == 0:
    st.warning(
        "a가 0이면 y = 0이므로 이차함수가 아닙니다. "
        "0이 아닌 값을 선택하세요."
    )

else:
    st.subheader(f"현재 함수: {function_name(a1)}")

    draw_graph(
        a_values=[a1],
        x_domain=[-4, 4],
        y_domain=[-20, 20],
        graph_key="explore1",
        height=540
    )

    st.info(
        "💭 생각해 보기\n\n"
        "a가 양수일 때와 음수일 때 그래프의 방향은 어떻게 달라지나요?"
    )


# ==================================================
# 탐구 2
# ==================================================

st.divider()
st.header("탐구 2. y = x²와 y = ax²의 모양 비교")

st.write(
    "좌표평면의 범위는 그대로 두고, "
    "a의 값만 바꾸면서 두 그래프를 비교해 보세요."
)

a2 = st.slider(
    "비교할 a의 값",
    min_value=1,
    max_value=5,
    value=2,
    step=1,
    key="a2"
)

if a2 == 1:
    compare_values = [1]
else:
    compare_values = [1, a2]

draw_graph(
    a_values=compare_values,
    x_domain=[-3, 3],
    y_domain=[0, 15],
    graph_key="explore2",
    height=560
)

st.info(
    "💭 생각해 보기\n\n"
    "a의 값이 1, 2, 3, 4, 5로 커질수록 "
    "y = ax²의 그래프가 좌우로 벌어진 정도는 어떻게 변하나요?"
)


# ==================================================
# 탐구 3
# ==================================================

st.divider()
st.header("탐구 3. 여러 그래프를 한눈에 비교")

st.write(
    "a의 값이 다른 그래프를 한 좌표평면에 나타냈습니다."
)

draw_graph(
    a_values=[1, 2, 3, 4, 5],
    x_domain=[-3, 3],
    y_domain=[0, 15],
    graph_key="explore3",
    height=600
)

st.info(
    "💭 생각해 보기\n\n"
    "① 모든 그래프가 공통으로 지나는 점이 있나요?\n\n"
    "② a의 값이 커질수록 그래프는 어느 쪽에 가까워지나요?\n\n"
    "③ 그래프의 왼쪽과 오른쪽 모양에서 어떤 공통점을 찾을 수 있나요?"
)


# ==================================================
# 탐구 4
# ==================================================

st.divider()
st.header("탐구 4. y = ax²와 y = -ax² 비교")

st.write(
    "a와 -a를 계수로 갖는 두 그래프의 관계를 관찰해 보세요."
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
    x_domain=[-3, 3],
    y_domain=[-15, 15],
    graph_key="explore4",
    height=600
)

st.info(
    "💭 생각해 보기\n\n"
    "한 그래프를 어느 선을 기준으로 뒤집으면 "
    "다른 그래프와 겹칠까요?"
)


# ==================================================
# 좌표값 확인
# ==================================================

st.divider()
st.header("좌표값 확인하기")

st.write(
    "a와 x의 값을 정하고, 그때의 y값과 그래프 위의 점을 확인해 보세요."
)

coordinate_a = st.slider(
    "a의 값",
    min_value=-5,
    max_value=5,
    value=1,
    step=1,
    key="coordinate_a"
)

coordinate_x = st.slider(
    "x의 값",
    min_value=-5,
    max_value=5,
    value=2,
    step=1,
    key="coordinate_x"
)

if coordinate_a == 0:
    st.warning(
        "a가 0이면 이차함수가 아닙니다. "
        "0이 아닌 값을 선택하세요."
    )

else:
    coordinate_y = coordinate_a * coordinate_x**2

    st.latex(
        f"y=({coordinate_a})"
        f"\\times({coordinate_x})^2"
        f"={coordinate_y}"
    )

    st.success(
        f"그래프는 점 ({coordinate_x}, {coordinate_y})을 지납니다."
    )


# ==================================================
# 그래프의 특징 발견하기
# ==================================================

st.divider()
st.header("🔎 그래프의 특징에 이름 붙이기")

st.write(
    "지금까지 관찰한 그래프에는 눈에 띄는 특징이 있습니다. "
    "먼저 자신만의 말로 설명해 보세요."
)

st.subheader("발견 1. 그래프를 반으로 나누는 선")

st.write(
    "그래프의 왼쪽 부분과 오른쪽 부분은 "
    "한 직선을 기준으로 서로 겹쳐지는 모양입니다."
)

st.info(
    "💭 이 직선에 이름을 붙인다면 어떤 이름이 좋을까요?\n\n"
    "활동지에 자신이 생각한 이름과 그 이유를 적어 보세요."
)

with st.expander("수학에서는 어떤 이름을 사용할까요?"):
    st.write(
        "수학에서는 그래프를 대칭이 되도록 나누는 직선을 "
        "**포물선의 축**이라고 부릅니다."
    )

    st.write(
        "이차함수 y = ax²의 그래프에서는 "
        "**y축**이 이 역할을 합니다."
    )


st.subheader("발견 2. 방향이 바뀌는 특별한 점")

st.write(
    "그래프를 따라가다 보면 아래쪽 또는 위쪽에서 "
    "방향이 바뀌는 특별한 점이 있습니다."
)

st.info(
    "💭 이 점에 이름을 붙인다면 어떤 이름이 좋을까요?\n\n"
    "이 점이 다른 점들과 무엇이 다른지도 활동지에 적어 보세요."
)

with st.expander("수학에서는 어떤 이름을 사용할까요?"):
    st.write(
        "수학에서는 그래프와 축이 만나는 특별한 점을 "
        "**포물선의 꼭짓점**이라고 부릅니다."
    )

    st.write(
        "이차함수 y = ax²의 그래프에서는 "
        "원점 **(0, 0)**이 이 점입니다."
    )


st.subheader("발견 3. 이 곡선 전체의 이름")

st.write(
    "지금까지 살펴본 그래프들은 모두 비슷한 곡선 모양을 가지고 있습니다."
)

st.info(
    "💭 이 곡선 모양 전체에 이름을 붙인다면 어떤 이름이 좋을까요?"
)

with st.expander("수학에서는 어떤 이름을 사용할까요?"):
    st.write(
        "이차함수 y = ax²의 그래프와 같은 모양의 곡선을 "
        "**포물선**이라고 부릅니다."
    )


st.divider()

st.caption(
    "※ 먼저 자신의 생각을 활동지에 적은 뒤, "
    "접힌 내용을 열어 수학에서 사용하는 용어와 비교해 보세요."
)