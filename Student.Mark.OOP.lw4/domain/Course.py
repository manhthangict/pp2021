Course = []
CourseID = []
CourseName = []
Credit = []

class Cse:
    def __init__(self, cid, cname):
        self._cid = cid
        self._cname = cname

        Course.append(self)
        CourseID.append(self._cid)

    def get_id(self):
        return self._cid

    def get_name(self):
        return self.cname