import discord
from discord.ext import commands
import os
import time

client = commands.Bot(command_prefix='/', intents=discord.Intents.all())

j = ('\n')
s = "===================================================="
g = "공 정 재 료"
m = "마 감 재 료"
ga = "개 조 식"

item1_name = "켈틱 스로잉 스타"
item1_s_name = "켈스스"
item1_i1 = "여신의 무기의 외형적 특징을 참고해 만든 수리검 끝을 매우 예리하게 다듬어 적에게 던져 명중 시 매우 치명적인 타격을 입힐 수 있다."
item1_i2 = "공격력 7~42"
item1_i3 = "부상률 5~100%"
item1_i4 = "크리티컬 18%"
item1_i5 = "밸런스 30%"
item1_i6 = "내구력 20/20"
item1_i7 = "추가옵션 없음"
item1_i8 = "은괴 2개 / 미스릴괴 8개 / 균열된 검은 금속 3개 / 냉혹함의 징표 1개"
item1_i9 = "벼린 무기조각 6개 / 대못 4개 / 불완전한 봉인의 엠블럼 4개"
item1_i10 = "날 벼리기5 - 날 벼리기1 - 날 벼리기1 - 날 벼리기4"
item1_i11 = "장인개조 (아이데른. 풀맥 38)"
item1_i12 = "보석개조 (안드라스) > 다이아몬드 1cm, 스타사파이어 1cm, 스피넬 1cm"

item2_name = "켈틱 로열 나이트 소드"
item2_s_name = "켈로나"
item2_i1 = "여신이 사용했다고 전해지는 무기를 복원해 만든 한손검. 한손검 특유의 가벼움으로 날렵한 공격이 가능하면서도 높은 파괴력을 가지고 있는 점이 인상적이다. 두 자루를 쌍으로 들었을 때 이 무기의 진정한 위력을 체감할 수 있다고 한다."
item2_i2 = "공격력 20~46"
item2_i3 = "부상률 0~0%"
item2_i4 = "크리티컬 14%"
item2_i5 = "밸런스 60%"
item2_i6 = "내구력 15/15"
item2_i7 = "추가옵션 없음"
item2_i8 = "은괴 2개 / 미스릴괴 8개 / 빛을 잃어버린 금속 파편 1개 / 어둠에 물든 칼날의 파편 1개"
item2_i9 = "끊어진 봉인의 사슬 4개, 대못 4개, 질긴끈 2개 망가진 엠블럼 6개"
item2_i10 = "켈틱 로열 나이트 소드 전용 개조 - 검신 다듬기2 - 검신 다듬기3 - 검신 다듬기4"
item2_i11 = "장인개조 (네리스, 레이널드 등. 체력 / 행운 / 스태미나 / 생명력) or 검신 다듬기 5"
item2_i12 = "보석개조 (네리스, 레이널드 등) > 다이아몬드 1cm, 루비 1cm, 토파즈 1cm"

item3_name = "켈틱 로열 크로스보우"
item3_s_name = "켈로크"
item3_i1 = "여신의 위용을 기리며 만들었다고 하는 석궁. 아름답고 유연한 몸체로 강력한 힘을 발휘한다. 적을 꿰뚫는 단호함이 분노한 여신을 연상시킨다."
item3_i2 = "공격력 25~61"
item3_i3 = "부상률 0~100%"
item3_i4 = "크리티컬 40%"
item3_i5 = "밸런스 20%"
item3_i6 = "내구력 15/15"
item3_i7 = "피어싱 3레벨"
item3_i8 = "목공"
item3_i9 = "최고급 나무장작 8개, 빛나는 질긴 끈 3개, 빛을 잃어버린 금속의 파편 2개, 잊혀진 마법사의 보석 1개, 단단한 괴수의 뿔 5개"
item3_i10 = "니커식 석궁강화 - 활줄 강화1 - 활줄 강화3 (네리스, 니커)"
item3_i11 = "퍼거스식 석궁개조 - 날카로운 마무리 (퍼거스)"
item3_i12 = "보석개조 (아란웬, 아이데른) > 가넷 1cm, 아쿠아마린 2cm, 재스퍼 4cm"

item4_name = "켈틱 하울링 체인 블레이드"
item4_s_name = "켈하체"
item4_i1 = "여신의 무기의 외형적 특징을 참고해 만든 체인 블레이드. 강도를 극도로 높인 체인에 섬뜩하게 다듬어진 칼날을 결합하여 빼어난 공격력을 발휘한다."
item4_i2 = "공격력 70~91"
item4_i3 = "부상률 10~25%"
item4_i4 = "크리티컬 40%"
item4_i5 = "밸런스 50%"
item4_i6 = "내구력 15/15"
item4_i7 = "추가옵션 없음"
item4_i8 = "은괴 2개, 미스릴괴 8개, 균열된 검은 금속 3개, 어둠이 깃든 칼날 조각 1개"
item4_i9 = "질긴끈 4개, 의지가 잠든 룬스톤 6개, 불완전한 봉인의 엠블럼 4개"
item4_i10 = "날끝갈기 - 칼갈기1 - 칼갈기2 - 칼갈기3"
item4_i11 = "장인개조 (아이데른. 맥뎀 0~25 / 행운 0~30)"
item4_i12 = "보석개조 (그라나트, 네리스 등) > 다이아몬드 1cm, 에메랄드 1cm, 루비 1cm"

item5_name = "켈틱 워 해머"
item5_s_name = "-"
item5_i1 = "여신의 무기의 외형적 특징을 참고해 만든 전투용 한손 둔기. 기존의 일반 해머와 차별되는 공격력은 이 무기가 단순한 양산형만은 아니라는 것을 말해주고 있다."
item5_i2 = "공격력 7~55"
item5_i3 = "부상률 0~5%"
item5_i4 = "크리티컬 17%"
item5_i5 = "밸런스 39%"
item5_i6 = "내구력 15/15"
item5_i7 = "추가옵션 없음"
item5_i8 = "철괴 4개, 은괴 3개, 미스릴괴 6개"
item5_i9 = "매듭끈 2개, 대못 6개, 망가진 엠블럼 1개"
item5_i10 = "-"
item5_i11 = "-"
item5_i12 = "-"

