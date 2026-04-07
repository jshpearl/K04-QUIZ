import streamlit as st

# --- CONFIG ---
st.set_page_config(page_title="一起复习第十五课（一）", page_icon="📝")

# --- DATA ---
# Đã lọc sạch: 左右, 鼓掌, 骄傲, 承担
questions = [
    {"q": "爸爸的爸爸叫爷爷，那爷爷管我叫什么？", "options": ["A. 孙子", "B. 儿子", "C. 叔叔", "D. 老师"], "a": "A"},
    {"q": "表扬孩子的时候，____不要太多，否则会给孩子带来压力。", "options": ["A. 一定", "B. 千万", "C. 甚至", "D. 起来"], "a": "B"},
    {"q": "当孩子表现得好时，父母应该____表扬孩子。", "options": ["A. 及时", "B. 甚至", "C. 放弃", "D. 结果"], "a": "A"},
    {"q": "这双鞋穿____非常舒服，一点儿也不累。", "options": ["A. 起来", "B. 出来", "C. 过去", "D. 下来"], "a": "A"},
    {"q": "我不小心把刚才准备好的新闻材料____乱了。", "options": ["A. 弄", "B. 做", "C. 办", "D. 写"], "a": "A"},
    {"q": "哪怕是再小的一件事，只要坚持做，也能____好习惯。", "options": ["A. 养成", "B. 放弃", "C. 解决", "D. 弄坏"], "a": "A"},
    {"q": "听到那个笑话，大家都忍不住大笑____了。\n\n*(忍不住 rěn bú zhù: không nhịn được)*", "options": ["A. 起来", "B. 出来", "C. 过去", "D. 下来"], "a": "A"},
    {"q": "明天有很重要的考试，你____别迟到了。", "options": ["A. 一定", "B. 弄", "C. 起来", "D. 千万"], "a": "D"},
    {"q": "每个人在成长的____中，都会遇到很多困难。", "options": ["A. 过程", "B. 结果", "C. 效果", "D. 责任"], "a": "A"},
    {"q": "看到这张老照片，我突然____了他是谁。", "options": ["A. 想起来", "B. 想出来", "C. 弄出来", "D. 看起来"], "a": "A"},
    {"q": "这种学习方法对提高汉语水平有明显的____。", "options": ["A. 习惯", "B. 勇气", "C. 效果", "D. 孙子"], "a": "C"},
    {"q": "由于他不仅聪明，____非常努力，所以进步很快。", "options": ["A. 甚至", "B. 而且", "C. 起来", "D. 千万"], "a": "B"},
    {"q": "这台电脑刚买不久，怎么就被你____坏了？", "options": ["A. 做", "B. 弄", "C. 办", "D. 拿"], "a": "B"},
    {"q": "我刚才太____了，竟然走错了房间。", "options": ["A. 糊涂", "B. 清楚", "C. 认真", "D. 热情"], "a": "A"},
    {"q": "____你连这么简单的问题都不会？", "options": ["A. 难道", "B. 甚至", "C. 结果", "D. 顺便"], "a": "A"},
    {"q": "在酒店，问路时用“____”更礼貌。\n\n*(礼貌 lǐmào: lịch sự/lễ phép)*", "options": ["A. 厕所", "B. 洗手间", "C. 厨房", "D. 卧室"], "a": "B"},
    {"q": "这个任务虽然很难，但我____会想办法完成的。", "options": ["A. 一定", "B. 千万", "C. 起来", "D. 顺便"], "a": "A"},
    {"q": "只有经历了努力的____，你才能体会到成功的快乐。", "options": ["A. 养成", "B. 过程", "C. 解决", "D. 鼓励"], "a": "B"},
    {"q": "这个问题你还没____明白吗？需要我再讲一遍吗？", "options": ["A. 起来", "B. 弄", "C. 千万", "D. 一定"], "a": "B"},
    {"q": "天气冷了，快把那件大衣穿____吧。", "options": ["A. 起来", "B. 出来", "C. 下下来", "D. 过去"], "a": "A"},
    {"q": "不管____是什么，你都已经努力过了。", "options": ["A. 结果", "B. 过程", "C. 效果", "D. 习惯"], "a": "A"},
    {"q": "下班的时候，请____把垃圾带走。", "options": ["A. 顺便", "B. 难道", "C. 甚至", "D. 养成"], "a": "A"},
    {"q": "这篇文章他不仅读了，____还能全部背下来。", "options": ["A. 甚至", "B. 难道", "C. 千万", "D. 起来"], "a": "A"},
    {"q": "当孩子表现好时，父母的一句____非常重要。", "options": ["A. 鼓励", "B. 养成", "C. 过程", "D. 糊涂"], "a": "A"},
    {"q": "你应该有____去面对失败，不要轻易放弃。\n\n*(轻易 qīngyì: dễ dàng/tùy tiện)*", "options": ["A. 勇气", "B. 孙子", "C. 过程", "D. 结果"], "a": "A"},
    {"q": "如果你不尝试，____失败的机会都没有。", "options": ["A. 甚至", "B. 难道", "C. 千万", "D. 起来"], "a": "A"},
    {"q": "成功需要努力，你____不能想着走捷径。\n\n*(捷径 jiéjìng: đường tắt)*", "options": ["A. 千万", "B. 起来", "C. 弄", "D. 顺便"], "a": "A"},
    {"q": "我不小心把刚才买的药____丢了。", "options": ["A. 弄", "B. 办", "C. 做", "D. 拿"], "a": "A"},
    {"q": "既然是由于你的原因，你就应该承担____。\n\n*(承担 chéngdān: gánh vác/đảm nhận)*", "options": ["A. 责任", "B. 效果", "C. 结果", "D. 过程"], "a": "A"},
    {"q": "教育孩子不仅需要爱心，更需要帮他们____良好的习惯。", "options": ["A. 养成", "B. 放弃", "C. 甚至", "D. 弄"], "a": "A"}
]

