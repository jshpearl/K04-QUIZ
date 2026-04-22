import streamlit as st

st.set_page_config(page_title="HSK4 - Bài 18 Quiz", layout="centered")

# --- DANH SÁCH 30 CÂU HỎI ---
if 'questions' not in st.session_state:
    st.session_state.questions = [
        # --- MÔI TRƯỜNG (ENVIRONMENT) ---
        {"q": "现在的环境污染问题越来越严重，人类已经_______大自然了。", "options": ["离得开", "离不开", "受不了", "接着"], "a": "离不开", "type": "fill"},
        {"q": "保护地球_______每个人的责任，这还需要讨论吗？", "options": ["是否", "是不是", "受不了", "接着"], "a": "是否", "type": "fill"},
        {"q": "夏天的气温一年比一年高，真是让人_______。", "options": ["受得住", "受不了", "离不开", "接着"], "a": "受不了", "type": "fill"},
        {"q": "我们应该先垃圾分类，_______把可回收物送到工厂。", "options": ["然后", "接着", "是否", "既然"], "a": "接着", "type": "fill"},
        {"q": "Dịch: Liệu phương pháp bảo vệ môi trường này có hiệu quả không?", "options": ["这个保护环境方法是否有效？", "是否这个保护环境方法有效？", "这个保护环境方法是不是否有效？", "这个保护环境方法有效是否？"], "a": "这个保护环境方法是否有效？", "type": "trans"},
        
        # --- KHOA HỌC CÔNG NGHỆ (TECH) ---
        {"q": "如果没有互联网，现代人的生活还能_______吗？", "options": ["离得开", "离不开", "是否", "仍然"], "a": "离得开", "type": "fill"},
        {"q": "科技的发展_______能给人类带来真正的幸福，是一个值得思考的问题。", "options": ["是否", "离不开", "受不了", "接着"], "a": "是否", "type": "fill"},
        {"q": "这个手机软件总是在关键时刻卡住，我真是_______！", "options": ["受不了", "受得了", "离不开", "接着"], "a": "受不了", "type": "fill"},
        {"q": "请先打开电脑，_______输入密码登录系统。", "options": ["接着", "然后", "是否", "依然"], "a": "接着", "type": "fill"},
        {"q": "Dịch: Con người không thể rời xa các thiết bị công nghệ.", "options": ["人类离不开科技设备。", "人类离得开科技设备。", "科技设备离不开人类。", "科技设备人类离得开。"], "a": "人类离不开科技设备。", "type": "trans"},

        # --- NUÔI DẠY CON CÁI (PARENTING) ---
        {"q": "无论工作多忙，父母都_______孩子的陪伴。", "options": ["离得开", "离不开", "是否", "受不了"], "a": "离不开", "type": "fill"},
        {"q": "教育孩子时，最重要的看你_______愿意耐心地倾听。", "options": ["是否", "受不了", "接着", "离得开"], "a": "是否", "type": "fill"},
        {"q": "现在的孩子压力太大，有时候连周末都要补习，真让人_______。", "options": ["受不了", "受得了", "接着", "离不开"], "a": "受不了", "type": "fill"},
        {"q": "妈妈先批评了孩子，_______又耐心地讲了道理。", "options": ["接着", "然后", "是否", "由于"], "a": "接着", "type": "fill"},
        {"q": "Dịch: Cách giáo dục này được gọi là 'giáo dục gia đình'.", "options": ["这种教育方式把叫作“家庭教育”。", "人们把这种教育方式叫作“家庭教育”。", "这种教育方式叫作把“家庭教育”。", "把这种教育方式人们叫作“家庭教育”。"], "a": "人们把这种教育方式叫作“家庭教育”。", "type": "trans"},

        # --- CON NGƯỜI & ĐỜI SỐNG (HUMANS) ---
        {"q": "一个人_______能获得成功，主要看他是否努力。", "options": ["是否", "离不开", "接着", "仍然"], "a": "是否", "type": "fill"},
        {"q": "他刚喝完药，_______又躺下休息了。", "options": ["接着", "然后", "是否", "既然"], "a": "接着", "type": "fill"},
        {"q": "这种奇特的风俗_______还存在，我不太确定。", "options": ["是否", "受不了", "离不开", "接着"], "a": "是否", "type": "fill"},
        {"q": "现代社会，工作和生活是_______的。", "options": ["离得开", "离不开", "受不了", "接着"], "a": "离不开", "type": "fill"},
        {"q": "Dịch: Tôi thực sự không chịu nổi tiếng ồn của hàng xóm.", "options": ["我真的受不了邻居的噪音了。", "邻居的噪音真的受不了我了。", "我受得住邻居真的噪音了。", "真的我邻居受不了噪音了。"], "a": "我真的受不了邻居的噪音了。", "type": "trans"},
        
        {"q": "这种联系_______在现代社会非常普及。", "options": ["方法", "方式", "方向", "方案"], "a": "方式", "type": "fill"},
        {"q": "那个人的脾气太怪了，大家都对他_______。", "options": ["受不了", "受得了", "离不开", "是否"], "a": "受不了", "type": "fill"},
        {"q": "科学研究_______严谨的态度。", "options": ["离得开", "离不开", "受不了", "接着"], "a": "离不开", "type": "fill"},
        {"q": "他在黑板上写了一个字，_______又画了一个圆。", "options": ["接着", "然后", "是否", "甚至"], "a": "接着", "type": "fill"},
        {"q": "Dịch: Bạn có thể sống thiếu (rời xa) máy tính một ngày không?", "options": ["你一天离不开电脑吗？", "你一天离得开电脑吗？", "电脑一天离得开你吗？", "你离得开电脑一天吗？"], "a": "你离得开电脑吗？", "type": "trans"},
        
        {"q": "婚姻_______幸福，不在于有没有“夫妻相”。", "options": ["是否", "受不了", "接着", "离得开"], "a": "是否", "type": "fill"},
        {"q": "每天都要在公车上挤一个小时，我实在_______。", "options": ["受不了", "离不开", "接着", "是否"], "a": "受不了", "type": "fill"},
        {"q": "他先看了看地图，_______指向了前方。", "options": ["接着", "然后", "是否", "仍然"], "a": "接着", "type": "fill"},
        {"q": "鱼儿_______水，就像人类离不开空气。", "options": ["离不开", "离得开", "受不了", "是否"], "a": "离不开", "type": "fill"},
        {"q": "Dịch: Theo tin tức mới nhất, thời tiết tuần sau sẽ rất đẹp.", "options": ["据最新消息，下周天气会很好。", "根据最新消息，下周天气会很好。", "据最新消息，下周天气会很好。（A&B đều đúng）", "据/根据都没有这个说法。"], "a": "据最新消息，下周天气会很好。（A&B đều đúng）", "type": "trans"}
    ]