item6_name = "켈틱 배틀 액스"
item6_s_name = "-"
item6_i1 = "여신이 사용했던 전투용 한 손 도끼를 본뜬 무기. 외형 만이 아니라 높은 공격력 또한 여신의 무기의 특징을 최대한 살려내고 있다고 할 수 있다."
item6_i2 = "공격력 13~45"
item6_i3 = "부상률 0~0%"
item6_i4 = "크리티컬 27%"
item6_i5 = "밸런스 35%"
item6_i6 = "내구력 19/19"
item6_i7 = "추가옵션 없음"
item6_i8 = "철괴 4개, 은괴3개, 미스릴괴 6개"
item6_i9 = "고급 가죽 2개, 매듭끈 1개, 대못 2개, 망가진 엠블럼 1개"
item6_i10 = "-"
item6_i11 = "-"
item6_i12 = "-"

item7_name = "켈틱 워리어 해머"
item7_s_name = "-"
item7_i1 = "여신의 무기의 외형적 특징과 함께 그 파괴력까지 최대한 본떠 만든 전투용 양손 해머. 인간과 엘프도 휘두를 수 있는 손쉬운 사용성도 장점이다."
item7_i2 = "공격력 18~64"
item7_i3 = "부상률 6~10%"
item7_i4 = "크리티컬 27%"
item7_i5 = "밸런스 19%"
item7_i6 = "내구력 17/17"
item7_i7 = "추가옵션 없음"
item7_i8 = "철괴 7개, 은괴 4개, 미스릴괴 9개"
item7_i9 = "매듭끈 3개, 대못 8개, 망가진 커다란 엠블럼 1개"
item7_i10 = "-"
item7_i11 = "-"
item7_i12 = "-"

item8_name = "켈틱 워리어 액스"
item8_s_name = "-"
item8_i1 = "여신의 무기를 본떠 만든 무기. 거대하고 예리한 날이 만들어내는 파괴력과 함께 인간과 엘프도 휘두를 수 있다는 특별함이 이 양손 도끼를 돋보이게 하는 차별점이다."
item8_i2 = "공격력 8~75"
item8_i3 = "부상률 0~0%"
item8_i4 = "크리티컬 23%"
item8_i5 = "밸런스 42%"
item8_i6 = "내구력 12/12"
item8_i7 = "추가옵션 없음"
item8_i8 = "철괴 7개, 은괴 4개, 미스릴괴 9개"
item8_i9 = "고급 가죽 4개, 매듭끈 2개, 대못 2개, 망가진 커다란 엠블럼 1개"
item8_i10 = "-"
item8_i11 = "-"
item8_i12 = "-"

item9_name = "켈틱 로열 워 해머"
item9_s_name = "-"
item9_i1 = "여신의 무기를 복원해 만든 전투용 한 손 둔기. 높은 파괴력도 인상적이지만 해머치고는 비교적 안정정인 공격력을 낼 수 있다는 점이 이 무기의 장점이다."
item9_i2 = "공격력 13~62"
item9_i3 = "부상률 0~2%"
item9_i4 = "크리티컬 18%"
item9_i5 = "밸런스 39%"
item9_i6 = "내구력 20/20"
item9_i7 = "추가옵션 없음"
item9_i8 = "은괴 2개, 미스릴괴 8개, 빛을 잃어버린 금속 파편 3개, 매우 거대한 갑옷의 조각 1개"
item9_i9 = "질긴 끈 2개, 대못 8개, 끊어진 봉인의 사슬 5개, 망가진 엠블럼 5개"
item9_i10 = "켈틱 로열 워 해머 전용 개조 - 담금질2 - 담금질3 - 담금질4"
item9_i11 = "개조 (아이데른. 담금질5)"
item9_i12 = "보석개조1 (아이데른) > 스타사파이어 4cm, 루비 2cm, 스피넬 1cm"

item10_name = "켈틱 로열 배틀 액스"
item10_s_name = "-"
item10_i1 = "여신이 사용했다고 전해지는 무기를 복원한 강력한 전투용 한 손 도끼. 무게와 날카로움의 조화에서 오는 한 방의 파괴력이 다양한 전투 상황에서 빛을 발한다."
item10_i2 = "공격력 18~53"
item10_i3 = "부상률 1~3%"
item10_i4 = "크리티컬 25%"
item10_i5 = "밸런스 35%"
item10_i6 = "내구력 21/21"
item10_i7 = "추가옵션 없음"
item10_i8 = "은괴 2개, 미스릴괴 8개, 빛을 잃어버린 금속 파편 3개, 날카롭게 깨진 괴물의 핵 1개"
item10_i9 = "최고급 가죽 2개, 대못 4개, 끊어진 봉인의 사슬 6개, 망가진 엠블럼 4개"
item10_i10 = "켈틱 로열 배틀 액스 전용 개조 - 담금질2 - 담금질3 - 담금질 4"
item10_i11 = "개조 (아이데른, 컬룸. 엔포리움 켈틱 로열 배틀 액스 특수 개조)"
item10_i12 = "보석개조1 (아이데른) > 재스퍼 4cm, 스타사파이어 2cm, 스피넬 1cm"

