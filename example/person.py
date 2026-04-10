class Person:    # EMP 테이블 한 행(row)을 객체로 표현
    def __init__(self,empno, ename, job, mgr, hiredate, sal, comm, deptno):
        self.empno = empno
        self.ename = ename
        self.job = job
        self.mgr = mgr
        self.hiredate = hiredate
        self.sal= sal
        self.comm = comm
        self.deptno = deptno

    def print_person(self):
        print(f"{self.empno} : {self.ename} : {self.sal}")