# --- LOGIC APP ---
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = [None] * 30
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

st.title("🎓 Luyện tập Tiếng Trung Bài 18 - HSK 4")
st.write("Chủ đề: Môi trường, Công nghệ, Con người & Nuôi dạy con cái.")
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
        st.warning("Ông ơi, học sinh còn mấy câu chưa làm kìa! Làm hết mới nộp được nha.")
    else:
        st.session_state.submitted = True

# Hiển thị kết quả
if st.session_state.submitted:
    score = sum(1 for i, q in enumerate(st.session_state.questions) if st.session_state.user_answers[i] == q['a'])
    
    st.header(f"📊 Kết quả: {score}/30")
    
    if score >= 25:
        st.balloons()
        st.success("Quá đỉnh! PhD có khác, dạy học sinh thế này thì ai cũng giỏi! 🌟")
    elif score >= 15:
        st.info("Cũng ổn đấy, nhưng nhắc học sinh xem lại mấy chỗ '接着' với '然后' nha.")
    else:
        st.error("Học sinh cần cố gắng nhiều rồi. Ông cho tụi nó làm lại đi!")

    st.subheader("📝 Chi tiết bài làm:")
    for i, q in enumerate(st.session_state.questions):
        user_ans = st.session_state.user_answers[i]
        if user_ans == q['a']:
            st.write(f"✅ Câu {i+1}: Đúng! (Đáp án: {q['a']})")
        else:
            st.write(f"❌ Câu {i+1}: Sai. (Bạn chọn: {user_ans} | Đáp án đúng: {q['a']})")

    st.markdown("---")
    st.markdown("### ❤️ Cảm ơn bạn đã hoàn thành bài tập này! Chúc bạn tiến bộ mỗi ngày!")
    
    if st.button("Làm lại bài / 重新开始"):
        st.session_state.submitted = False
        st.session_state.user_answers = [None] * 30
        st.rerun()