item11_name = "켈틱 로열 워리어 해머"
item11_s_name = "-"
item11_i1 = "여신이 적들을 심판하기 위해 휘둘렀다는 양손 둔기를 복원해 만든 무기. 높은 파괴력에 걸맞는 육중한 외양과 달리 인간과 엘프도 휘두를 수 있을 정도로 손쉬운 사용성을 자랑한다."
item11_i2 = "공격력 27~72"
item11_i3 = "부상률 2~4%"
item11_i4 = "크리티컬 28%"
item11_i5 = "밸런스 19%"
item11_i6 = "내구력 22/22"
item11_i7 = "추가옵션 없음"
item11_i8 = "은괴 4개, 미스릴괴 10개, 빛을 잃어버린 금속 파편 5개, 매우 거대한 갑옷의 조각 2개"
item11_i9 = "질긴 끈 5개, 대못 10개, 녹슨 봉인의 사슬 5개, 망가진 커다란 엠블럼 5개"
item11_i10 = "켈틱 로열 워리어 해머 전용 개조 - 경량화 - 담금질3 - 담금질4"
item11_i11 = "개조 (타우네스. 담금질5 또는 켈틱 로열 워리어 해머 특수 개조1 or 2)"
item11_i12 = "보석개조 (타우네스) > 루비 4cm, 스타사파이어 2cm, 스피넬 1cm"

item12_name = "켈틱 로열 워리어 액스"
item12_s_name = "-"
item12_i1 = "여신의 무기를 복원한 강력하고 거대한 양손 도끼. 거대한 덩치와 예리한 날에서 뿜어져 나오는 파괴력으로 적에게 치명적인 대미지를 입힌다. 특히 인간과 엘프도 휘두를 수 있다는 점은 이 무기를 돋보이게 하는 최고의 장점일 것이다."
item12_i2 = "공격력 14~85"
item12_i3 = "부상률 1~3%"
item12_i4 = "크리티컬 20%"
item12_i5 = "밸런스 40%"
item12_i6 = "내구력 15/15"
item12_i7 = "추가옵션 없음"
item12_i8 = "은괴 4개, 미스릴괴 10개, 빛을 잃어버린 금속 파편 5개, 날카롭게 깨진 괴물의 핵 2개"
item12_i9 = "최고급 가죽 5개, 대못 4개, 녹슨 봉인의 사슬 6개, 망가진 커다란 엠블럼 4개"
item12_i10 = "개조 (타우네스. 담금질5 또는 켈틱 로열 워리어 액스 특수 개조1 or 2)"
item12_i11 = "item12_i11"
item12_i12 = "보석개조1 (타우네스) > 스타사파이어 4cm, 루비 2cm, 가넷 1cm"

item13_name = "켈틱 트라이볼트 원드"
item13_s_name = "켈트볼"
item13_i1 = "여신의 지혜가 녹아들어 있다고 전해지는 원드. 파이어, 라이트닝, 아이스의 세 속성이 혼재되어 있다. 일부 마법을 사용할 수 없지만, 원드 하나로 세 속성의 볼트 마법 효율을 모두 끌어올릴 수 있는 극단적인 개조가 가능하다. 원드를 손에 쥐면 몸의 마나와 공명하게 되어 달리면서도 메디테이션을 할 수 있다."
item13_i2 = "공격력 5~12"
item13_i3 = "부상률 20~40%"
item13_i4 = "크리티컬 33%"
item13_i5 = "밸런스 50%"
item13_i6 = "내구력 20/20"
item13_i7 = "마법 공격력 5~30+ / 내구력 0~40+"
item13_i8 = "매직 크래프트"
item13_i9 = "마력이 깃든 나무장작 3개, 온전한 실리엔 10개, 뮤턴트 2개, 망가진 고리형 구조체 2개, 봉인의 검은 금속 3개, 잊혀진 마법사의 보석 6개"
item13_i10 = "엘레멘탈 응축1 - 엘레멘탈 가속1 - 엘레멘탈 가속2 - 3속성 엘레멘탈 증폭4"
item13_i11 = "개조 (바이스. 엘레멘탈 응축4)"
item13_i12 = "보석개조 (바이스) > 아쿠아마린 3cm, 재스퍼 3cm, 스피넬 3cm"

item14_name = "켈틱 드루이드 스태프"
item14_s_name = "켈드루"
item14_i1 = "여신의 의지를 담아 만들었다고 전해지는 스태프. 이 스태프의 고유의 특성을 잘 살려 개조한다면 매우 효율적으로 마나를 운용할 수 있게 된다. 3속성의 모든 마법을 사용할 수 있으며 중급 마법을 사용하기 위해 특별히 속성을 모을 필요도 없다. 스태프를 손에 쥐면 몸의 마나와 공명하게 되어 달리면서도 메디테이션을 할 수 있다."
item14_i2 = "공격력 17~39"
item14_i3 = "부상률 0~0%"
item14_i4 = "크리티컬 16%"
item14_i5 = "밸런스 65%"
item14_i6 = "내구력 13/13"
item14_i7 = "마법 공격력 3~12+ / 크리티컬 1~24+ / 내구력 1~17+"
item14_i8 = "매직 크래프트"
item14_i9 = "마력이 깃든 나무장작 3개, 온전한 실리엔 20개, 뮤턴트 2개, 망가진 고리형 구조체 12개, 봉인의 검은 금속 3개, 잊혀진 마법사의 보석 5개"
item14_i10 = "엘레멘탈 응축1 - 엘레멘탈 응축1 - 엘레멘탈 응축2 - 엘레멘탈 응축3"
item14_i11 = "개조 (바이스. 켈틱 드루이드 스태프 전용 개조)"
item14_i12 = "보석개조 (바이스) > 아쿠아마린 3cm, 재스퍼 3cm, 스피넬 3cm"

