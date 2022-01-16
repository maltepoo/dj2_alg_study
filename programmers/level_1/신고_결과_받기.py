def solution(id_list, report, k):
    mail = [0]*len(id_list)
    report_list = {}
    report = set(report)
    for r in report:
        reporter, reported = r.split()
        if reported in report_list:
            report_list[reported].append(reporter)
        else:
            report_list[reported] = [reporter]
    for i in id_list:
        if i in report_list and len(report_list[i]) >= k:
            for j in report_list[i]:
                mail[id_list.index(j)] += 1
    return mail