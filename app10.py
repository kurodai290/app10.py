import streamlit as st
import random

# ページ設定
st.set_page_config(page_title="剣道二段 学科試験10問ドリル", layout="centered")

# --- 剣道二段：全30問のデータベース ---
if "all_questions" not in st.session_state:
    st.session_state.all_questions = [
        {"id": 1, "title": "試合の目的", "text": "試合は技能の（　）と人間性の発露にある。", "options": ["向上", "改善", "維持"], "correct": "向上"},
        {"id": 2, "title": "試合の目的", "text": "勝つための周到な（　）と節制ある生活が大切である。", "options": ["準備", "計画", "練習"], "correct": "準備"},
        {"id": 3, "title": "試合の目的", "text": "勝っておごらず負けて（　）になることなく...", "options": ["卑屈", "傲慢", "自暴自棄"], "correct": "卑屈"},
        {"id": 4, "title": "試合の目的", "text": "負けた試合を（　）して、自己の欠点を矯正すべきである。", "options": ["反省", "忘却", "自慢"], "correct": "反省"},
        {"id": 5, "title": "足の運び方", "text": "打突には（　）と言うことを第一に心がける。", "options": ["引きつける", "踏み切る", "止まる"], "correct": "引きつける"},
        {"id": 6, "title": "足の運び方", "text": "一打突にはかならず両足共に（　）又は踏み切ること。", "options": ["引きつける", "浮かせる", "揃える"], "correct": "引きつける"},
        {"id": 7, "title": "足の運び方", "text": "足の進め方は後足で（　）前足を進めるのが常法。", "options": ["蹴って", "引いて", "浮かせて"], "correct": "蹴って"},
        {"id": 8, "title": "切り返し", "text": "切り返しは（　）の動きを巧妙にする効果がある。", "options": ["竹刀", "身体", "足"], "correct": "竹刀"},
        {"id": 9, "title": "切り返し", "text": "間合を（　）に知ることができるようになる。", "options": ["正確", "適当", "自在"], "correct": "正確"},
        {"id": 10, "title": "切り返し", "text": "（　）一致の技を修錬するものである。", "options": ["気剣体", "心技体", "心身"], "correct": "気剣体"},
        {"id": 11, "title": "手の内", "text": "手の内とは（　）や締め方のことである。", "options": ["握り方", "振り方", "構え方"], "correct": "握り方"},
        {"id": 12, "title": "手の内", "text": "相手の打突を（　）、切り落として攻撃に繋げる。", "options": ["応じ", "避け", "無視し"], "correct": "応じ"},
        {"id": 13, "title": "手の内", "text": "その（　）を手の内という。", "options": ["作用", "形", "動き"], "correct": "作用"},
        {"id": 14, "title": "一足一刀の間合", "text": "一歩（　）、相手を打突することができる距離。", "options": ["踏み込めば", "退けば", "止まれば"], "correct": "踏み込めば"},
        {"id": 15, "title": "一足一刀の間合", "text": "いわゆる（　）に強く、守りにも強い間合。", "options": ["攻め", "足", "心"], "correct": "攻め"},
        {"id": 16, "title": "引掛け", "text": "引掛けとは、打突後に（　）を示さず構えを解くこと。", "options": ["残心", "気合", "威力"], "correct": "残心"},
        {"id": 17, "title": "引掛け", "text": "気勢を（　）、試合を中止する行為である。", "options": ["削ぎ", "高め", "維持し"], "correct": "削ぎ"},
        {"id": 18, "title": "日本剣道形", "text": "剣道形の（　）な技、即ち抜き技などを修練する。", "options": ["理合", "基本", "応用"], "correct": "理合"},
        {"id": 19, "title": "日本剣道形", "text": "剣道形を（　）に応用し、変化活用できるようにする。", "options": ["実戦", "演武", "審査"], "correct": "実戦"},
        {"id": 20, "title": "剣道形二本目", "text": "打太刀、仕太刀（　）でお互いに右足から進む。", "options": ["相中段", "相下段", "相上段"], "correct": "相中段"},
        {"id": 21, "title": "剣道形二本目", "text": "機を見て仕太刀の（　）を打つ。", "options": ["右小手", "面", "胴"], "correct": "右小手"},
        {"id": 22, "title": "剣道形二本目", "text": "剣先を下げて打太刀の刀の下で（　）をえがく。", "options": ["半円", "円", "直線"], "correct": "半円"},
        {"id": 23, "title": "剣道形二本目", "text": "打太刀は（　）から、仕太刀は右足から退く。", "options": ["左足", "右足", "両足"], "correct": "左足"},
        {"id": 24, "title": "有効打突", "text": "充実した気勢、適正な姿勢をもって（　）で打つ。", "options": ["物打ち", "鍔", "先革"], "correct": "物打ち"},
        {"id": 25, "title": "有効打突", "text": "打突部位を（　）正しく打突すること。", "options": ["刃筋", "角度", "音"], "correct": "刃筋"},
        {"id": 26, "title": "残心", "text": "打突した後、相手の（　）に備える。 ", "options": ["反撃", "移動", "休息"], "correct": "反撃"},
        {"id": 27, "title": "礼儀", "text": "道場内では常に（　）を尊ぶ。", "options": ["礼節", "勝敗", "技術"], "correct": "礼節"},
        {"id": 28, "title": "三殺法", "text": "相手の（　）を殺す、技を殺す、気を殺す。", "options": ["剣", "足", "目"], "correct": "剣"},
        {"id": 29, "title": "四戒", "text": "驚・（　）・疑・惑の四つの心。", "options": ["惧", "恐", "怒"], "correct": "惧"},
        {"id": 30, "title": "蹲踞", "text": "蹲踞は相手に対して（　）を表す姿勢である。", "options": ["敬意", "敵意", "注意"], "correct": "敬意"},
    ]