item15_name = "켈틱 가디언 스태프"
item15_s_name = "켈가스"
item15_i1 = "여신의 자애로움이 담겨 있다고 전해지는 스태프. 이 스태프를 사용하면 적에게 강력한 마법 공격을 할 수 있을 뿐 아니라 파티 힐링을 통해 동료들을 지키는 것이 가능하다. 3속성의 모든 마법을 사용할 수 있으며 중급 마법을 사용하기 위해 특별히 속성을 모을 필요도 없다. 스태프를 손에 쥐면 몸의 마나와 공명하게 되어 달리면서도 메디테이션을 할 수 있다."
item15_i2 = "공격력 17~39"
item15_i3 = "부상률 0~0%"
item15_i4 = "크리티컬 33%"
item15_i5 = "밸런스 65%"
item15_i6 = "내구력 14/14"
item15_i7 = "마법 공격력 4~10+ / 내구력 1~29+"
item15_i8 = "매직 크래프트"
item15_i9 = "마력이 깃든 나무장작 3개, 온전한 실리엔 20개, 뮤턴트 2개, 망가진 고리형 구조체 12개, 봉인의 검은 금속 8개, 잊혀진 마법사의 보석 4개"
item15_i10 = ""
item15_i11 = ""
item15_i12 = ""

item16_name = "켈틱 크로스보우"
item16_s_name = "켈크보"
item16_i1 = "여신의 숨결을 담아 만들었다고 하는 석궁. 뛰어난 균형미를 자랑하며 침착하게 화살을 쏜다."
item16_i2 = "공격력 20~45"
item16_i3 = "부상률 0~100%"
item16_i4 = "크리티컬 35%"
item16_i5 = "밸런스 70%"
item16_i6 = "내구력 18/18"
item16_i7 = "피어싱 1레벨"
item16_i8 = "목공"
item16_i9 = "최고급 나무장작 4개, 빛나는 질긴 끈 1개, 빛을 잃어버린 금속 파편 2개, 단단한 괴수의 뿔 2개"
item16_i10 = "니커의 석궁강화 - 활줄강화2 - 활줄강화3 - 활줄강화4"
item16_i11 = "퍼거스식 석궁개조 - 날카로운 마무리 (퍼거스)"
item16_i12 = "보석개조 (아이데른) > "

item17_name = "켈틱 테트라 실린더"
item17_s_name = "켈테실"
item17_i1 = "여신의 무기의 외형적 특징을 참고해 한차원 더 발전시킨 형태의 실린더. 적을 공격하는 모든 속성의 연금술 스킬 사용 시 효력이 크게 증가한다."
item17_i2 = "공격력 12~29"
item17_i3 = "부상률 10~20%"
item17_i4 = "크리티컬 25~28%"
item17_i5 = "밸런스 38~46%"
item17_i6 = "내구력 29/29"
item17_i7 = "모든 속성 대미지 30%"
item17_i8 = "은괴 2개, 미스릴괴 8개, 균열된 검은 금속 3개, 증폭된 연금술 결정 1개"
item17_i9 = "빛나는 결정 파편 6개, 대못 4개, 불완전한 봉인의 엠블럼 4개"
item17_i10 = "켈틱 테트라 실린더 전용 개조 - 4대 속성 활성화2 - 4대 속성 활성화3 - 4대 속성 활성화4 - 4대 속성 활성화5"
item17_i11 = "-"
item17_i12 = "보석개조 (아이바, 도렌, 헬레드) > 다이아몬드 3cm, 아쿠아마린 3cm, 가넷 5cm"

item18_name = "켈틱 다우라 제로"
item18_s_name = "켈다제"
item18_i1 = ""
item18_i2 = "공격력 9~27"
item18_i3 = "부상률 25~60%"
item18_i4 = "크리티컬 43%"
item18_i5 = "밸런스 32%"
item18_i6 = "내구력 32/32"
item18_i7 = "추가옵션 없음"
item18_i8 = "힐웬 공학"
item18_i9 = "힐웬 합금 15개, 에너지 컨버터 2개, 에메랄드 퓨즈 1개, 정화된 마법사의 보석 4개, 산산조각난 검은 금속 6개, 변형된 고리형 구조체 2개"
item18_i10 = "약실확장 - 강선추가1 - 강선추가2 - 총신확장 - 총신확장"
item18_i11 = "-"
item18_i12 = "보석개조(헥터) > 다이아몬드 3cm, 스피넬 3cm, 재스퍼 3cm"

item19_name = "켈틱 리스트릭트 핸들"
item19_s_name = "켈리핸"
item19_i1 = "여신의 무기의 외형적 특징을 참고해 만든 십자 모양의 철제 마리오네트 핸들. 시전자의 의지에 따라 적을 무기력하게 만들 수 있다."
item19_i2 = "공격력 29~42"
item19_i3 = "부상률 10~35%"
item19_i4 = "크리티컬 25%"
item19_i5 = "밸런스 32%"
item19_i6 = "내구력 24/24"
item19_i7 = "추가옵션 없음"
item19_i8 = "핸디크래프트"
item19_i9 = "특급 나무장작 5개, 금판 3개, 대못 10개, 정화된 마법사의 보석 4개, 산산조각난 검은 금속 6개, 악몽 파수꾼의 유물 2개"
item19_i10 = "핸들 길들이기 - 자루 조절1 - 자루 조절2 - 자루 조절3 "
item19_i11 = "핸들 맞춤 개조 또는 장인개조 (그라나트, 네리스 등. 맥뎀 10~30 / 크리티컬 4~6%)"
item19_i12 = "보석개조 (그라나트, 네리스 등) > 아쿠아마린 2cm, 스피넬 1cm, 에메랄드 1cm"

