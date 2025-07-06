import streamlit as st
import time
import random
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="성공 타이머", layout="centered")

COMPLIMENTS = [
    "정말 멋져요!", "계속 잘하고 있어요!", "너무 집중하고 있네요!", "대단해요!", "열정이 느껴져요!",
    "훌륭한 노력이에요!", "한 걸음 더 나아갔어요!", "지치지 말고 계속!", "끝까지 힘내요!", "당신은 최고예요!",
    "집중력이 빛나요!", "오늘도 화이팅!", "성공을 향해 달려가고 있어요!", "노력이 헛되지 않아요!", "포기하지 마세요!",
    "굉장해요!", "계속 성장 중!", "자신감을 가지세요!", "매일 발전하고 있어요!", "끈기가 대단해요!",
    "집중하는 모습이 멋져요!", "멋진 하루예요!", "목표에 한 걸음 더!", "성공은 가까워요!", "열심히 하는 당신 최고!",
    "계속 나아가요!", "오늘도 빛나요!", "성취감을 느껴보세요!", "집중하는 모습이 아름다워요!", "힘내세요!",
    "최고예요!", "끝까지 파이팅!", "노력은 배신하지 않아요!", "매일 새로운 도전!", "꿈을 향해 달려가요!",
    "지금 이 순간도 소중해요!", "할 수 있어요!", "자신을 믿으세요!", "큰 성과가 기다리고 있어요!", "멋진 집중력!",
    "한 단계 업그레이드!", "포기하지 않는 모습 감동이에요!", "지금부터 시작!", "자신감 충전 완료!", "끝없는 도전!",
    "꾸준함이 힘이에요!", "오늘도 잘했어요!", "성공을 위한 한 걸음!", "당신은 놀라워요!", "힘차게 전진하세요!"
]

if 'running' not in st.session_state:
    st.session_state.running = False
if 'elapsed_seconds' not in st.session_state:
    st.session_state.elapsed_seconds = 0
if 'compliments_received' not in st.session_state:
    st.session_state.compliments_received = []
if 'last_minute' not in st.session_state:
    st.session_state.last_minute = 0
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

st.title("성공 타이머")

col1, col2, col3 = st.columns(3)
start_btn = col1.button("▶ 시작")
pause_btn = col2.button("⏸ 일시정지")
reset_btn = col3.button("⏹ 정지 및 초기화")

if start_btn and not st.session_state.running:
    st.session_state.running = True
    st.session_state.start_time = time.time() - st.session_state.elapsed_seconds

if pause_btn and st.session_state.running:
    st.session_state.running = False

if reset_btn:
    st.session_state.running = False
    st.session_state.elapsed_seconds = 0
    st.session_state.compliments_received = []
    st.session_state.last_minute = 0

# 1초마다 자동 새로고침 (타이머 흐름 유지)
st_autorefresh(interval=1000, limit=1000, key="refresh")

if st.session_state.running:
    st.session_state.elapsed_seconds = int(time.time() - st.session_state.start_time)

minutes = st.session_state.elapsed_seconds // 60
seconds = st.session_state.elapsed_seconds % 60

if minutes > st.session_state.last_minute and COMPLIMENTS:
    new_compliment = random.choice(COMPLIMENTS)
    st.session_state.compliments_received.append(new_compliment)
    st.session_state.last_minute = minutes

st.markdown(f"<h1 style='text-align:center; font-size:80px;'>⏰ {minutes:02d}분 {seconds:02d}초</h1>", unsafe_allow_html=True)

st.markdown("### 받은 칭찬 메시지")
for c in st.session_state.compliments_received:
    st.markdown(f"- {c}")
