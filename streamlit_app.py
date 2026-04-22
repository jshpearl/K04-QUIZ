import streamlit as st

st.set_page_config(page_title="K04 Ôn tập Bài 18", layout="centered")

# --- DANH SÁCH 20 CÂU HỎI ---
if 'questions' not in st.session_state:
    st.session_state.questions = [
        # --- MÔI TRƯỜNG & CON NGƯỜI ---
        {"q": "鱼儿_______水，就像人离不开空气一样。", "options": ["离得开", "离不开", "受不了", "接着"], "a": "离不开"},
        {"q": "每个人都应该关心环境保护，这_______我们生活的环境。", "options": ["关系到", "受不了", "接着", "离得开"], "a": "关系到"},
        {"q": "这种保护环境的方法_______有效，我们还需要再试试。", "options": ["是否", "离得开", "受不了", "接着"], "a": "是否"},
        {"q": "夏天的天气太热了，我真的_______。", "options": ["受得了", "受不了", "离得开", "接着"], "a": "受不了"},
        {"q": "Dịch: Con người không thể rời xa tự nhiên.", "options": ["人类离不开自然。", "人类离得开自然。", "自然离不开人类。", "人类自然离不开。"], "a": "人类离不开自然。"},
        
        # --- KHOA HỌC CÔNG NGHỆ ---
        {"q": "如果没有手机，你_______这样的生活吗？", "options": ["离得开", "离不开", "受不了", "是否"], "a": "离得开"},
        {"q": "先下载这个软件，_______再输入你的名字。", "options": ["接着", "然后", "是否", "既然"], "a": "接着"},
        {"q": "现在的技术非常发达，手机的联系_______有很多种。", "options": ["方式", "方法", "方向", "方案"], "a": "方式"},
        {"q": "电脑又坏了，我真的_______这台旧电脑了。", "options": ["受得了", "受不了", "离得开", "接着"], "a": "受不了"},
        {"q": "Dịch: Tôi muốn biết liệu anh ấy có nhận được tin nhắn không.", "options": ["我想知道他是否收到了短信。", "我想知道他是不是否收到了短信。", "是否我想知道他收到了短信。", "我想知道收到短信是否他。"], "a": "我想知道他是否收到了短信。"},

        # --- NUÔI DẠY CON CÁI ---
        {"q": "父母的爱是孩子成长中_______的。", "options": ["离得开", "离不开", "受不了", "接着"], "a": "离不开"},
        {"q": "教育孩子时，你应该先听听他们的想法，_______再告诉他们对不对。", "options": ["接着", "然后", "是否", "仍然"], "a": "接着"},
        {"q": "孩子每天都哭，邻居们都快_______了。", "options": ["受不了", "受得了", "离不开", "是否"], "a": "受不了"},
        {"q": "现在的父母都很关心孩子_______能养成良好的习惯。", "options": ["是否", "离得开", "受不了", "接着"], "a": "是否"},
        {"q": "Dịch: Mọi người gọi thói quen này là 'Nuanfang'.", "options": ["人们把这个习惯叫作“暖房”。", "这个习惯叫作把“暖房”人们。", "人们把这个习惯叫作了“暖房”。", "把人们这个习惯叫作“暖房”。"], "a": "人们把 questo 习惯叫作“暖房”。"},

        # --- TỔNG HỢP ---
        {"q": "除了这些优点，你_______发现他有别的缺点吗？", "options": ["是否", "受不了", "离不开", "接着"], "a": "是否"},
        {"q": "他刚写完作业，_______又开始预习明天的课。", "options": ["接着", "然后", "是否", "居然"], "a": "接着"},
        {"q": "这种生活_______虽然辛苦，但是很有趣。", "options": ["方法", "方式", "方案", "方便"], "a": "方式"},
        {"q": "这里的噪音太大了，我一分钟也_______。", "options": ["受不了", "受得了", "离不开", "接着"], "a": "受不了"},
        {"q": "Dịch: Liệu kế hoạch này có khả thi không?", "options": ["这个计划是否可行？", "这个计划是不是否可行？", "是否这个计划可行？", "这个计划可行是否？"], "a": "这个计划是否可行？"}
    ]

# --- LOGIC APP ---
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = [None] * 20
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

st.title("🎯 K04 Ôn tập Bài 18")
st.write("Hãy hoàn thành các câu hỏi trắc nghiệm dưới đây để ôn tập các điểm ngữ pháp quan trọng nhé!")
st.divider()

# Hiển thị câu hỏi
for i, item in enumerate(st.session_state.questions):
    st.markdown(f"**Câu {i+1}:** {item['q']}")
    st.session_state.user_answers[i] = st.radio(
        f"Chọn đáp án cho câu {i+1}", 
        item['options'], 
        key=f"q{i}", 
        index=None if st.session_state.user_answers[i] is None else item['options'].index(st.session_state.user_answers[i]),
        label_visibility="collapsed"
    )
    st.write("")

st.divider()

# Nút nộp bài
if st.button("Nộp bài / 提交回答", use_container_width=True):
    if None in st.session_state.user_answers:
        st.warning("Học sinh ơi, còn câu chưa làm kìa! Làm hết mới nộp được nha.")
    else:
        st.session_state.submitted = True

# Hiển thị kết quả
if st.session_state.submitted:
    score = sum(1 for i, q in enumerate(st.session_state.questions) if st.session_state.user_answers[i] == q['a'])
    
    st.header(f"📊 Kết quả bài làm: {score}/20")
    
    if score >= 16:
        st.balloons()
        st.success("Tuyệt vời! Bạn đã nắm vững kiến thức Bài 18! 🌟")
    elif score >= 10:
        st.info("Kết quả khá tốt, nhưng bạn nên xem lại một vài câu sai nhé.")
    else:
        st.error("Bạn cần ôn tập kỹ hơn về cách dùng 是否 và 接着 rồi.")

    st.subheader("🔍 Xem lại chi tiết:")
    for i, q in enumerate(st.session_state.questions):
        user_ans = st.session_state.user_answers[i]
        if user_ans == q['a']:
            st.write(f"✅ **Câu {i+1}**: Đúng! (Đáp án: {q['a']})")
        else:
            st.write(f"❌ **Câu {i+1}**: Sai. (Bạn chọn: {user_ans} | Đáp án đúng: {q['a']})")

    st.markdown("---")
    st.markdown("### ❤️ Cảm ơn bạn đã hoàn thành bài tập này! Chúc bạn học tốt!")
    
    if st.button("Làm lại bài / 重新开始"):
        st.session_state.submitted = False
        st.session_state.user_answers = [None] * 20
        st.rerun()
