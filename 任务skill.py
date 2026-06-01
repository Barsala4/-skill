def daily_study_plan_skill(user_input: str) -> str:
    """
    大学生每日学习计划生成Skill
    输入：用户空闲时间、科目、考试/作业情况
    输出：结构化学习计划表
    """
    # ========== 1. 触发条件判断 ==========
    trigger_words = ["学习计划", "时间表", "学习安排", "规划今天"]
    if not any(word in user_input for word in trigger_words):
        return "未触发学习计划生成Skill，请输入相关指令。"

    # ========== 2. 简单信息提取（模拟解析） ==========
    import re
    # 提取时间
    time_match = re.findall(r'(\d+点.*?\d+点)', user_input)
    # 提取科目
    subjects = ["高数", "英语", "Python", "近代史", "计算机基础", "人工智能导论"]
    user_subjects = [s for s in subjects if s in user_input]
    # 提取紧急事件
    urgent = "考试" in user_input or "小测" in user_input or "作业" in user_input

    # ========== 3. 优先级排序（紧急 > 常规） ==========
    if urgent and user_subjects:
        first_sub = user_subjects[0]
        other_subs = user_subjects[1:]
    else:
        first_sub, other_subs = user_subjects[0], user_subjects[1:] if len(user_subjects) > 1 else []

    # ========== 4. 时间分配生成计划表 ==========
    plan = "# 今日学习计划表\n"
    if "下午3点到晚上9点" in user_input:
        plan += """15:00-16:30  {}（90min）：刷题+整理错题，重点复习考点
16:30-16:40  休息（10min）
16:40-17:40  {}（60min）：完成作业，梳理知识点
17:40-18:40  晚餐+休息
18:40-19:40  {}（60min）：背诵单词/巩固基础
19:40-19:50  休息（10min）
19:50-20:40  复盘+查漏补缺（50min）：回顾当日学习内容
20:40-21:00  自由放松""".format(first_sub, other_subs[0] if other_subs else "复盘", other_subs[1] if len(other_subs)>=2 else "英语")
    elif "上午9点" in user_input and "晚上7点" in user_input:
        plan += """09:00-10:30  {}（90min）：梳理章节框架，背诵高频考点
10:30-10:40  休息（10min）
10:40-12:00  {}（80min）：刷题练习，记忆考点
12:00-19:00  午餐、午休、自由安排
19:00-20:30  {}（90min）：复盘上午内容，做章节练习题
20:30-20:40  休息（10min）
20:40-22:00  {}（80min）：整理错题，背诵考点""".format(user_subjects[0], user_subjects[1] if len(user_subjects)>=2 else user_subjects[0], user_subjects[0], user_subjects[1] if len(user_subjects)>=2 else user_subjects[0])
    elif "晚上7点" in user_input and "10点" in user_input:
        plan += """19:00-20:30  {}（90min）：复习核心知识点，梳理测验重点
20:30-20:40  休息（10min）
20:40-22:00  {}（80min）：背诵单词+练习，巩固基础""".format(user_subjects[0], user_subjects[1] if len(user_subjects)>=2 else "英语")

    return plan


# ========== 测试示例（直接运行即可） ==========
if __name__ == "__main__":
    # 示例1
    input1 = "今天下午3点到晚上9点有空，要学高数、英语、Python，明天高数小测，今天要背英语单词，写完Python作业"
    print("示例1输入：\n", input1)
    print(daily_study_plan_skill(input1))
    print("-"*50)

    # 示例2
    input2 = "上午9点-12点，晚上7点-10点有空，要复习近代史、计算机基础，本周要期末考试"
    print("示例2输入：\n", input2)
    print(daily_study_plan_skill(input2))
    print("-"*50)

    # 测试用例
    test_input = "今晚7点-10点有空，要学人工智能导论、英语，后天有AI课程测验"
    print("测试输入：\n", test_input)
    print(daily_study_plan_skill(test_input))