# --- セッション状態初期化 ---
if "current_test" not in st.session_state:
    st.session_state.current_test = random.sample(st.session_state.all_questions, 10)
if "page_idx" not in st.session_state:
    st.session_state.page_idx = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "show_results" not in st.session_state:
    st.session_state.show_results = False

def restart_test():
    st.session_state.current_test = random.sample(st.session_state.all_questions, 10)
    st.session_state.page_idx = 0
    st.session_state.user_answers = {}
    st.session_state.show_results = False
    st.rerun()

# --- メインロジック ---
st.title("🛡️ 剣道二段 学科試験（10問ランダム）")

if not st.session_state.show_results:
    q = st.session_state.current_test[st.session_state.page_idx]
    
    st.progress((st.session_state.page_idx) / 10)
    st.subheader(f"第 {st.session_state.page_idx + 1} 問：{q['title']}")
    st.info(q['text'])
    
    ans = st.radio("正しい言葉を選んでください", q['options'], key=f"q_{q['id']}")
    
    col1, col2 = st.columns(2)
    if st.session_state.page_idx < 9:
        if col1.button("次へ進む"):
            st.session_state.user_answers[q['id']] = ans
            st.session_state.page_idx += 1
            st.rerun()
    else:
        if col1.button("採点する"):
            st.session_state.user_answers[q['id']] = ans
            st.session_state.show_results = True
            st.rerun()
            
    if col2.button("中断して採点"):
        st.session_state.show_results = True
        st.rerun()

else:
    st.header("🏁 採点結果")
    score = 0
    for q in st.session_state.current_test:
        u_ans = st.session_state.user_answers.get(q['id'], "未回答")
        correct = q['correct']
        is_correct = (u_ans == correct)
        if is_correct: score += 1
        
        with st.expander(f"{q['title']}：{'✅' if is_correct else '❌'}"):
            st.write(f"問題: {q['text']}")
            st.write(f"あなたの回答: {u_ans}")
            st.write(f"正解: {correct}")

    st.subheader(f"得点: {score} / 10")
    if st.button("新しい10問でやり直す"):
        restart_test()