item20_name = "켈틱 엣지드 너클"
item20_s_name = "켈엣너"
item20_i1 = "여신의 무기의 외형적 특징을 참고해 만든 너클. 매우 단단한 금속 재질로 섬세하게 제작된 너클로 강력한 펀치를 구사할 수 있다. 날카롭게 벼린 칼날이 부착되어 치명적인 공격이 가능한다."
item20_i2 = "공격력 27~85"
item20_i3 = "부상률 10~25%"
item20_i4 = "크리티컬 48%"
item20_i5 = "밸런스 55%"
item20_i6 = "내구력 27/27"
item20_i7 = "추가옵션 없음"
item20_i8 = "은괴 2개, 미스릴괴 8개, 균열된 검은 금속 3개, 단호한 칼날의 파편 1개"
item20_i9 = "파괴된 봉인의 사슬 6개, 대못 4개, 불완전한 봉인의 엠블럼 4개"
item20_i10 = "켈틱 엣지드 너클 전용 개조1 - 징 갈기 - 체인 교체 - 중량화"
item20_i11 = "장인개조 (네리스, 니커 등. 맥뎀 0~18 / 의지 0~60 / 체력 0~30)"
item20_i12 = "보석개조 (네리스, 니커 등) > 다이아몬드 3cm, 스피넬 3cm, 재스퍼 3cm"

item21_name = "바펠세파르 헌터"
item21_s_name = "바펠"
item21_i1 = "블랙 드래곤, 바펠세파르를 처치한 자만이 가질 수 있다는 고대의 활. 바펠세파르 헌트리스와 한 쌍을 이뤘을 때 무한한 힘을 가진 마력의 화살을 쏠 수 있다. 일반적인 화살도 쏠 수 있다."
item21_i2 = "공격력 20~43"
item21_i3 = "부상률 20~60%"
item21_i4 = "크리티컬 34%"
item21_i5 = "밸런스 45%"
item21_i6 = "내구력 25/25"
item21_i7 = "피어싱 1레벨"
item21_i8 = "매직크래프트"
item21_i9 = "롱 보우 1개, 블랙 드래곤 눈알 1개, 드래곤의 살덩어리 5개, 블랙 드래곤의 피 5개, 온전한 실리엔 10개, 뮤턴트 1개"
item21_i10 = "활줄 강화1 - 조준기 교체 - 조준기 교체 - 활줄 강화 4"
item21_i11 = "개조 (네리스, 아이데른 등. 바펠세파르 헌터 봉인 해제)"
item21_i12 = "보석개조1 (네리스, 아이데른 등) > 다이아몬드 5cm, 스피넬 5cm, 재스퍼 5cm"

item22_name = "바펠세파르 헌트리스"
item22_s_name = "바펠화살"
item22_i1 = "블랙 드래곤, 바펠세파르를 처치한 자만이 가질 수 있다는 특별한 화살. 바펠세파르 헌터와 한 쌍을 이뤘을 때 무한한 힘을 가진 마력의 화살을 쏠 수 있다. 일반적인 활에는 장비할 수 없다."
item22_i2 = "공격력 15~30 추가"
item22_i3 = "부상률 -"
item22_i4 = "크리티컬 -"
item22_i5 = "밸런스 -"
item22_i6 = "내구력 -"
item22_i7 = "총 추가 데미지 15%"
item22_i8 = "매직크래프트"
item22_i9 = "화살 100개, 온전한 실리엔 10개, 뮤턴트, 블랙 드래곤의 심장 1개, 블랙 드래곤의 피 3개"
item22_i10 = "-"
item22_i11 = "-"
item22_i12 = "-"

item23_name = "다우라 SE"
item23_s_name = "다우라"
item23_i1 = "에너지 증폭 장치가 추가된 후기형 듀얼 건. 다우라 전용으로 제작된 이 듀얼 건은 빠른 연사 속도와 높은 장탄량을 자랑한다."
item23_i2 = "공격력 10~22"
item23_i3 = "부상률 25~60%"
item23_i4 = "크리티컬 50%"
item23_i5 = "밸런스 35%"
item23_i6 = "내구력 28/28"
item23_i7 = "탄환 64"
item23_i8 = "힐웬 공학"
item23_i9 = "힐웬 합금 15개, 육각 볼트 8개, 육각 너트 8개, 에너지 컨버터 2개, 에메랄드 퓨즈 1개, 에너지 증폭 장치 1개"
item23_i10 = "약실 확장 - 강선 추가1 - 강선 추가2 - 총신 확장"
item23_i11 = "개조 (헥터. 총신 확장)"
item23_i12 = "보석개조1 (헥터) > 다이아몬트 3cm, 스피넬 3cm, 재스퍼 3cm"

