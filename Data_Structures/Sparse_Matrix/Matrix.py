from Obj.Day import Day
from Obj.Hour import Hour
from Data_Structures.Sparse_Matrix.Header import Header
from Data_Structures.Sparse_Matrix.List_Task import List_Task

class Matrix:
    def __init__(self):
        self.head_row = Header()
        self.head_column = Header()

    def add_task(self, _hour, _day, _task):
        ls_task = self.insert(_hour, _day, _task)
        if ls_task is not None:
            ls_task.insert(_hour, _day, _task)

    def insert(self, _hour, _day, _task):
        hour = Hour(_hour)
        nodeRow = self.head_row.insert(hour) #insert header row

        day = Day(_day)
        nodeCol = self.head_column.insert(day) #insert header column

        #new headers
        if nodeRow.right is None and nodeCol.down is None:
            new_lsTask = self.new_list_task(_hour, _day, _task)
            #associating headers
            nodeRow.right = new_lsTask
            nodeCol.down = new_lsTask
            return None
        elif nodeRow.right is not None and nodeCol.down is None: #exist row and not column
            new_lsTask = self.new_list_task(_hour, _day, _task)
            nodeCol.down = new_lsTask #link the new header

            if new_lsTask.column < nodeRow.right.column:
                new_lsTask.right = nodeRow.right
                nodeRow.right.left = new_lsTask
                nodeRow.right = new_lsTask
                return None
            else:
                tmp = nodeRow.right
                insertPrevious = False
                while tmp.right is not None:
                    if new_lsTask.column > tmp.column and new_lsTask.column < tmp.right.column: #insert to half
                        new_lsTask.right = tmp.right
                        tmp.right.left = new_lsTask
                        tmp.right = new_lsTask
                        new_lsTask.left = tmp
                        insertPrevious = True
                        return None
                    tmp = tmp.right
                if not insertPrevious: #insert to the end
                    tmp.right = new_lsTask
                    new_lsTask.left = tmp
                    return None
        elif nodeRow.right is None and nodeCol.down is not None: #exist colomn and not row
            #link new header
            new_lsTask = self.new_list_task(_hour, _day, _task)
            nodeRow.right = new_lsTask
            #search position in columns
            if new_lsTask.row < nodeCol.down.row:
                new_lsTask.down = nodeCol.down
                nodeCol.down.up = new_lsTask
                nodeCol.down = new_lsTask
                return None
            else:
                tmp = nodeCol.down
                flagInsertion = False
                while tmp.down is not None:
                    if new_lsTask.row > tmp.row and new_lsTask.row < tmp.down.row: #insert to half
                        new_lsTask.down = tmp.down
                        tmp.down.up = new_lsTask
                        tmp.down = new_lsTask
                        new_lsTask.up = tmp
                        flagInsertion = True
                        return None
                    tmp = tmp.down
                if not flagInsertion: #insert to the end
                    tmp.down = new_lsTask
                    new_lsTask.up = tmp
                    return None
        else: #exist the headers
            new_lsTask = self.new_list_task(_hour, _day, _task)
            #validate to start (rows)
            if new_lsTask.column < nodeRow.right.column:
                new_lsTask.right = nodeRow.right
                nodeRow.right.left = new_lsTask
                nodeRow.right = new_lsTask
            elif new_lsTask.column == nodeRow.right.column:
                print(f"Ya existe hacia la derecha {new_lsTask.row} {new_lsTask.column}") #only have one list in a position
                return nodeRow.right
            else:
                tmp = nodeRow.right
                flagInsertion = False
                while tmp.right is not None:
                    if new_lsTask.column == tmp.column:
                        print(f"Ya existe hacia la derecha no primero {new_lsTask.row} {new_lsTask.column}")
                        flagInsertion = True
                        return tmp
                    if new_lsTask.column > tmp.column and new_lsTask.column < tmp.right.column:
                        new_lsTask.right = tmp.right
                        tmp.right.left = new_lsTask
                        tmp.right = new_lsTask
                        new_lsTask.left = tmp
                        flagInsertion = True
                        break
                    tmp = tmp.right
                if not flagInsertion: #insert to the end
                    tmp.right = new_lsTask
                    new_lsTask.left = tmp
            if new_lsTask.row < nodeCol.down.row:
                new_lsTask.down = nodeCol.down
                nodeCol.down.up = new_lsTask
                nodeCol.down = new_lsTask
            elif new_lsTask.row == nodeCol.down.row:
                print(f"ya existe hacia abajo {new_lsTask.row} {new_lsTask.column}")
                return nodeCol.down
            else:
                tmp = nodeCol.down
                flagInsertion = False
                while tmp.down is not None:
                    if new_lsTask.row == tmp.row:
                        print(f"ya existe hacia abajo no prim {new_lsTask.row} {new_lsTask.column}")
                        flagInsertion = True #not add to the end
                        return tmp
                    if new_lsTask.row > tmp.row and new_lsTask.row < tmp.down.row: #insert to the half
                        new_lsTask.down = tmp.down
                        tmp.down.up = new_lsTask
                        tmp.down = new_lsTask
                        new_lsTask.up = tmp
                        flagInsertion = True
                        break
                    tmp = tmp.down
                if not flagInsertion: #insert to the end
                    tmp.down = new_lsTask
                    new_lsTask.up = tmp
        return None

    def new_list_task(self, _hour, _day, _task):
        ls_task = List_Task()
        ls_task.insert(_hour, _day, _task)
        return ls_task
