#练习处理一批学生成绩，计算统计信息，容错处理
students = [{"name":"张三","score":90},
            {"name":"李四","score":"92"},
            {"name":"王五","score":78},
            {"name":"赵六","score":"abc"},
            {"name":"钱七","score":-10},
            {"name":"孙八","score":"88"}]
def process_scores(students_list):
    valid_scores = []
    errors = []
    class RaiseValueError(Exception):
        pass
    for student in students_list:
        try:
            score = int(student["score"])  
            if score < 0 or score > 100:
                raise RaiseValueError(f"成绩 {score} 无效，必须在 0 到 100 之间")
            valid_scores.append(score)
        except ValueError:
            errors.append(f"学生 {student['name']} 的成绩 {student['score']} 不是数字")
        except KeyError:
            errors.append(f"学生 {student['name']} 缺少成绩字段")
        except RaiseValueError as e:
            errors.append(f"学生 {student['name']} 的成绩处理出现错误: {str(e)}")
        pass
    return valid_scores, errors

valid_scores, errors = process_scores(students)
print("有效成绩：", valid_scores,"错误信息：", errors)