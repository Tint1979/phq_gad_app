import streamlit as st

# 제목
st.title("📝 PHQ-9 & GAD-7 심리 검사 웹 앱")
st.write("이 검사는 지난 2주 동안의 정신 건강 상태를 평가합니다.")

# PHQ-9 문항
st.header("📌 PHQ-9 (우울증 선별 검사)")
phq9_questions = [
    "1. 일상적인 활동에 대한 흥미 또는 즐거움이 거의 없음",
    "2. 우울하거나 희망이 없다고 느낌",
    "3. 잠이 들기 어렵거나, 자주 깨거나, 너무 많이 잠",
    "4. 피곤하거나 기운이 거의 없음",
    "5. 식욕이 줄거나 과식함",
    "6. 자신이 실패자라고 느끼거나, 자신과 가족을 실망시켰다고 느낌",
    "7. 신문을 읽거나 TV를 볼 때 집중하기 어려움",
    "8. 너무 느리게 움직이거나, 안절부절 못함",
    "9. 차라리 죽는 것이 낫겠다고 생각하거나 스스로 해치고 싶은 생각을 함"
]

phq9_scores = []
for question in phq9_questions:
    phq9_scores.append(st.slider(question, 0, 3, 0))

phq9_total = sum(phq9_scores)

# PHQ-9 결과 해석
st.subheader(f"📊 PHQ-9 총점: {phq9_total}점")
if phq9_total <= 4:
    st.success("✅ 우울증 없음~경미함")
elif phq9_total <= 9:
    st.warning("⚠️ 가벼운 우울 (경과 관찰 필요)")
elif phq9_total <= 14:
    st.warning("⚠️ 중간 정도 우울 (상담 고려)")
elif phq9_total <= 19:
    st.error("🚨 중증도 높은 우울 (치료 적극 권장)")
else:
    st.error("🚨🚨 심각한 우울 (즉각적 개입 필요)")

if phq9_scores[8] > 0:
    st.error("⚠️ **자살 사고(9번 문항) 감지됨! 추가 상담 권장**")

# GAD-7 문항
st.header("📌 GAD-7 (불안 장애 선별 검사)")
gad7_questions = [
    "1. 신경이 날카롭거나 초조함을 느낌",
    "2. 걱정을 멈추거나 조절하기 어려움",
    "3. 여러 가지 걱정이 너무 많음",
    "4. 긴장을 풀거나 편안하게 쉬기 어려움",
    "5. 너무 안절부절못해서 가만히 앉아있기 어려움",
    "6. 쉽게 짜증이 나거나 신경질이 남",
    "7. 무언가 끔찍한 일이 일어날 것 같다는 두려움을 느낌"
]

gad7_scores = []
for question in gad7_questions:
    gad7_scores.append(st.slider(question, 0, 3, 0))

gad7_total = sum(gad7_scores)

# GAD-7 결과 해석
st.subheader(f"📊 GAD-7 총점: {gad7_total}점")
if gad7_total <= 4:
    st.success("✅ 불안 없음~경미함")
elif gad7_total <= 9:
    st.warning("⚠️ 가벼운 불안 (경과 관찰 필요)")
elif gad7_total <= 14:
    st.warning("⚠️ 중간 정도 불안 (상담 고려)")
else:
    st.error("🚨 심각한 불안 (적극적 치료 필요)")

# 마무리
st.write("📝 이 검사는 자가진단 도구일 뿐이며, 정확한 진단을 위해 전문가 상담을 권장합니다.")