class node:
    def __init__(self, lastName, IO, year, oklad):
        self.lastName = lastName
        self.IO = IO
        self.year = year
        self.oklad = oklad
        self.next = None

    def setLastName(self, lastName):
        self.lastName = lastName

    def setIO(self, IO):
        self.IO = IO

    def setYear(self, year):
        self.year = year

    def setOklad(self, oklad):
        self.oklad = oklad

    def getLastName(self):
        return self.lastName

    def getIO(self):
        return self.IO

    def getYear(self):
        return self.year

    def getOklad(self):
        return self.oklad


class linked_list:
    def __init__(self):
        self.head = node('', '', 0, 0)
        self.last = None

    def append(self, data):
        new_node = node(data.lastName, data.IO, data.year, data.oklad)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elems.append(cur_node)
        print(elems)

    def get(self, index):
        if index >= self.length() or index < 0:
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node
            cur_idx += 1

    def __getitem__(self, index):
        return self.get(index)

    def erase(self, index):
        if index >= self.length() or index < 0:
            print("ERROR: 'Erase' Index out of range!")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

    def insert(self, index, data):
        if index >= self.length() or index < 0:
            return self.append(data)
        cur_node = self.head
        prior_node = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                new_node = node(data.lastName, data.IO, data.year, data.oklad)
                prior_node.next = new_node
                new_node.next = cur_node
                return
            prior_node = cur_node
            cur_idx += 1

    def printToFile(self):
        f = open('list000.txt', 'w')
        for i in range(self.length() - 1):
            f.write(self[i].getLastName() + " " +
                    self[i].getIO() + " " +
                    str(self[i].getYear()) + " " +
                    str(self[i].getOklad()) + "\n")
        f.write(self[self.length() - 1].getLastName() + " " +
                self[self.length() - 1].getIO() + " " +
                str(self[self.length() - 1].getYear()) + " " +
                str(self[self.length() - 1].getOklad()))
        f.close()

    def sortOklad(self):
        a = node('', '', 0, 0)
        b = node('', '', 0, 0)
        c = node('', '', 0, 0)
        e = node('', '', 0, 0)
        tmp = node('', '', 0, 0)

        while (e != self.head.next):
            c = a = self.head
            b = a.next

            while a != e:
                if a and b:
                    if int(a.oklad) > int(b.oklad):
                        if a == self.head:
                            tmp = b.next
                            b.next = a
                            a.next = tmp
                            self.head = b
                            c = b
                        else:
                            tmp = b.next
                            b.next = a
                            a.next = tmp
                            c.next = b
                            c = b
                    else:
                        c = a
                        a = a.next
                    b = a.next
                    if b == e:
                        e = a
                else:
                    e = a

        self.printToFile()

    def sortName(self):
        a = node('', '', 0, 0)
        b = node('', '', 0, 0)
        c = node('', '', 0, 0)
        e = node('', '', 0, 0)
        tmp = node('', '', 0, 0)

        while (e != self.head.next):
            c = a = self.head
            b = a.next

            while a != e:
                if a and b:
                    if a.lastName > b.lastName:
                        if a == self.head:
                            tmp = b.next
                            b.next = a
                            a.next = tmp
                            self.head = b
                            c = b
                        else:
                            tmp = b.next
                            b.next = a
                            a.next = tmp
                            c.next = b
                            c = b
                    else:
                        c = a
                        a = a.next
                    b = a.next
                    if b == e:
                        e = a
                else:
                    e = a

        self.printToFile()

    def sortAge(self):
        a = node('', '', int(0), int(0))
        b = node('', '', int(0), int(0))
        c = node('', '', 0, 0)
        e = node('', '', 0, 0)
        tmp = node('', '', 0, 0)

        while (e != self.head.next):
            c = a = self.head
            b = a.next

            while a != e:
                if a and b:
                    if int(a.year) > int(b.year):
                        if a == self.head:
                            tmp = b.next
                            b.next = a
                            a.next = tmp
                            self.head = b
                            c = b
                        else:
                            tmp = b.next
                            b.next = a
                            a.next = tmp
                            c.next = b
                            c = b
                    else:
                        c = a
                        a = a.next
                    b = a.next
                    if b == e:
                        e = a
                else:
                    e = a

        self.printToFile()