# --- SESSION STATE ---
if 'idx' not in st.session_state:
    st.session_state.idx = 0
    st.session_state.answers = [None] * len(questions)
    st.session_state.done = False

# --- UI ---
st.title("一起复习第十五课（一）")
st.write("Ôn tập từ vựng (3 bài khóa đầu) & Ngữ pháp (起来、弄、千万)")

if not st.session_state.done:
    q = questions[st.session_state.idx]
    st.subheader(f"Câu {st.session_state.idx + 1}/{len(questions)}")
    st.info(q['q'])
    
    # User choice
    choice = st.radio("Chọn đáp án:", q['options'], key=f"radio_{st.session_state.idx}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.idx > 0:
            if st.button("⬅️ Back"):
                st.session_state.idx -= 1
                st.rerun()
    with col2:
        label = "Finish 🏁" if st.session_state.idx == len(questions)-1 else "Next ➡️"
        if st.button(label):
            st.session_state.answers[st.session_state.idx] = choice[0]
            if st.session_state.idx < len(questions)-1:
                st.session_state.idx += 1
                st.rerun()
            else:
                st.session_state.done = True
                st.rerun()
else:
    # --- RESULT ---
    st.balloons()
    score = sum(1 for i, q in enumerate(questions) if st.session_state.answers[i] == q['a'])
    st.header(f"FINISHED! 🏆 Score: {score}/{len(questions)}")
    
    tab1, tab2 = st.tabs(["📊 Review", "🔄 Redo"])
    with tab1:
        for i, q in enumerate(questions):
            is_correct = st.session_state.answers[i] == q['a']
            status = "✅ CORRECT" if is_correct else f"❌ INCORRECT (Correct: {q['a']})"
            with st.expander(f"Câu {i+1}: {status}"):
                st.write(q['q'])
                st.write(f"Your answer: {st.session_state.answers[i]}")
    with tab2:
        if st.button("Làm lại từ đầu (Redo)"):
            st.session_state.idx = 0
            st.session_state.answers = [None] * len(questions)
            st.session_state.done = False
            st.rerun()