a = {
        item1_name : { "b": item1_name, "c": item1_i1, "d": item1_i2, "e": item1_i3, "f": item1_i4, "g": item1_i5, "h": item1_i6,"i": item1_i7,"j": s, "k": g, "l": item1_i8, "m": m, "n": item1_i9, "o": s, "p": ga, "q": item1_i10, "r": item1_i11, "s": item1_i12},
        item1_s_name : { "b": item1_name, "c": item1_i1, "d": item1_i2, "e": item1_i3, "f": item1_i4, "g": item1_i5, "h": item1_i6,"i": item1_i7,"j": s, "k": g, "l": item1_i8, "m": m, "n": item1_i9, "o": s, "p": ga, "q": item1_i10, "r": item1_i11, "s": item1_i12},
        item2_name : { "b": item2_name, "c": item2_i1, "d": item2_i2, "e": item2_i3, "f": item2_i4, "g": item2_i5, "h": item2_i6,"i": item2_i7,"j": s, "k": g, "l": item2_i8, "m": m, "n": item2_i9, "o": s, "p": ga, "q": item2_i10, "r": item2_i11, "s": item2_i12},
        item2_s_name : { "b": item2_name, "c": item2_i1, "d": item2_i2, "e": item2_i3, "f": item2_i4, "g": item2_i5, "h": item2_i6,"i": item2_i7,"j": s, "k": g, "l": item2_i8, "m": m, "n": item2_i9, "o": s, "p": ga, "q": item2_i10, "r": item2_i11, "s": item2_i12},
        item3_name : { "b": item3_name, "c": item3_i1, "d": item3_i2, "e": item3_i3, "f": item3_i4, "g": item3_i5, "h": item3_i6,"i": item3_i7,"j": s, "k": g, "l": item3_i8, "m": m, "n": item3_i9, "o": s, "p": ga, "q": item3_i10, "r": item3_i11, "s": item3_i12},
        item3_s_name : { "b": item3_name, "c": item3_i1, "d": item3_i2, "e": item3_i3, "f": item3_i4, "g": item3_i5, "h": item3_i6,"i": item3_i7,"j": s, "k": g, "l": item3_i8, "m": m, "n": item3_i9, "o": s, "p": ga, "q": item3_i10, "r": item3_i11, "s": item3_i12},
        item4_name : { "b": item4_name, "c": item4_i1, "d": item4_i2, "e": item4_i3, "f": item4_i4, "g": item4_i5, "h": item4_i6,"i": item4_i7,"j": s, "k": g, "l": item4_i8, "m": m, "n": item4_i9, "o": s, "p": ga, "q": item4_i10, "r": item4_i11, "s": item4_i12},
        item4_s_name : { "b": item4_name, "c": item4_i1, "d": item4_i2, "e": item4_i3, "f": item4_i4, "g": item4_i5, "h": item4_i6,"i": item4_i7,"j": s, "k": g, "l": item4_i8, "m": m, "n": item4_i9, "o": s, "p": ga, "q": item4_i10, "r": item4_i11, "s": item4_i12},
        item5_name : { "b": item5_name, "c": item5_i1, "d": item5_i2, "e": item5_i3, "f": item5_i4, "g": item5_i5, "h": item5_i6,"i": item5_i7,"j": s, "k": g, "l": item5_i8, "m": m, "n": item5_i9, "o": s, "p": ga, "q": item5_i10, "r": item5_i11, "s": item5_i12},
        item5_s_name : { "b": item5_name, "c": item5_i1, "d": item5_i2, "e": item5_i3, "f": item5_i4, "g": item5_i5, "h": item5_i6,"i": item5_i7,"j": s, "k": g, "l": item5_i8, "m": m, "n": item5_i9, "o": s, "p": ga, "q": item5_i10, "r": item5_i11, "s": item5_i12},
        item6_name : { "b": item6_name, "c": item6_i1, "d": item6_i2, "e": item6_i3, "f": item6_i4, "g": item6_i5, "h": item6_i6,"i": item6_i7,"j": s, "k": g, "l": item6_i8, "m": m, "n": item6_i9, "o": s, "p": ga, "q": item6_i10, "r": item6_i11, "s": item6_i12},
        item6_s_name : { "b": item6_name, "c": item6_i1, "d": item6_i2, "e": item6_i3, "f": item6_i4, "g": item6_i5, "h": item6_i6,"i": item6_i7,"j": s, "k": g, "l": item6_i8, "m": m, "n": item6_i9, "o": s, "p": ga, "q": item6_i10, "r": item6_i11, "s": item6_i12},
        item7_name : { "b": item7_name, "c": item7_i1, "d": item7_i2, "e": item7_i3, "f": item7_i4, "g": item7_i5, "h": item7_i6,"i": item7_i7,"j": s, "k": g, "l": item7_i8, "m": m, "n": item7_i9, "o": s, "p": ga, "q": item7_i10, "r": item7_i11, "s": item7_i12},
        item7_s_name : { "b": item7_name, "c": item7_i1, "d": item7_i2, "e": item7_i3, "f": item7_i4, "g": item7_i5, "h": item7_i6,"i": item7_i7,"j": s, "k": g, "l": item7_i8, "m": m, "n": item7_i9, "o": s, "p": ga, "q": item7_i10, "r": item7_i11, "s": item7_i12},
        item8_name : { "b": item8_name, "c": item8_i1, "d": item8_i2, "e": item8_i3, "f": item8_i4, "g": item8_i5, "h": item8_i6,"i": item8_i7,"j": s, "k": g, "l": item8_i8, "m": m, "n": item8_i9, "o": s, "p": ga, "q": item8_i10, "r": item8_i11, "s": item8_i12},
        item8_s_name : { "b": item8_name, "c": item8_i1, "d": item8_i2, "e": item8_i3, "f": item8_i4, "g": item8_i5, "h": item8_i6,"i": item8_i7,"j": s, "k": g, "l": item8_i8, "m": m, "n": item8_i9, "o": s, "p": ga, "q": item8_i10, "r": item8_i11, "s": item8_i12},
        item9_name : { "b": item9_name, "c": item9_i1, "d": item9_i2, "e": item9_i3, "f": item9_i4, "g": item9_i5, "h": item9_i6,"i": item9_i7,"j": s, "k": g, "l": item9_i8, "m": m, "n": item9_i9, "o": s, "p": ga, "q": item9_i10, "r": item9_i11, "s": item9_i12},
        item9_s_name : { "b": item9_name, "c": item9_i1, "d": item9_i2, "e": item9_i3, "f": item9_i4, "g": item9_i5, "h": item9_i6,"i": item9_i7,"j": s, "k": g, "l": item9_i8, "m": m, "n": item9_i9, "o": s, "p": ga, "q": item9_i10, "r": item9_i11, "s": item9_i12},
        item10_name : { "b": item10_name, "c": item10_i1, "d": item10_i2, "e": item10_i3, "f": item10_i4, "g": item10_i5, "h": item10_i6,"i": item10_i7,"j": s, "k": g, "l": item10_i8, "m": m, "n": item10_i9, "o": s, "p": ga, "q": item10_i10, "r": item10_i11, "s": item10_i12},
        item10_s_name : { "b": item10_name, "c": item10_i1, "d": item10_i2, "e": item10_i3, "f": item10_i4, "g": item10_i5, "h": item10_i6,"i": item10_i7,"j": s, "k": g, "l": item10_i8, "m": m, "n": item10_i9, "o": s, "p": ga, "q": item10_i10, "r": item10_i11, "s": item10_i12},
        item11_name : { "b": item11_name, "c": item11_i1, "d": item11_i2, "e": item11_i3, "f": item11_i4, "g": item11_i5, "h": item11_i6,"i": item11_i7,"j": s, "k": g, "l": item11_i8, "m": m, "n": item11_i9, "o": s, "p": ga, "q": item11_i10, "r": item11_i11, "s": item11_i12},
        item11_s_name : { "b": item11_name, "c": item11_i1, "d": item11_i2, "e": item11_i3, "f": item11_i4, "g": item11_i5, "h": item11_i6,"i": item11_i7,"j": s, "k": g, "l": item11_i8, "m": m, "n": item11_i9, "o": s, "p": ga, "q": item11_i10, "r": item11_i11, "s": item11_i12},
        item12_name : { "b": item12_name, "c": item12_i1, "d": item12_i2, "e": item12_i3, "f": item12_i4, "g": item12_i5, "h": item12_i6,"i": item12_i7,"j": s, "k": g, "l": item12_i8, "m": m, "n": item12_i9, "o": s, "p": ga, "q": item12_i10, "r": item12_i11, "s": item12_i12},
        item12_s_name : { "b": item12_name, "c": item12_i1, "d": item12_i2, "e": item12_i3, "f": item12_i4, "g": item12_i5, "h": item12_i6,"i": item12_i7,"j": s, "k": g, "l": item12_i8, "m": m, "n": item12_i9, "o": s, "p": ga, "q": item12_i10, "r": item12_i11, "s": item12_i12},
        item13_name : { "b": item13_name, "c": item13_i1, "d": item13_i2, "e": item13_i3, "f": item13_i4, "g": item13_i5, "h": item13_i6,"i": item13_i7,"j": s, "k": g, "l": item13_i8, "m": m, "n": item13_i9, "o": s, "p": ga, "q": item13_i10, "r": item13_i11, "s": item13_i12},
        item13_s_name : { "b": item13_name, "c": item13_i1, "d": item13_i2, "e": item13_i3, "f": item13_i4, "g": item13_i5, "h": item13_i6,"i": item13_i7,"j": s, "k": g, "l": item13_i8, "m": m, "n": item13_i9, "o": s, "p": ga, "q": item13_i10, "r": item13_i11, "s": item13_i12},
        item14_name : { "b": item14_name, "c": item14_i1, "d": item14_i2, "e": item14_i3, "f": item14_i4, "g": item14_i5, "h": item14_i6,"i": item14_i7,"j": s, "k": g, "l": item14_i8, "m": m, "n": item14_i9, "o": s, "p": ga, "q": item14_i10, "r": item14_i11, "s": item14_i12},
        item14_s_name : { "b": item14_name, "c": item14_i1, "d": item14_i2, "e": item14_i3, "f": item14_i4, "g": item14_i5, "h": item14_i6,"i": item14_i7,"j": s, "k": g, "l": item14_i8, "m": m, "n": item14_i9, "o": s, "p": ga, "q": item14_i10, "r": item14_i11, "s": item14_i12},
        item15_name : { "b": item15_name, "c": item15_i1, "d": item15_i2, "e": item15_i3, "f": item15_i4, "g": item15_i5, "h": item15_i6,"i": item15_i7,"j": s, "k": g, "l": item15_i8, "m": m, "n": item15_i9, "o": s, "p": ga, "q": item15_i10, "r": item15_i11, "s": item15_i12},
        item15_s_name : { "b": item15_name, "c": item15_i1, "d": item15_i2, "e": item15_i3, "f": item15_i4, "g": item15_i5, "h": item15_i6,"i": item15_i7,"j": s, "k": g, "l": item15_i8, "m": m, "n": item15_i9, "o": s, "p": ga, "q": item15_i10, "r": item15_i11, "s": item15_i12},
        item16_name : { "b": item16_name, "c": item16_i1, "d": item16_i2, "e": item16_i3, "f": item16_i4, "g": item16_i5, "h": item16_i6,"i": item16_i7,"j": s, "k": g, "l": item16_i8, "m": m, "n": item16_i9, "o": s, "p": ga, "q": item16_i10, "r": item16_i11, "s": item16_i12},
        item16_s_name : { "b": item16_name, "c": item16_i1, "d": item16_i2, "e": item16_i3, "f": item16_i4, "g": item16_i5, "h": item16_i6,"i": item16_i7,"j": s, "k": g, "l": item16_i8, "m": m, "n": item16_i9, "o": s, "p": ga, "q": item16_i10, "r": item16_i11, "s": item16_i12},
        item17_name : { "b": item17_name, "c": item17_i1, "d": item17_i2, "e": item17_i3, "f": item17_i4, "g": item17_i5, "h": item17_i6,"i": item17_i7,"j": s, "k": g, "l": item17_i8, "m": m, "n": item17_i9, "o": s, "p": ga, "q": item17_i10, "r": item17_i11, "s": item17_i12},
        item17_s_name : { "b": item17_name, "c": item17_i1, "d": item17_i2, "e": item17_i3, "f": item17_i4, "g": item17_i5, "h": item17_i6,"i": item17_i7,"j": s, "k": g, "l": item17_i8, "m": m, "n": item17_i9, "o": s, "p": ga, "q": item17_i10, "r": item17_i11, "s": item17_i12},
        item18_name : { "b": item18_name, "c": item18_i1, "d": item18_i2, "e": item18_i3, "f": item18_i4, "g": item18_i5, "h": item18_i6,"i": item18_i7,"j": s, "k": g, "l": item18_i8, "m": m, "n": item18_i9, "o": s, "p": ga, "q": item18_i10, "r": item18_i11, "s": item18_i12},
        item18_s_name : { "b": item18_name, "c": item18_i1, "d": item18_i2, "e": item18_i3, "f": item18_i4, "g": item18_i5, "h": item18_i6,"i": item18_i7,"j": s, "k": g, "l": item18_i8, "m": m, "n": item18_i9, "o": s, "p": ga, "q": item18_i10, "r": item18_i11, "s": item18_i12},
        item19_name : { "b": item19_name, "c": item19_i1, "d": item19_i2, "e": item19_i3, "f": item19_i4, "g": item19_i5, "h": item19_i6,"i": item19_i7,"j": s, "k": g, "l": item19_i8, "m": m, "n": item19_i9, "o": s, "p": ga, "q": item19_i10, "r": item19_i11, "s": item19_i12},
        item19_s_name : { "b": item19_name, "c": item19_i1, "d": item19_i2, "e": item19_i3, "f": item19_i4, "g": item19_i5, "h": item19_i6,"i": item19_i7,"j": s, "k": g, "l": item19_i8, "m": m, "n": item19_i9, "o": s, "p": ga, "q": item19_i10, "r": item19_i11, "s": item19_i12},
        item20_name : { "b": item20_name, "c": item20_i1, "d": item20_i2, "e": item20_i3, "f": item20_i4, "g": item20_i5, "h": item20_i6,"i": item20_i7,"j": s, "k": g, "l": item20_i8, "m": m, "n": item20_i9, "o": s, "p": ga, "q": item20_i10, "r": item20_i11, "s": item20_i12},
        item20_s_name : { "b": item20_name, "c": item20_i1, "d": item20_i2, "e": item20_i3, "f": item20_i4, "g": item20_i5, "h": item20_i6,"i": item20_i7,"j": s, "k": g, "l": item20_i8, "m": m, "n": item20_i9, "o": s, "p": ga, "q": item20_i10, "r": item20_i11, "s": item20_i12},
        item21_name : { "b": item21_name, "c": item21_i1, "d": item21_i2, "e": item21_i3, "f": item21_i4, "g": item21_i5, "h": item21_i6,"i": item21_i7,"j": s, "k": g, "l": item21_i8, "m": m, "n": item21_i9, "o": s, "p": ga, "q": item21_i10, "r": item21_i11, "s": item21_i12},
        item21_s_name : { "b": item21_name, "c": item21_i1, "d": item21_i2, "e": item21_i3, "f": item21_i4, "g": item21_i5, "h": item21_i6,"i": item21_i7,"j": s, "k": g, "l": item21_i8, "m": m, "n": item21_i9, "o": s, "p": ga, "q": item21_i10, "r": item21_i11, "s": item21_i12},
        item22_name : { "b": item22_name, "c": item22_i1, "d": item22_i2, "e": item22_i3, "f": item22_i4, "g": item22_i5, "h": item22_i6,"i": item22_i7,"j": s, "k": g, "l": item22_i8, "m": m, "n": item22_i9, "o": s, "p": ga, "q": item22_i10, "r": item22_i11, "s": item22_i12},
        item22_s_name : { "b": item22_name, "c": item22_i1, "d": item22_i2, "e": item22_i3, "f": item22_i4, "g": item22_i5, "h": item22_i6,"i": item22_i7,"j": s, "k": g, "l": item22_i8, "m": m, "n": item22_i9, "o": s, "p": ga, "q": item22_i10, "r": item22_i11, "s": item22_i12},
        item23_name : { "b": item23_name, "c": item23_i1, "d": item23_i2, "e": item23_i3, "f": item23_i4, "g": item23_i5, "h": item23_i6,"i": item23_i7,"j": s, "k": g, "l": item23_i8, "m": m, "n": item23_i9, "o": s, "p": ga, "q": item23_i10, "r": item23_i11, "s": item23_i12},
        item23_s_name : { "b": item23_name, "c": item23_i1, "d": item23_i2, "e": item23_i3, "f": item23_i4, "g": item23_i5, "h": item23_i6,"i": item23_i7,"j": s, "k": g, "l": item23_i8, "m": m, "n": item23_i9, "o": s, "p": ga, "q": item23_i10, "r": item23_i11, "s": item23_i12}
}    

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="게임 하는중"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",'정보 봇',"봇 아이디:",'1022184013714182174',"봇 버전:",discord.__version__)

@client.command()
async def 정보(ctx, *, txt):    
    try:
        w1 = a[txt]["b"]
        w2 = a[txt]["c"]
        w3 = a[txt]["d"]
        w4 = a[txt]["e"]
        w5 = a[txt]["f"]
        w6 = a[txt]["g"]
        w7 = a[txt]["h"]
        w8 = a[txt]["i"]
        w9 = a[txt]["j"]
        w10 = a[txt]["k"]
        w11 = a[txt]["l"]
        w12 = a[txt]["m"]
        w13 = a[txt]["n"]
        w14 = a[txt]["o"]
        w15 = a[txt]["p"]
        w16 = a[txt]["q"]
        w17 = a[txt]["r"]
        w18 = a[txt]["s"]

        embed=discord.Embed(title=w1, description=w2, color=discord.Color.random())
        embed.set_footer(text=w3 + j + w4 + j + w5 + j + w6 + j + w7 + j + w8 + j + w9 + j + w10 + j + w11 + j + w12 + j + w13 + j + w14 + j + w15 + j + w16 + j + w17 + j + w18)
        embed.set_image(url="https://cdn.discordapp.com/emojis/1022110046139732061.webp?size=160&quality=lossless")
        await ctx.send(embed=embed)
    except:
        await ctx.channel.send('등록되지 않은 무기 입니다.')

client.run(os.environ['token'])